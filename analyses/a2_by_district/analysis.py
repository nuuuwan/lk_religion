import json
from functools import lru_cache
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from gig import Ent, EntType
from matplotlib.cm import ScalarMappable
from matplotlib.colors import TwoSlopeNorm
from matplotlib.ticker import PercentFormatter

from analyses.proportion_change_common import shares, triangle

ANALYSIS_DIR = Path(__file__).resolve().parent
README_PATH = ANALYSIS_DIR / 'README.md'
CHART_PATH = ANALYSIS_DIR / 'chart.png'
DATA_2012_PATH = ANALYSIS_DIR / 'religion_by_district_2012.json'
DATA_2024_PATH = ANALYSIS_DIR / 'religion_by_district_2024.json'

RELIGIONS = [
    'Buddhist',
    'Hindu',
    'Islam',
    'RomanCatholic',
    'OtherChristian',
    'Other',
]
YEARS = 2024 - 2012
RELIGION_LABELS = {
    'Buddhist': 'Buddhist',
    'Hindu': 'Hindu',
    'Islam': 'Islam',
    'RomanCatholic': 'Roman Catholic',
    'OtherChristian': 'Other Christian',
    'Other': 'Other',
}
LOW_POPULATION_THRESHOLD = 1000


def _format_share(value):
    return f'{value:.1%}'


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


def run():
    print('=== 2) By-district religion change maps ===')

    db2012, db2024 = _load_district_data()
    district_names, district_map_gdf = _district_geometries()
    district_codes = sorted(set(db2012) | set(db2024))
    national2024 = {
        religion: sum(db2024.get(code, {}).get(religion, 0) for code in district_codes)
        for religion in RELIGIONS
    }

    results = {}
    for religion in RELIGIONS:
        rows = []
        for code in district_codes:
            district2012 = db2012.get(code, {})
            district2024 = db2024.get(code, {})
            v2012 = db2012.get(code, {}).get(religion, 0)
            v2024 = db2024.get(code, {}).get(religion, 0)
            change = v2024 - v2012
            pct_change = change / v2012 if v2012 else None
            share_2012 = shares(district2012)[religion]
            share_2024 = shares(district2024)[religion]
            share_change = share_2024 - share_2012
            annual_growth = (
                (v2024 / v2012) ** (1 / YEARS) - 1 if v2012 > 0 else None
            )
            rows.append(
                {
                    'district_code': code,
                    'district': district_names.get(code, code),
                    '2012': v2012,
                    '2024': v2024,
                    'change': change,
                    'pct_change': round(pct_change, 6) if pct_change is not None else None,
                    'proportion_2012': round(share_2012, 6),
                    'proportion_2024': round(share_2024, 6),
                    'proportion_change': round(share_change, 6),
                    'annual_growth_rate': (
                        round(annual_growth, 6)
                        if annual_growth is not None
                        else None
                    ),
                    'proportion_national': (
                        round(v2024 / national2024[religion], 6)
                        if national2024[religion] > 0
                        else 0
                    ),
                }
            )

        rows.sort(key=lambda row: row['proportion_change'], reverse=True)

        results[religion] = rows

        print(f'\n  {RELIGION_LABELS[religion]}')
        print(
            f"  {'District':<16} {'% Natl':>8} {'2012':>10} {'2024':>10} {'Change':>10} {'% Pop 12':>9} {'% Pop 24':>9} {'Δpp':>7}"
        )
        print('  ' + '-' * 96)
        for row in rows:
            proportion_national = (
                f"{row['proportion_national']:.1%}"
                if row.get('proportion_national') is not None
                else ''
            )
            print(
                f"  {row['district']:<16} {proportion_national:>8} {row['2012']:>10,} {row['2024']:>10,} {row['change']:>+10,} {_format_share(row['proportion_2012']):>8} {_format_share(row['proportion_2024']):>8} {_format_pp(row['proportion_change']):>7}"
            )

    with open(ANALYSIS_DIR / 'religion_by_district_analysis.json', 'w') as f:
        json.dump(results, f, indent=2)

    _write_chart(results, district_map_gdf)

    return _write_readme(_readme_section(results))


def _write_readme(content):
    README_PATH.write_text(content + '\n')
    return content


def _readme_section(results):
    lines = [
        '## A2. Religion by District: Key Trends',
        '',
        '![A2 district change maps](chart.png)',
        '',
        f'District labels show the religion share of each district population in **2012 → 2024**. Districts are shaded by **change in share of population (pp)** from **red (decline)** to **green (growth)**. Districts with religion population **< {LOW_POPULATION_THRESHOLD:,} (2024)** are shown in **grey**.',
        '',
    ]

    for religion, rows in results.items():
        if not rows:
            continue

        fastest_growing = max(rows, key=lambda row: row['proportion_change'])
        fastest_declining = min(rows, key=lambda row: row['proportion_change'])
        largest_absolute = max(rows, key=lambda row: row['change'])

        lines += [
            f"### {RELIGION_LABELS[religion]}",
            '',
            '| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |',
            '|---|---:|---:|---:|---:|---:|---:|---:|',
        ]
        for row in rows:
            proportion_national = (
                f"{row['proportion_national']:.1%}"
                if row.get('proportion_national') is not None
                else ''
            )
            lines.append(
                f"| {row['district']} | {proportion_national} | {row['2012']:,} | {row['2024']:,} | {row['change']:+,}{triangle(row['change'])} | {_format_share(row['proportion_2012'])} | {_format_share(row['proportion_2024'])} | {_format_pp(row['proportion_change'])}pp{triangle(_rounded_pp(row['proportion_change']))} |"
            )

        highlights = []
        if fastest_growing['proportion_change'] and fastest_growing['proportion_change'] > 0:
            highlights.append(
                f"**{fastest_growing['district']}** gained the most share at **{_format_pp(fastest_growing['proportion_change'])}pp**."
            )
        if (
            fastest_declining['proportion_change']
            and fastest_declining['proportion_change'] < 0
        ):
            highlights.append(
                f"**{fastest_declining['district']}** saw the steepest share decline at **{_format_pp(fastest_declining['proportion_change'])}pp**."
            )
        elif fastest_declining != fastest_growing:
            highlights.append(
                f"**{fastest_declining['district']}** had the smallest share gain at **{_format_pp(fastest_declining['proportion_change'])}pp**."
            )
        if largest_absolute != fastest_growing and largest_absolute['change'] > 0:
            highlights.append(
                f"**{largest_absolute['district']}** had the largest absolute increase (**{largest_absolute['change']:+,}**)."
            )

        if highlights:
            lines += ['', '*' + ' '.join(highlights) + '*']

        lines.append('')

    return '\n'.join(lines).rstrip()

@lru_cache(maxsize=1)
def _district_geometries():
    districts = []
    district_names = {}
    for ent in sorted(Ent.list_from_type(EntType.DISTRICT), key=lambda ent: ent.id):
        district_names[ent.id] = ent.name
        district_gdf = ent.geo().copy()
        district_gdf['district_code'] = ent.id
        district_gdf['district'] = ent.name
        districts.append(district_gdf[['district_code', 'district', 'geometry']])

    geometry = gpd.GeoDataFrame(
        pd.concat(districts, ignore_index=True),
        geometry='geometry',
        crs=districts[0].crs if districts else None,
    )
    return district_names, geometry


def _load_district_data():
    try:
        from lanka_data import Db

        db2012 = Db('/LK:Districts/Religion/2012')
        db2024 = Db('/LK:Districts/Religion/2024')
        DATA_2012_PATH.write_text(json.dumps(db2012, indent=2) + '\n')
        DATA_2024_PATH.write_text(json.dumps(db2024, indent=2) + '\n')
        return db2012, db2024
    except Exception:
        return (
            json.loads(DATA_2012_PATH.read_text()),
            json.loads(DATA_2024_PATH.read_text()),
        )


def _write_chart(results, district_map_gdf):
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
                'district_code',
                '2012',
                '2024',
                'proportion_2012',
                'proportion_2024',
                'proportion_change',
            ]
        ]
        plot_gdf = district_map_gdf.merge(map_data, on='district_code', how='left')
        plot_gdf['is_low_population'] = plot_gdf['2024'].fillna(0) < LOW_POPULATION_THRESHOLD
        plot_gdf['plot_proportion_change'] = plot_gdf['proportion_change'].where(
            ~plot_gdf['is_low_population'],
            other=pd.NA,
        )
        plot_gdf.plot(
            column='plot_proportion_change',
            cmap=cmap,
            norm=norm,
            linewidth=0.6,
            edgecolor='white',
            ax=ax,
            missing_kwds={'color': '#f0f0f0'},
        )
        low_population_gdf = plot_gdf[plot_gdf['is_low_population']]
        if not low_population_gdf.empty:
            low_population_gdf.plot(
                color='#bdbdbd',
                linewidth=0.6,
                edgecolor='white',
                ax=ax,
            )
        plot_gdf.boundary.plot(ax=ax, color='#666666', linewidth=0.35)
        label_points = plot_gdf.representative_point()
        for _, row in plot_gdf.iterrows():
            point = label_points.loc[row.name]
            proportion_2012 = row['proportion_2012']
            proportion_2024 = row['proportion_2024']
            label = (
                f'{_format_share(proportion_2012)}→{_format_share(proportion_2024)}'
                if pd.notna(proportion_2012) and pd.notna(proportion_2024)
                else 'N/A'
            )
            ax.text(
                point.x,
                point.y,
                label,
                ha='center',
                va='center',
                fontsize=6.5,
                color='#1a1a1a',
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
        f'Grey districts: religion population < {LOW_POPULATION_THRESHOLD:,} in 2024',
        ha='center',
        va='center',
        fontsize=10,
        color='#444444',
    )
    fig.suptitle(
        'Sri Lanka district-level religion share change, 2012→2024',
        fontsize=16,
        y=1.02,
    )
    fig.savefig(CHART_PATH, dpi=150, bbox_inches='tight')
    plt.close(fig)
