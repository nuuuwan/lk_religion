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

from analyses.proportion_change_common import triangle

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
            v2012 = db2012.get(code, {}).get(religion, 0)
            v2024 = db2024.get(code, {}).get(religion, 0)
            change = v2024 - v2012
            pct_change = change / v2012 if v2012 else None
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

        rows.sort(key=lambda row: row['pct_change'], reverse=True)

        results[religion] = rows

        print(f'\n  {RELIGION_LABELS[religion]}')
        print(
            f"  {'District':<16} {'2012':>10} {'2024':>10} {'Change':>10} {'% Change':>10} {'% of Natl':>10}"
        )
        print('  ' + '-' * 72)
        for row in rows:
            pct_change = (
                f"{row['pct_change']:+.1%}"
                if row['pct_change'] is not None
                else 'N/A'
            )
            proportion_national = (
                f"{row['proportion_national']:.1%}"
                if row.get('proportion_national') is not None
                else ''
            )
            print(
                f"  {row['district']:<16} {row['2012']:>10,} {row['2024']:>10,} {row['change']:>+10,} {pct_change:>10} {proportion_national:>10}"
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
        'District-level **% change in population** for each religion between 2012 and 2024. Districts are shaded from **red (decline)** to **green (growth)**.',
        '',
    ]

    for religion, rows in results.items():
        if not rows:
            continue

        fastest_growing = max(rows, key=lambda row: row['pct_change'])
        fastest_declining = min(rows, key=lambda row: row['pct_change'])
        largest_absolute = max(rows, key=lambda row: row['change'])

        lines += [
            f"### {RELIGION_LABELS[religion]}",
            '',
            '| District | 2012 | 2024 | Change | % Change | % of Natl |',
            '|---|---:|---:|---:|---:|---:|',
        ]
        for row in rows:
            pct_change = (
                f"{row['pct_change']:+.1%}"
                if row['pct_change'] is not None
                else 'N/A'
            )
            proportion_national = (
                f"{row['proportion_national']:.1%}"
                if row.get('proportion_national') is not None
                else ''
            )
            lines.append(
                f"| {row['district']} | {row['2012']:,} | {row['2024']:,} | {triangle(row['change'])}{row['change']:+,} | {triangle(row['pct_change'] or 0)}{pct_change} | {proportion_national} |"
            )

        highlights = []
        if fastest_growing['pct_change'] and fastest_growing['pct_change'] > 0:
            highlights.append(
                f"**{fastest_growing['district']}** grew fastest at **{fastest_growing['pct_change']:+.1%}**."
            )
        if fastest_declining['pct_change'] and fastest_declining['pct_change'] < 0:
            highlights.append(
                f"**{fastest_declining['district']}** saw the steepest decline at **{fastest_declining['pct_change']:+.1%}**."
            )
        elif fastest_declining != fastest_growing:
            highlights.append(
                f"**{fastest_declining['district']}** had the slowest growth at **{fastest_declining['pct_change']:+.1%}**."
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
        abs(row['pct_change'])
        for rows in results.values()
        for row in rows
        if row['pct_change'] is not None
    )
    norm = TwoSlopeNorm(vmin=-max_abs_change, vcenter=0, vmax=max_abs_change)
    cmap = plt.get_cmap('RdYlGn')

    fig, axes = plt.subplots(2, 3, figsize=(14, 16), constrained_layout=True)

    for ax, religion in zip(axes.flat, RELIGIONS):
        map_data = pd.DataFrame(results[religion])[
            ['district_code', 'pct_change']
        ]
        plot_gdf = district_map_gdf.merge(map_data, on='district_code', how='left')
        plot_gdf.plot(
            column='pct_change',
            cmap=cmap,
            norm=norm,
            linewidth=0.6,
            edgecolor='white',
            ax=ax,
            missing_kwds={'color': '#f0f0f0'},
        )
        plot_gdf.boundary.plot(ax=ax, color='#666666', linewidth=0.35)
        ax.set_title(RELIGION_LABELS[religion], fontsize=13, pad=10)
        ax.set_axis_off()

    colorbar = fig.colorbar(
        ScalarMappable(norm=norm, cmap=cmap),
        ax=axes,
        fraction=0.03,
        pad=0.02,
    )
    colorbar.ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    colorbar.set_label('% change in population (2012→2024)')
    fig.suptitle(
        'Sri Lanka district-level religion population change, 2012→2024',
        fontsize=16,
        y=0.98,
    )
    fig.savefig(CHART_PATH, dpi=150, bbox_inches='tight')
    plt.close(fig)
