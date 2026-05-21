import json
from functools import lru_cache
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from gig import Ent, EntType

from analyses.proportion_change_common import (
    RELIGIONS,
    shares,
    triangle,
)

ANALYSIS_DIR = Path(__file__).resolve().parent
README_PATH = ANALYSIS_DIR / 'README.md'
CHART_PATH = ANALYSIS_DIR / 'chart.png'
A2_ANALYSIS_DIR = Path(__file__).resolve().parents[1] / 'a2_by_district'
A2_DATA_2012_PATH = A2_ANALYSIS_DIR / 'religion_by_district_2012.json'
A2_DATA_2024_PATH = A2_ANALYSIS_DIR / 'religion_by_district_2024.json'
MIN_CHANGE_ABS = 0.01
RELIGION_LABELS = {
    'Buddhist': 'Buddhist',
    'Hindu': 'Hindu',
    'Islam': 'Islam',
    'RomanCatholic': 'Roman Catholic',
    'OtherChristian': 'Other Christian',
    'Other': 'Other',
}


def run():
    print('=== 3) Largest change in religious proportion ===')

    db_dist_2012, db_dist_2024 = _load_district_data()
    district_names, district_map_gdf = _district_geometries()

    district_rows = []
    for code in db_dist_2012:
        if code not in db_dist_2024:
            continue
        shares_2012 = shares(db_dist_2012[code])
        shares_2024 = shares(db_dist_2024[code])
        max_religion = max(
            RELIGIONS,
            key=lambda religion: abs(
                shares_2024[religion] - shares_2012[religion]
            ),
        )
        change = shares_2024[max_religion] - shares_2012[max_religion]
        if abs(change) <= MIN_CHANGE_ABS:
            continue
        district_rows.append(
            {
                'district_code': code,
                'district': district_names.get(code, code),
                'religion': max_religion,
                'proportion_2012': round(shares_2012[max_religion], 6),
                'proportion_2024': round(shares_2024[max_religion], 6),
                'change': round(change, 6),
            }
        )
    district_rows.sort(key=lambda row: abs(row['change']), reverse=True)

    with open(ANALYSIS_DIR / 'proportion_change_analysis.json', 'w') as f:
        json.dump({'by_district': district_rows}, f, indent=2)

    _write_chart(district_rows, district_map_gdf)

    print('\n  By District:')
    print(
        f"  {'District':<16} {'Religion':<16} {'2012':>8} {'2024':>8} {'Change':>10}"
    )
    print('  ' + '-' * 62)
    for row in district_rows:
        print(
            f"  {row['district']:<16} {row['religion']:<16} {row['proportion_2012']:>8.1%} {row['proportion_2024']:>8.1%} {row['change'] * 100:>+9.1f}pp"
        )

    return _write_readme(_readme_section(district_rows))


def _write_readme(content):
    README_PATH.write_text(content + '\n')
    return content


def _readme_section(district_rows):
    lines = [
        '## A3. Largest Change in Religious Proportion',
        '',
        '![A3 increase/decrease maps](chart.png)',
        '',
        f'For each district, the religion whose share of the local population changed most between 2012 and 2024, showing only rows with absolute change > {MIN_CHANGE_ABS:.0%}. Largest increases and largest decreases are shown on separate maps.',
        '',
        '### By District',
        '',
        '| District | Religion | Share 2012 | Share 2024 | Change (pp) |',
        '|---|---|---:|---:|---:|',
    ]
    for row in district_rows:
        lines.append(
            f"| {row['district']} | {row['religion']} | {row['proportion_2012']:.1%} | {row['proportion_2024']:.1%} | {row['change'] * 100:+.1f}pp{triangle(row['change'])} |"
        )

    return '\n'.join(lines)


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

        return Db('/LK:Districts/Religion/2012'), Db('/LK:Districts/Religion/2024')
    except Exception:
        return (
            json.loads(A2_DATA_2012_PATH.read_text()),
            json.loads(A2_DATA_2024_PATH.read_text()),
        )


def _write_chart(district_rows, district_map_gdf):
    plot_df = pd.DataFrame(district_rows)
    plot_gdf = district_map_gdf.merge(plot_df, on='district_code', how='left')
    fig, axes = plt.subplots(1, 2, figsize=(13, 7), constrained_layout=True)

    map_specs = [
        ('Largest increases', plot_gdf['change'] > 0, 'Greens'),
        ('Largest decreases', plot_gdf['change'] < 0, 'Reds'),
    ]
    for ax, (title, mask, cmap) in zip(axes, map_specs):
        district_map_gdf.plot(
            ax=ax,
            color='#f2f2f2',
            edgecolor='white',
            linewidth=0.6,
        )
        subset = plot_gdf[mask].copy()
        if not subset.empty:
            subset['change_pp_abs'] = subset['change'].abs() * 100
            subset.plot(
                ax=ax,
                column='change_pp_abs',
                cmap=cmap,
                edgecolor='white',
                linewidth=0.6,
            )
            label_points = subset.representative_point()
            for _, row in subset.iterrows():
                point = label_points.loc[row.name]
                ax.text(
                    point.x,
                    point.y,
                    f"{RELIGION_LABELS[row['religion']]}\n{row['change'] * 100:+.1f}pp",
                    ha='center',
                    va='center',
                    fontsize=6.5,
                    color='#1a1a1a',
                    bbox={
                        'boxstyle': 'round,pad=0.2',
                        'facecolor': 'white',
                        'alpha': 0.75,
                        'edgecolor': 'none',
                    },
                )
        else:
            ax.text(0.5, 0.5, 'No districts to show', ha='center', va='center')
        district_map_gdf.boundary.plot(ax=ax, color='#666666', linewidth=0.35)
        ax.set_title(title)
        ax.set_axis_off()

    fig.suptitle('Largest district-level religion share changes, 2012→2024', fontsize=15)
    fig.savefig(CHART_PATH, dpi=150, bbox_inches='tight')
    plt.close(fig)
