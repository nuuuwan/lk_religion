import json
from pathlib import Path

import matplotlib.pyplot as plt
from lanka_data import Db, RegionNames

from analyses.proportion_change_common import RELIGION_COLORS, triangle

ANALYSIS_DIR = Path(__file__).resolve().parent
README_PATH = ANALYSIS_DIR / 'README.md'
CHART_PATH = ANALYSIS_DIR / 'chart.png'

RELIGIONS = [
    'Buddhist',
    'Hindu',
    'Islam',
    'RomanCatholic',
    'OtherChristian',
    'Other',
]
YEARS = 2024 - 2012
SIGNIFICANT_THRESHOLD = 0.01  # 1% of national total
MIN_ABSOLUTE = 1000  # minimum absolute count


def run():
    print('=== 2) By-district analysis per religion ===')

    db2012 = Db('/LK:Districts/Religion/2012')
    db2024 = Db('/LK:Districts/Religion/2024')
    national2024 = Db('/LK/Religion/2024')

    with open(ANALYSIS_DIR / 'religion_by_district_2012.json', 'w') as f:
        json.dump(db2012, f, indent=2)
    with open(ANALYSIS_DIR / 'religion_by_district_2024.json', 'w') as f:
        json.dump(db2024, f, indent=2)

    region_names = RegionNames()

    results = {}
    for religion in RELIGIONS:
        threshold = national2024[religion] * SIGNIFICANT_THRESHOLD

        rows = []
        other_2012, other_2024 = 0, 0
        for code in db2012:
            v2012 = db2012[code].get(religion, 0)
            v2024 = db2024[code].get(religion, 0)
            if (
                max(v2012, v2024) < threshold
                or max(v2012, v2024) < MIN_ABSOLUTE
            ):
                other_2012 += v2012
                other_2024 += v2024
                continue
            change = v2024 - v2012
            annual_growth = (
                (v2024 / v2012) ** (1 / YEARS) - 1 if v2012 > 0 else None
            )
            rows.append(
                {
                    'district_code': code,
                    'district': region_names.name_for(code),
                    '2012': v2012,
                    '2024': v2024,
                    'change': change,
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

        rows.sort(
            key=lambda row: (
                row['annual_growth_rate'] is not None,
                row['annual_growth_rate']
                if row['annual_growth_rate'] is not None
                else float('-inf'),
            ),
            reverse=True,
        )

        if other_2012 or other_2024:
            other_change = other_2024 - other_2012
            other_growth = (
                (other_2024 / other_2012) ** (1 / YEARS) - 1
                if other_2012 > 0
                else None
            )
            rows.append(
                {
                    'district_code': None,
                    'district': 'Other (<1% or <1,000)',
                    '2012': other_2012,
                    '2024': other_2024,
                    'change': other_change,
                    'annual_growth_rate': (
                        round(other_growth, 6)
                        if other_growth is not None
                        else None
                    ),
                }
            )

        results[religion] = rows

        print(
            f"\n  {religion} (threshold ≥ {threshold:,.0f} and ≥ {MIN_ABSOLUTE:,})"
        )
        print(
            f"  {'District':<16} {'2012':>10} {'2024':>10} {'Change':>10} {'Ann. Growth':>12} {'% of Natl':>10}"
        )
        print('  ' + '-' * 72)
        for row in rows:
            annual_growth = (
                f"{row['annual_growth_rate']:+.2%}"
                if row['annual_growth_rate'] is not None
                else 'N/A'
            )
            proportion_national = (
                f"{row['proportion_national']:.1%}"
                if row.get('proportion_national') is not None
                else ''
            )
            print(
                f"  {row['district']:<16} {row['2012']:>10,} {row['2024']:>10,} {row['change']:>+10,} {annual_growth:>12} {proportion_national:>10}"
            )

    with open(ANALYSIS_DIR / 'religion_by_district_analysis.json', 'w') as f:
        json.dump(results, f, indent=2)

    _write_chart(results)

    return _write_readme(_readme_section(results))


def _write_readme(content):
    README_PATH.write_text(content + '\n')
    return content


def _readme_section(results):
    lines = [
        '## A2. Religion by District: Key Trends',
        '',
        '![A2 representative chart](chart.png)',
        '',
    ]

    for religion, rows in results.items():
        if not rows:
            continue

        significant_rows = [row for row in rows if row['district_code'] is not None]
        other_row = next(
            (row for row in rows if row['district_code'] is None), None
        )

        if not significant_rows:
            continue

        fastest_growing = significant_rows[0]
        fastest_declining = significant_rows[-1]
        largest_absolute = max(significant_rows, key=lambda row: row['change'])

        lines += [
            f'### {religion}',
            '',
            '| District | 2012 | 2024 | Change | Annual Growth | % of Natl |',
            '|---|---:|---:|---:|---:|---:|',
        ]
        for row in significant_rows:
            annual_growth = (
                f"{row['annual_growth_rate']:+.2%}"
                if row['annual_growth_rate'] is not None
                else 'N/A'
            )
            proportion_national = (
                f"{row['proportion_national']:.1%}"
                if row.get('proportion_national') is not None
                else ''
            )
            lines.append(
                f"| {row['district']} | {row['2012']:,} | {row['2024']:,} | {row['change']:+,}{triangle(row['change'])} | {annual_growth}{triangle(row['annual_growth_rate'] or 0)} | {proportion_national} |"
            )
        if other_row:
            annual_growth = (
                f"{other_row['annual_growth_rate']:+.2%}"
                if other_row['annual_growth_rate'] is not None
                else 'N/A'
            )
            lines.append(
                f"| *{other_row['district']}* | *{other_row['2012']:,}* | *{other_row['2024']:,}* | *{other_row['change']:+,}{triangle(other_row['change'])}* | *{annual_growth}{triangle(other_row['annual_growth_rate'] or 0)}* | |"
            )

        highlights = []
        if (
            fastest_growing['annual_growth_rate']
            and fastest_growing['annual_growth_rate'] > 0
        ):
            highlights.append(
                f"**{fastest_growing['district']}** grew fastest at **{fastest_growing['annual_growth_rate']:+.2%}/yr**."
            )
        if (
            fastest_declining['annual_growth_rate']
            and fastest_declining['annual_growth_rate'] < 0
        ):
            highlights.append(
                f"**{fastest_declining['district']}** saw the steepest decline at **{fastest_declining['annual_growth_rate']:+.2%}/yr**."
            )
        elif fastest_declining != fastest_growing:
            highlights.append(
                f"**{fastest_declining['district']}** had the slowest growth at **{fastest_declining['annual_growth_rate']:+.2%}/yr**."
            )
        if (
            largest_absolute != fastest_growing
            and largest_absolute['change'] > 0
        ):
            highlights.append(
                f"**{largest_absolute['district']}** had the largest absolute increase (**{largest_absolute['change']:+,}**)."
            )

        if highlights:
            lines += ['', '*' + ' '.join(highlights) + '*']

        lines.append('')

    return '\n'.join(lines).rstrip()


def _write_chart(results):
    labels = []
    values = []
    colors = []

    for religion, rows in results.items():
        significant_rows = [row for row in rows if row['district_code'] is not None]
        if not significant_rows:
            continue
        top_row = max(
            significant_rows, key=lambda row: row.get('proportion_national', 0)
        )
        labels.append(religion)
        values.append(top_row.get('proportion_national', 0) * 100)
        colors.append(RELIGION_COLORS.get(religion, 'grey'))

    fig, ax = plt.subplots(figsize=(8, 4.8))
    if labels:
        ax.bar(labels, values, color=colors)
        ax.set_ylabel('% of national religion population')
        ax.set_title('Top district share by religion (2024)')
        ax.tick_params(axis='x', rotation=30)
    else:
        ax.text(0.5, 0.5, 'No chartable data', ha='center', va='center')
        ax.set_axis_off()
    fig.tight_layout()
    fig.savefig(CHART_PATH, dpi=150)
    plt.close(fig)
