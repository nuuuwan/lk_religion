import json
from pathlib import Path

import matplotlib.pyplot as plt

from lk_religion.common.MarkdownUtils import write_markdown
from lk_religion.common.ReligionUtils import (
    RELIGION_COLORS,
    RELIGIONS,
    shares,
    triangle,
)

ROOT_DIR = Path(__file__).resolve().parents[3]
ANALYSIS_DIR = ROOT_DIR / 'analyses' / 'a0-national-population-by-religion'
README_PATH = ANALYSIS_DIR / 'README.md'
CHART_PATH = ANALYSIS_DIR / 'chart.png'
YEARS = 2024 - 2012


def run():
    print('=== 1) National totals by religion ===')

    religion_2012 = _load_religion_data(2012)
    religion_2024 = _load_religion_data(2024)

    with open(ANALYSIS_DIR / 'religion_2012.json', 'w') as f:
        json.dump(religion_2012, f, indent=2)
    with open(ANALYSIS_DIR / 'religion_2024.json', 'w') as f:
        json.dump(religion_2024, f, indent=2)

    totals_2012 = religion_2012
    totals_2024 = religion_2024

    shares_2012 = shares(totals_2012)
    shares_2024 = shares(totals_2024)

    rows = []
    for religion in RELIGIONS:
        v2012 = totals_2012[religion]
        v2024 = totals_2024[religion]
        change = v2024 - v2012
        proportion_2012 = shares_2012[religion]
        proportion_2024 = shares_2024[religion]
        annual_growth = (
            (v2024 / v2012) ** (1 / YEARS) - 1 if v2012 > 0 else None
        )
        rows.append(
            {
                'religion': religion,
                '2012': v2012,
                '2024': v2024,
                'change': change,
                'annual_growth_rate': (
                    round(annual_growth, 6)
                    if annual_growth is not None
                    else None
                ),
                'proportion_2012': round(proportion_2012, 6),
                'proportion_2024': round(proportion_2024, 6),
                'proportion_change': round(proportion_2024 - proportion_2012, 6),
            }
        )

    rows.sort(key=lambda row: row['proportion_2024'], reverse=True)

    with open(ANALYSIS_DIR / 'national_totals_by_religion.json', 'w') as f:
        json.dump(rows, f, indent=2)

    _write_chart(rows)

    print(
        f"{'Religion':<20} {'2012':>12} {'2024':>12} {'Change':>12} {'Ann. Growth':>12} {'Share 2012':>12} {'Share 2024':>12} {'Δ Share':>10}"
    )
    print('-' * 108)
    for row in rows:
        annual_growth = (
            f"{row['annual_growth_rate']:+.2%}"
            if row['annual_growth_rate'] is not None
            else '   N/A'
        )
        print(
            f"{row['religion']:<20} {row['2012']:>12,} {row['2024']:>12,} {row['change']:>+12,} {annual_growth:>12} {row['proportion_2012']:>11.1%} {row['proportion_2024']:>11.1%} {_format_percentage_point_change(row['proportion_change']):>10}"
        )

    return write_markdown(README_PATH, _readme_section(rows))


def _load_religion_data(year):
    try:
        from lanka_data import Db

        return Db(f'/LK/Religion/{year}')
    except Exception:
        return json.loads((ANALYSIS_DIR / f'religion_{year}.json').read_text())


def _normalized_percentage_point_change(value):
    rounded_pp = round(value * 100, 1)
    if rounded_pp == 0:
        return 0.0
    return rounded_pp / 100


def _format_percentage_point_change(value):
    normalized_value = _normalized_percentage_point_change(value)
    return f'{normalized_value * 100:+.1f}pp' if normalized_value else '0.0pp'


def _readme_section(rows):
    total_2012 = sum(row['2012'] for row in rows)
    total_2024 = sum(row['2024'] for row in rows)
    total_change = total_2024 - total_2012
    total_growth = (total_2024 / total_2012) ** (1 / YEARS) - 1

    buddhist = next(row for row in rows if row['religion'] == 'Buddhist')
    islam = next(row for row in rows if row['religion'] == 'Islam')
    buddhist_share_2024 = buddhist['2024'] / total_2024
    islam_share_2024 = islam['2024'] / total_2024

    lines = [
        '## A0. National Population by Religion',
        '',
        '![A0 representative chart](chart.png)',
        '',
        '### Commentary',
        '',
        f"- Sri Lanka's total population grew from **{total_2012:,}** (2012) to **{total_2024:,}** (2024), an increase of **{total_change:+,}** at an annual rate of **{total_growth:+.2%}**.",
        f"- **Buddhism** remains the dominant religion, accounting for **{buddhist_share_2024:.1%}** of the population in 2024, growing at **{buddhist['annual_growth_rate']:+.2%}** per year.",
        f"- **Islam** has the fastest growth rate among major religions at **{islam['annual_growth_rate']:+.2%}** per year, reaching a share of **{islam_share_2024:.1%}** in 2024.",
        '- **Roman Catholic** and **Other Christian** communities show slight declines over the period.',
    ]
    return '\n'.join(lines)


def _write_chart(rows):
    labels = [row['religion'] for row in rows]
    values = [row['change'] for row in rows]
    colors = [RELIGION_COLORS.get(label, 'grey') for label in labels]

    fig, ax = plt.subplots(figsize=(8, 4.8))
    bars = ax.bar(labels, values, color=colors)
    ax.set_title('Population change by religion (2012–2024)')
    ax.set_ylabel('Population change')
    ax.axhline(0, color='black', linewidth=0.8)
    ax.tick_params(axis='x', rotation=30)
    max_abs_value = max(abs(value) for value in values) if values else 0
    label_offset = max(max_abs_value * 0.02, 20000)
    for bar, value in zip(bars, values):
        x = bar.get_x() + bar.get_width() / 2
        if value >= 0:
            y = value + label_offset
            va = 'bottom'
        else:
            y = value - label_offset
            va = 'top'
        ax.text(
            x,
            y,
            f'{value:+,}',
            ha='center',
            va=va,
            fontsize=9,
        )
    fig.tight_layout()
    fig.savefig(CHART_PATH, dpi=150)
    plt.close(fig)
