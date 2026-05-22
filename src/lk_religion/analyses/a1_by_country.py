import json
from pathlib import Path

import matplotlib.pyplot as plt

from lk_religion.common.MarkdownUtils import write_markdown
from lk_religion.common.ReligionUtils import (
    RELIGION_COLORS,
    RELIGION_LABELS,
    RELIGIONS,
    format_pp,
    shares,
)

ROOT_DIR = Path(__file__).resolve().parents[3]
ANALYSIS_DIR = ROOT_DIR / 'analyses' / 'a1-religion-by-country-key-trends'
README_PATH = ANALYSIS_DIR / 'README.md'
CHART_PATH = ANALYSIS_DIR / 'chart.png'
ANALYSIS_PATH = ANALYSIS_DIR / 'religion_pp_change_analysis.json'
YEARS = 2024 - 2012


def run():
    religion_2012 = _load_religion_data(2012)
    religion_2024 = _load_religion_data(2024)

    shares_2012 = shares(religion_2012)
    shares_2024 = shares(religion_2024)

    rows = []
    for religion in RELIGIONS:
        v2012 = religion_2012.get(religion, 0)
        v2024 = religion_2024.get(religion, 0)
        annual_growth = ((v2024 / v2012) ** (1 / YEARS) - 1) if v2012 > 0 else None
        rows.append(
            {
                'religion': religion,
                'label': RELIGION_LABELS[religion],
                'share_2012': shares_2012[religion],
                'share_2024': shares_2024[religion],
                'pp_change': shares_2024[religion] - shares_2012[religion],
                'population_2012': v2012,
                'population_2024': v2024,
                'annual_growth_rate': annual_growth,
            }
        )

    with open(ANALYSIS_PATH, 'w') as f:
        json.dump(rows, f, indent=2)

    _write_chart(rows)
    return write_markdown(README_PATH, _readme_section(rows, religion_2012, religion_2024))


def _load_religion_data(year):
    try:
        from lanka_data import Db

        return Db(f'/LK/Religion/{year}')
    except Exception:
        fallback_dir = ROOT_DIR / 'analyses' / 'a0-national-population-by-religion'
        return json.loads((fallback_dir / f'religion_{year}.json').read_text())


def _readme_section(rows, religion_2012, religion_2024):
    total_2012 = religion_2012.get('TotalPopulation') or sum(
        religion_2012.get(religion, 0) for religion in RELIGIONS
    )
    total_2024 = religion_2024.get('TotalPopulation') or sum(
        religion_2024.get(religion, 0) for religion in RELIGIONS
    )
    total_change = total_2024 - total_2012
    total_growth = (total_2024 / total_2012) ** (1 / YEARS) - 1

    top_gain = max(rows, key=lambda row: row['pp_change'])
    top_decline = min(rows, key=lambda row: row['pp_change'])
    stable = [
        row['label'] for row in rows if abs(round(row['pp_change'] * 100, 1)) < 0.1
    ]
    stable_text = ', '.join(f'**{label}**' for label in stable) if stable else 'None'

    lines = [
        '## A1. National Religion Share Change (pp)',
        '',
        '![A1 pp changes by religion](chart.png)',
        '',
        '### Commentary',
        '',
        f"- Sri Lanka's total population grew from **{total_2012:,}** (2012) to **{total_2024:,}** (2024), an increase of **{total_change:+,}** at an annual rate of **{total_growth:+.2%}**.",
        f"- **{top_gain['label']}** recorded the largest increase in national share at **{format_pp(top_gain['pp_change'])}pp**, reaching **{top_gain['share_2024']:.1%}** in 2024.",
        f"- **{top_decline['label']}** recorded the largest decline in national share at **{format_pp(top_decline['pp_change'])}pp**, with a 2024 share of **{top_decline['share_2024']:.1%}**.",
        f'- Religions with near-stable national shares (change within ±0.1pp): {stable_text}.',
    ]
    return '\n'.join(lines)


def _write_chart(rows):
    labels = [row['label'] for row in rows]
    values = [row['pp_change'] * 100 for row in rows]
    colors = [RELIGION_COLORS[row['religion']] for row in rows]

    fig, ax = plt.subplots(figsize=(8, 4.8))
    bars = ax.bar(labels, values, color=colors)
    ax.set_title('Change in national share by religion (2012–2024)')
    ax.set_ylabel('Share change (percentage points)')
    ax.axhline(0, color='black', linewidth=0.8)
    ax.tick_params(axis='x', rotation=30)

    max_abs_value = max(abs(value) for value in values) if values else 0
    label_offset = max(max_abs_value * 0.05, 0.08)
    for bar, value in zip(bars, values):
        x = bar.get_x() + bar.get_width() / 2
        if value >= 0:
            y = value + label_offset
            va = 'bottom'
        else:
            y = value - label_offset
            va = 'top'
        ax.text(x, y, f'{value:+.1f}pp', ha='center', va=va, fontsize=9)

    ax.margins(y=0.15)
    fig.tight_layout()
    fig.savefig(CHART_PATH, dpi=150)
    plt.close(fig)
