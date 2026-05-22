import json
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.cm import ScalarMappable
from matplotlib.colors import TwoSlopeNorm
from matplotlib.ticker import PercentFormatter

ANALYSIS_DIR = Path(__file__).resolve().parent
SRC_DIR = ANALYSIS_DIR.parents[1] / 'src'
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from analyses.proportion_change_common import shares, triangle

try:
    from gig import EntType, Ent
except ImportError:
    EntType = None
    Ent = None

try:
    from lanka_data import Db
except ImportError:
    Db = None

README_PATH = ANALYSIS_DIR / 'README.md'
CHART_PATH = ANALYSIS_DIR / 'chart.png'
DATA_2012_PATH = ANALYSIS_DIR / 'religion_by_country_2012.json'
DATA_2024_PATH = ANALYSIS_DIR / 'religion_by_country_2024.json'
ANALYSIS_JSON_PATH = ANALYSIS_DIR / 'religion_by_country_analysis.json'
A1_DIR = ANALYSIS_DIR.parents[0] / 'a1_national_totals'
TABLE_MIN_ABS_PP = 1.0
COUNTRY_CODE = 'LK'
COUNTRY_NAME = 'Sri Lanka'
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


def run():
    print('=== A8) Religion by Country: Key Trends ===')
    db2012, db2024 = _load_country_data()
    results = _build_results(db2012, db2024)
    ANALYSIS_JSON_PATH.write_text(json.dumps(results, indent=2) + '\n')
    _write_chart(results)
    return _write_readme(results)


def _load_country_data():
    if Db is not None:
        data_2012 = Db('/LK/Religion/2012')
        data_2024 = Db('/LK/Religion/2024')
    else:
        data_2012 = json.loads((A1_DIR / 'religion_2012.json').read_text())
        data_2024 = json.loads((A1_DIR / 'religion_2024.json').read_text())

    db2012 = {COUNTRY_CODE: data_2012}
    db2024 = {COUNTRY_CODE: data_2024}
    DATA_2012_PATH.write_text(json.dumps(db2012, indent=2) + '\n')
    DATA_2024_PATH.write_text(json.dumps(db2024, indent=2) + '\n')
    return db2012, db2024


def _build_results(db2012, db2024):
    country2012 = db2012[COUNTRY_CODE]
    country2024 = db2024[COUNTRY_CODE]
    shares_2012 = shares(country2012)
    shares_2024 = shares(country2024)

    results = {}
    for religion in RELIGIONS:
        v2012 = country2012.get(religion, 0)
        v2024 = country2024.get(religion, 0)
        row = {
            'country_code': COUNTRY_CODE,
            'country': COUNTRY_NAME,
            '2012': v2012,
            '2024': v2024,
            'change': v2024 - v2012,
            'proportion_2012': round(shares_2012[religion], 6),
            'proportion_2024': round(shares_2024[religion], 6),
            'proportion_change': round(shares_2024[religion] - shares_2012[religion], 6),
            'proportion_national': 1.0,
        }
        results[religion] = [row]
    return results


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


def _get_country_geometry():
    if Ent is None or EntType is None:
        return None
    provinces = Ent.list_from_type(EntType.PROVINCE)
    gdfs = []
    for prov in provinces:
        gdf = prov.geo().copy()
        gdfs.append(gdf[['geometry']])
    combined = gpd.GeoDataFrame(
        pd.concat(gdfs, ignore_index=True),
        geometry='geometry',
        crs=gdfs[0].crs,
    )
    country_gdf = combined.dissolve().reset_index(drop=True)
    country_gdf[COUNTRY_CODE] = COUNTRY_CODE
    return country_gdf


def _write_chart(results):
    country_gdf = _get_country_geometry()

    max_abs_change = max(
        abs(row['proportion_change'])
        for rows in results.values()
        for row in rows
        if row['proportion_change'] is not None
    )
    if max_abs_change == 0:
        max_abs_change = 0.01
    norm = TwoSlopeNorm(vmin=-max_abs_change, vcenter=0, vmax=max_abs_change)
    cmap = plt.get_cmap('RdYlGn')

    fig, axes = plt.subplots(2, 3, figsize=(14, 16), constrained_layout=True)

    for ax, religion in zip(axes.flat, RELIGIONS):
        proportion_change = results[religion][0]['proportion_change']

        if country_gdf is not None:
            plot_gdf = country_gdf.copy()
            plot_gdf['proportion_change'] = proportion_change
            plot_gdf.plot(
                column='proportion_change',
                cmap=cmap,
                norm=norm,
                linewidth=0.4,
                edgecolor='white',
                ax=ax,
            )
            plot_gdf.boundary.plot(ax=ax, color='#666666', linewidth=0.25)
            centroid = plot_gdf.geometry.to_crs(epsg=3857).centroid.to_crs(plot_gdf.crs).iloc[0]
            ax.text(
                centroid.x,
                centroid.y,
                f'{COUNTRY_NAME}\n{_format_pp(proportion_change)} pp',
                ha='center',
                va='center',
                fontsize=8,
                color='#1a1a1a',
                linespacing=1.2,
                bbox={
                    'boxstyle': 'round,pad=0.3',
                    'facecolor': 'white',
                    'edgecolor': 'none',
                    'alpha': 1.0,
                },
            )
        else:
            ax.text(
                0.5,
                0.5,
                f'{COUNTRY_NAME}\n{_format_pp(proportion_change)} pp',
                ha='center',
                va='center',
                fontsize=12,
                transform=ax.transAxes,
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
    fig.suptitle(
        'Sri Lanka country-level religion share change, 2012→2024',
        fontsize=16,
        y=1.02,
    )
    fig.savefig(CHART_PATH, dpi=300, bbox_inches='tight')
    plt.close(fig)


def _write_readme(results):
    lines = [
        '## A8. Religion by Country: Key Trends',
        '',
        '![A8 country change maps](chart.png)',
        '',
        'Sri Lanka is shaded by **change in share of population (pp)** '
        'from **red (decline)** to **green (growth)**.',
        '',
        f'Tables list only rows where absolute share change is **> {TABLE_MIN_ABS_PP:.1f}pp**.',
        '',
    ]

    for religion in RELIGIONS:
        rows = results[religion]
        display_rows = [
            row
            for row in rows
            if abs(_rounded_pp(row['proportion_change'])) > TABLE_MIN_ABS_PP
        ]
        lines += [
            f'### {RELIGION_LABELS[religion]}',
            '',
            '| Country | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |',
            '|---|---:|---:|---:|---:|---:|---:|---:|',
        ]
        if not display_rows:
            lines.extend(['', '*No regions exceed the table share-change threshold.*', ''])
            continue

        for row in display_rows:
            lines.append(
                f"| {row['country']} `{row['country_code']}` | {row['proportion_national']:.1%} | {row['2012']:,} | {row['2024']:,} | {row['change']:+,}{triangle(row['change'])} | {row['proportion_2012']:.1%} | {row['proportion_2024']:.1%} | {_format_pp(row['proportion_change'])}pp{triangle(_rounded_pp(row['proportion_change']))} |"
            )

        row = display_rows[0]
        if row['proportion_change'] > 0:
            lines += ['', f"* **{COUNTRY_NAME}** gained share at **{_format_pp(row['proportion_change'])}pp**.*", '']
        elif row['proportion_change'] < 0:
            lines += ['', f"* **{COUNTRY_NAME}** saw a share decline at **{_format_pp(row['proportion_change'])}pp**.*", '']
        else:
            lines += ['', f"* **{COUNTRY_NAME}** had no share change (**{_format_pp(row['proportion_change'])}pp**).*", '']

    content = '\n'.join(lines).rstrip()
    README_PATH.write_text(content + '\n')
    return content
