import json
from pathlib import Path

import matplotlib.pyplot as plt
from lanka_data import Db, RegionNames

from analyses.proportion_change_common import (
    NEGATIVE_COLOR,
    POSITIVE_COLOR,
    RELIGIONS,
    shares,
    triangle,
)

ANALYSIS_DIR = Path(__file__).resolve().parent
README_PATH = ANALYSIS_DIR / 'README.md'
CHART_PATH = ANALYSIS_DIR / 'chart.png'
MIN_CHANGE_ABS = 0.01


def run():
    print('=== 3) Largest change in religious proportion ===')

    db_dist_2012 = Db('/LK:Districts/Religion/2012')
    db_dist_2024 = Db('/LK:Districts/Religion/2024')
    region_names = RegionNames()

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
                'district': region_names.name_for(code),
                'religion': max_religion,
                'proportion_2012': round(shares_2012[max_religion], 6),
                'proportion_2024': round(shares_2024[max_religion], 6),
                'change': round(change, 6),
            }
        )
    district_rows.sort(key=lambda row: row['change'], reverse=True)

    with open(ANALYSIS_DIR / 'proportion_change_analysis.json', 'w') as f:
        json.dump({'by_district': district_rows}, f, indent=2)

    _write_chart(district_rows)

    for religion in RELIGIONS:
        religion_rows = [
            row for row in district_rows if row['religion'] == religion
        ]
        if not religion_rows:
            continue
        print(f'\n  {religion}:')
        print(
            f"  {'District':<16} {'2012':>8} {'2024':>8} {'Change':>10}"
        )
        print('  ' + '-' * 48)
        for row in religion_rows:
            print(
                f"  {row['district']:<16} {row['proportion_2012']:>8.1%} {row['proportion_2024']:>8.1%} {row['change'] * 100:>+9.1f}pp"
            )

    return _write_readme(_readme_section(district_rows))


def _write_readme(content):
    README_PATH.write_text(content + '\n')
    return content


def _readme_section(district_rows):
    lines = [
        '## A3. Largest Change in Religious Proportion',
        '',
        '![A3 representative chart](chart.png)',
        '',
        f'For each district, the religion whose share of the local population changed most between 2012 and 2024, showing only rows with absolute change > {MIN_CHANGE_ABS:.0%}.',
    ]
    for religion in RELIGIONS:
        religion_rows = [
            row for row in district_rows if row['religion'] == religion
        ]
        if not religion_rows:
            continue
        lines.extend(
            [
                '',
                f'### {religion}',
                '',
                '| District | Share 2012 | Share 2024 | Change (pp) |',
                '|---|---:|---:|---:|',
            ]
        )
        for row in religion_rows:
            district_label = f"{row['district']} `{row['district_code']}`"
            lines.append(
                f"| {district_label} | {row['proportion_2012']:.1%} | {row['proportion_2024']:.1%} | {row['change'] * 100:+.1f}pp{triangle(row['change'])} |"
            )

    return '\n'.join(lines)


def _write_chart(district_rows):
    top_rows = district_rows[:15]
    labels = [row['district'] for row in top_rows]
    values = [row['change'] * 100 for row in top_rows]
    colors = [NEGATIVE_COLOR if value < 0 else POSITIVE_COLOR for value in values]

    fig, ax = plt.subplots(figsize=(8, 5.6))
    if labels:
        ax.barh(labels, values, color=colors)
        ax.set_title('Largest district-level religion share changes (pp)')
        ax.set_xlabel('Change in percentage points')
        ax.invert_yaxis()
    else:
        ax.text(0.5, 0.5, 'No chartable data', ha='center', va='center')
        ax.set_axis_off()
    fig.tight_layout()
    fig.savefig(CHART_PATH, dpi=150)
    plt.close(fig)
