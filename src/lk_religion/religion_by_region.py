import csv
import json
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from gig import Ent
from matplotlib.cm import ScalarMappable
from matplotlib.colors import TwoSlopeNorm
from matplotlib.ticker import PercentFormatter


RELIGIONS = [
    'Buddhist',
    'Hindu',
    'Islam',
    'RomanCatholic',
    'OtherChristian',
    'Other',
]
RELIGION_LABELS = {
    'Buddhist': 'Buddhist',
    'Hindu': 'Hindu',
    'Islam': 'Islam',
    'RomanCatholic': 'Roman Catholic',
    'OtherChristian': 'Other Christian',
    'Other': 'Other',
}
RAW_RELIGION_FIELD_MAP = {
    'buddhist': 'Buddhist',
    'hindu': 'Hindu',
    'islam': 'Islam',
    'roman_catholic': 'RomanCatholic',
    'other_christian': 'OtherChristian',
    'other': 'Other',
}
YEARS = 2024 - 2012
GIG_2012_RELIGION_URL = (
    'https://raw.githubusercontent.com/nuuuwan/gig-data/'
    '61d6fcf20d5379acebe90abf581a61a3f9f4514c/'
    'gig2/population-religion.regions.2012.tsv'
)
CENSUS_2024_RELIGION_URL = (
    'https://raw.githubusercontent.com/nuuuwan/lk_census_2024/main/data/'
    'Population-Preliminary-Report/Population-by-religion/data.tsv'
)


def shares(data):
    total = data.get('TotalPopulation') or sum(
        data.get(religion, 0) for religion in RELIGIONS
    )
    if total == 0:
        return {religion: 0.0 for religion in RELIGIONS}
    return {religion: data.get(religion, 0) / total for religion in RELIGIONS}


def triangle(value):
    if value > 0:
        return ' 🟩'
    if value < 0:
        return ' 🟥'
    return ''


def _rounded_pp(value):
    rounded = round(value * 100, 1)
    if rounded == -0.0:
        rounded = 0.0
    return rounded


def _format_pp(value):
    rounded = _rounded_pp(value)
    if rounded == 0:
        return '0.0'
    return f'{rounded:+.1f}'


def _format_share(value):
    return f'{value:.1%}'


def _raw_rows(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(request) as response:
        text = response.read().decode('utf-8')
    return list(csv.DictReader(text.splitlines(), delimiter='\t'))


def _normalize_snapshot(rows, id_key, valid_ids):
    data = {}
    for row in rows:
        code = row.get(id_key)
        if code not in valid_ids:
            continue
        entry = {
            religion: int(float(row.get(raw_key, 0) or 0))
            for raw_key, religion in RAW_RELIGION_FIELD_MAP.items()
        }
        total = row.get('total_population') or row.get('total')
        entry['TotalPopulation'] = int(float(total or sum(entry.values())))
        data[code] = entry
    return data


def _snapshot_from_raw(entity_type, year):
    valid_ids = {ent.id for ent in Ent.list_from_type(entity_type)}
    if year == 2012:
        return _normalize_snapshot(
            _raw_rows(GIG_2012_RELIGION_URL),
            'entity_id',
            valid_ids,
        )
    if year == 2024:
        return _normalize_snapshot(
            _raw_rows(CENSUS_2024_RELIGION_URL),
            'region_id',
            valid_ids,
        )
    raise ValueError(f'Unsupported year: {year}')


@dataclass(frozen=True)
class RegionAnalysisConfig:
    analysis_dir: Path
    analysis_key: str
    analysis_heading: str
    image_alt: str
    region_singular: str
    region_plural: str
    region_level_label: str
    entity_type: object
    code_key: str
    name_key: str
    data_2012_path: Path
    data_2024_path: Path
    analysis_json_path: Path
    readme_path: Path
    chart_path: Path
    low_population_threshold: int = 1000
    label_top_n: int | None = None
    description_override: str | None = None
    readme_row_limit: int | None = None
    print_row_limit: int | None = None
    extra_text: str | None = None
    extra_row_data: object | None = None
    excluded_codes: frozenset[str] = field(default_factory=frozenset)
    extra_columns: tuple[tuple[str, str], ...] = field(default_factory=tuple)


def _label_description(config):
    if config.description_override:
        return config.description_override
    if config.label_top_n == 0:
        return (
            f'{config.region_plural} are shaded by **change in share of population (pp)** '
            'from **red (decline)** to **green (growth)**. '
            f'{config.region_singular} labels are omitted due to map density. '
            f'{config.region_plural} with religion population **< {config.low_population_threshold:,} (2024)** '
            'are shown in **grey**.'
        )
    if config.label_top_n is None:
        return (
            f'{config.region_singular} labels show the **{config.region_singular.lower()} name** '
            'and **change in share of population (pp)**. '
            f'{config.region_plural} are shaded by **change in share of population (pp)** '
            'from **red (decline)** to **green (growth)**. '
            f'{config.region_plural} with religion population **< {config.low_population_threshold:,} (2024)** '
            'are shown in **grey**.'
        )
    return (
        f'The **top {config.label_top_n} {config.region_plural.lower()} by absolute share change** '
        f'are labeled with the **{config.region_singular.lower()} name** and '
        '**change in share of population (pp)**. '
        f'{config.region_plural} are shaded by **change in share of population (pp)** '
        'from **red (decline)** to **green (growth)**. '
        f'{config.region_plural} with religion population **< {config.low_population_threshold:,} (2024)** '
        'are shown in **grey**.'
    )


def _region_geometries(entity_type, code_key, name_key):
    regions = []
    region_names = {}
    for ent in sorted(Ent.list_from_type(entity_type), key=lambda ent: ent.id):
        region_names[ent.id] = ent.name
        region_gdf = ent.geo().copy()
        region_gdf[code_key] = ent.id
        region_gdf[name_key] = ent.name
        regions.append(region_gdf[[code_key, name_key, 'geometry']])

    geometry = gpd.GeoDataFrame(
        pd.concat(regions, ignore_index=True),
        geometry='geometry',
        crs=regions[0].crs if regions else None,
    )
    return region_names, geometry


def _load_region_data(config):
    try:
        from lanka_data import Db

        db2012 = Db(f'/LK:{config.region_plural}/Religion/2012')
        db2024 = Db(f'/LK:{config.region_plural}/Religion/2024')
        config.data_2012_path.write_text(json.dumps(db2012, indent=2) + '\n')
        config.data_2024_path.write_text(json.dumps(db2024, indent=2) + '\n')
        return db2012, db2024
    except Exception:
        pass

    if config.data_2012_path.exists() and config.data_2024_path.exists():
        return (
            json.loads(config.data_2012_path.read_text()),
            json.loads(config.data_2024_path.read_text()),
        )

    db2012 = _snapshot_from_raw(config.entity_type, 2012)
    db2024 = _snapshot_from_raw(config.entity_type, 2024)
    config.data_2012_path.write_text(json.dumps(db2012, indent=2) + '\n')
    config.data_2024_path.write_text(json.dumps(db2024, indent=2) + '\n')
    return db2012, db2024


def _build_results(config, db2012, db2024, region_names):
    region_codes = sorted(
        code
        for code in (set(db2012) | set(db2024))
        if code not in config.excluded_codes
    )
    national2024 = {
        religion: sum(db2024.get(code, {}).get(religion, 0) for code in region_codes)
        for religion in RELIGIONS
    }

    results = {}
    for religion in RELIGIONS:
        rows = []
        for code in region_codes:
            region2012 = db2012.get(code, {})
            region2024 = db2024.get(code, {})
            v2012 = region2012.get(religion, 0)
            v2024 = region2024.get(religion, 0)
            change = v2024 - v2012
            pct_change = change / v2012 if v2012 else None
            share_2012 = shares(region2012)[religion]
            share_2024 = shares(region2024)[religion]
            share_change = share_2024 - share_2012
            annual_growth = (
                (v2024 / v2012) ** (1 / YEARS) - 1 if v2012 > 0 else None
            )
            row = {
                config.code_key: code,
                config.name_key: region_names.get(code, code),
                '2012': v2012,
                '2024': v2024,
                'change': change,
                'pct_change': round(pct_change, 6) if pct_change is not None else None,
                'proportion_2012': round(share_2012, 6),
                'proportion_2024': round(share_2024, 6),
                'proportion_change': round(share_change, 6),
                'annual_growth_rate': (
                    round(annual_growth, 6) if annual_growth is not None else None
                ),
                'proportion_national': (
                    round(v2024 / national2024[religion], 6)
                    if national2024[religion] > 0
                    else 0
                ),
            }
            if config.extra_row_data is not None:
                row.update(config.extra_row_data(code))
            rows.append(row)
        rows.sort(key=lambda row: row['proportion_change'], reverse=True)
        results[religion] = rows
    return results


def _print_results(config, results):
    for religion, rows in results.items():
        print(f'\n  {RELIGION_LABELS[religion]}')
        display_rows = rows
        if config.print_row_limit is not None:
            display_rows = rows[: config.print_row_limit]
        for row in display_rows:
            extras = ' '.join(
                f"{header}={row[field]}"
                for field, header in config.extra_columns
            )
            proportion_national = (
                f"{row['proportion_national']:.1%}"
                if row.get('proportion_national') is not None
                else ''
            )
            print(
                f"  {row[config.name_key]} {extras} %Natl={proportion_national} "
                f"2012={row['2012']:,} 2024={row['2024']:,} "
                f"Δ={row['change']:+,} share12={_format_share(row['proportion_2012'])} "
                f"share24={_format_share(row['proportion_2024'])} "
                f"Δpp={_format_pp(row['proportion_change'])}"
            )


def _write_readme(config, results):
    lines = [
        f'## {config.analysis_key}. {config.analysis_heading}',
        '',
        f'![{config.image_alt}](chart.png)',
        '',
        _label_description(config),
        '',
    ]

    if config.extra_text:
        lines.extend([config.extra_text, ''])

    for religion, rows in results.items():
        if not rows:
            continue

        fastest_growing = max(rows, key=lambda row: row['proportion_change'])
        fastest_declining = min(rows, key=lambda row: row['proportion_change'])
        largest_absolute = max(rows, key=lambda row: row['change'])
        display_rows = rows
        if config.readme_row_limit is not None:
            display_rows = rows[: config.readme_row_limit]

        headers = [config.region_singular]
        headers.extend(header for _, header in config.extra_columns)
        headers.extend(
            [
                '% Nationally',
                '2012',
                '2024',
                'Change',
                '% of Population (2012)',
                '% of Population (2024)',
                'Change in % of Population (pp)',
            ]
        )
        lines += [
            f"### {RELIGION_LABELS[religion]}",
            '',
            '| ' + ' | '.join(headers) + ' |',
            '|'
            + '|'.join(
                ['---'] + ['---'] * len(config.extra_columns) + ['---:'] * 7
            )
            + '|',
        ]
        for row in display_rows:
            proportion_national = (
                f"{row['proportion_national']:.1%}"
                if row.get('proportion_national') is not None
                else ''
            )
            row_cells = [f"{row[config.name_key]} `{row[config.code_key]}`"]
            row_cells.extend(str(row[field]) for field, _ in config.extra_columns)
            row_cells.extend(
                [
                    proportion_national,
                    f"{row['2012']:,}",
                    f"{row['2024']:,}",
                    f"{row['change']:+,}{triangle(row['change'])}",
                    _format_share(row['proportion_2012']),
                    _format_share(row['proportion_2024']),
                    (
                        f"{_format_pp(row['proportion_change'])}"
                        f"{triangle(_rounded_pp(row['proportion_change']))} pp"
                    ),
                ]
            )
            lines.append('| ' + ' | '.join(row_cells) + ' |')

        highlights = []
        if fastest_growing['proportion_change'] and fastest_growing['proportion_change'] > 0:
            highlights.append(
                f"**{fastest_growing[config.name_key]}** gained the most share at "
                f"**{_format_pp(fastest_growing['proportion_change'])}pp**."
            )
        if (
            fastest_declining['proportion_change']
            and fastest_declining['proportion_change'] < 0
        ):
            highlights.append(
                f"**{fastest_declining[config.name_key]}** saw the steepest share decline at "
                f"**{_format_pp(fastest_declining['proportion_change'])}pp**."
            )
        elif fastest_declining != fastest_growing:
            highlights.append(
                f"**{fastest_declining[config.name_key]}** had the smallest share gain at "
                f"**{_format_pp(fastest_declining['proportion_change'])}pp**."
            )
        if largest_absolute != fastest_growing and largest_absolute['change'] > 0:
            highlights.append(
                f"**{largest_absolute[config.name_key]}** had the largest absolute increase "
                f"(**{largest_absolute['change']:+,}**)."
            )
        if config.readme_row_limit is not None and len(rows) > len(display_rows):
            lines.extend(
                [
                    '',
                    f'*Showing the first {len(display_rows)} {config.region_plural.lower()} sorted by share change. Full results are in `{config.analysis_json_path.name}`.*',
                ]
            )

        if highlights:
            lines += ['', '*' + ' '.join(highlights) + '*']
        lines.append('')

    content = '\n'.join(lines).rstrip()
    config.readme_path.write_text(content + '\n')
    return content


def _write_chart(config, results, region_map_gdf):
    max_abs_change = max(
        abs(row['proportion_change'])
        for rows in results.values()
        for row in rows
        if row['proportion_change'] is not None
    )
    norm = TwoSlopeNorm(vmin=-max_abs_change, vcenter=0, vmax=max_abs_change)
    cmap = plt.get_cmap('RdYlGn')
    fig, axes = plt.subplots(2, 3, figsize=(14, 16), constrained_layout=True)

    for ax, religion in zip(axes.flat, RELIGIONS):
        map_data = pd.DataFrame(results[religion])[
            [
                config.code_key,
                '2012',
                '2024',
                'proportion_2012',
                'proportion_2024',
                'proportion_change',
            ]
        ]
        plot_gdf = region_map_gdf.merge(map_data, on=config.code_key, how='left')
        plot_gdf['is_low_population'] = (
            plot_gdf['2024'].fillna(0) < config.low_population_threshold
        )
        plot_gdf['plot_proportion_change'] = plot_gdf['proportion_change'].where(
            ~plot_gdf['is_low_population'],
            other=pd.NA,
        )
        plot_gdf.plot(
            column='plot_proportion_change',
            cmap=cmap,
            norm=norm,
            linewidth=0.4,
            edgecolor='white',
            ax=ax,
            missing_kwds={'color': '#f0f0f0'},
        )
        low_population_gdf = plot_gdf[plot_gdf['is_low_population']]
        if not low_population_gdf.empty:
            low_population_gdf.plot(
                color='#bdbdbd',
                linewidth=0.4,
                edgecolor='white',
                ax=ax,
            )
        plot_gdf.boundary.plot(ax=ax, color='#666666', linewidth=0.25)

        if config.label_top_n != 0:
            label_points = plot_gdf.representative_point()
            label_codes = None
            if config.label_top_n is not None:
                ranked_rows = sorted(
                    (
                        row
                        for row in results[religion]
                        if row['proportion_change'] is not None
                    ),
                    key=lambda row: abs(row['proportion_change']),
                    reverse=True,
                )
                label_codes = {
                    row[config.code_key] for row in ranked_rows[: config.label_top_n]
                }
            for _, row in plot_gdf.iterrows():
                if label_codes is not None and row[config.code_key] not in label_codes:
                    continue
                point = label_points.loc[row.name]
                proportion_change = row['proportion_change']
                label = (
                    f"{row[config.name_key]}\n{_format_pp(proportion_change)} pp"
                    if pd.notna(proportion_change)
                    else f"{row[config.name_key]}\nN/A"
                )
                ax.text(
                    point.x,
                    point.y,
                    label,
                    ha='center',
                    va='center',
                    fontsize=5.8 if config.label_top_n is None else 4.0,
                    color='#1a1a1a',
                    linespacing=1.1,
                    bbox={
                        'boxstyle': 'round,pad=0.2',
                        'facecolor': 'white',
                        'edgecolor': 'none',
                        'alpha': 1.0,
                    },
                )

        ax.set_title(RELIGION_LABELS[religion], fontsize=13, pad=10)
        ax.set_axis_off()

    colorbar = fig.colorbar(
        ScalarMappable(norm=norm, cmap=cmap),
        ax=axes,
        fraction=0.03,
        pad=0.02,
    )
    colorbar.ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    colorbar.set_label('Change in % of population (pp, 2012→2024)')
    fig.text(
        0.5,
        0.02,
        f'Grey {config.region_plural.lower()}: religion population < {config.low_population_threshold:,} in 2024',
        ha='center',
        va='center',
        fontsize=10,
        color='#444444',
    )
    fig.suptitle(
        f'Sri Lanka {config.region_level_label} religion share change, 2012→2024',
        fontsize=16,
        y=1.02,
    )
    fig.savefig(config.chart_path, dpi=300, bbox_inches='tight')
    plt.close(fig)


def run_religion_by_region(config):
    print(f'=== {config.analysis_key}) {config.analysis_heading} ===')
    db2012, db2024 = _load_region_data(config)
    region_names, region_map_gdf = _region_geometries(
        config.entity_type,
        config.code_key,
        config.name_key,
    )
    results = _build_results(config, db2012, db2024, region_names)
    config.analysis_json_path.write_text(json.dumps(results, indent=2) + '\n')
    _write_chart(config, results, region_map_gdf)
    _print_results(config, results)
    return _write_readme(config, results)
