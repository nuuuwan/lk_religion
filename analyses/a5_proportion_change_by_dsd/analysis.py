import json
from pathlib import Path

from lanka_data import Db, RegionNames

from analyses.proportion_change_common import RELIGIONS, shares, triangle

ANALYSIS_DIR = Path(__file__).resolve().parent
README_PATH = ANALYSIS_DIR / 'README.md'
A4_ANALYSIS_PATH = (
    Path(__file__).resolve().parents[1]
    / 'a4_by_dsd'
    / 'religion_by_dsd_analysis.json'
)

TOP_DSD = 50
MIN_ABSOLUTE = 1000
MIN_NATIONAL_SHARE = 0.01  # 1% of that religion's national count
MIN_CHANGE_ABS = 0.01


def run():
    print('=== 5) Largest change in religious proportion (DSD) ===')

    db_dsd_2012 = Db('/LK:DSDs/Religion/2012')
    db_dsd_2024 = Db('/LK:DSDs/Religion/2024')
    national2024 = Db('/LK/Religion/2024')
    region_names = RegionNames()

    with open(A4_ANALYSIS_PATH) as f:
        dsd_analysis = json.load(f)
    excluded_dsds = {row['dsd_code'] for row in dsd_analysis['flagged']}

    dsd_rows = []
    for code in db_dsd_2012:
        if code in excluded_dsds or code not in db_dsd_2024:
            continue
        shares_2012 = shares(db_dsd_2012[code])
        shares_2024 = shares(db_dsd_2024[code])
        eligible = [
            religion
            for religion in RELIGIONS
            if max(
                db_dsd_2012[code].get(religion, 0),
                db_dsd_2024[code].get(religion, 0),
            )
            >= MIN_ABSOLUTE
            and max(
                db_dsd_2012[code].get(religion, 0),
                db_dsd_2024[code].get(religion, 0),
            )
            >= national2024[religion] * MIN_NATIONAL_SHARE
        ]
        if not eligible:
            continue
        max_religion = max(
            eligible,
            key=lambda religion: abs(
                shares_2024[religion] - shares_2012[religion]
            ),
        )
        change = shares_2024[max_religion] - shares_2012[max_religion]
        if abs(change) <= MIN_CHANGE_ABS:
            continue
        dsd_rows.append(
            {
                'dsd_code': code,
                'dsd': region_names.name_for(code),
                'district': region_names.name_for(code[:5]),
                'religion': max_religion,
                'proportion_2012': round(shares_2012[max_religion], 6),
                'proportion_2024': round(shares_2024[max_religion], 6),
                'change': round(change, 6),
            }
        )
    dsd_rows.sort(key=lambda row: row['change'], reverse=True)

    with open(
        ANALYSIS_DIR / 'proportion_change_by_dsd_analysis.json', 'w'
    ) as f:
        json.dump({'by_dsd': dsd_rows}, f, indent=2)

    print(f'\n  By DSD (top {TOP_DSD}, excl. altered/new/removed):')
    print(
        f"  {'DSD':<22} {'District':<14} {'Religion':<16} {'2012':>8} {'2024':>8} {'Change':>10}"
    )
    print('  ' + '-' * 82)
    for row in dsd_rows[:TOP_DSD]:
        print(
            f"  {row['dsd']:<22} {row['district']:<14} {row['religion']:<16} {row['proportion_2012']:>8.1%} {row['proportion_2024']:>8.1%} {row['change'] * 100:>+9.1f}pp"
        )

    return _write_readme(_readme_section(dsd_rows))


def _write_readme(content):
    README_PATH.write_text(content + '\n')
    return content


def _readme_section(dsd_rows):
    top_rows = dsd_rows[:TOP_DSD]
    lines = [
        '## A5. Largest Change in Religious Proportion by DSD',
        '',
        f'For each DSD, the religion whose share of the local population changed most between 2012 and 2024, showing only rows with absolute change > {MIN_CHANGE_ABS:.0%}.',
        '',
        f'*Altered, new, and removed DSDs excluded. Religions with <{MIN_NATIONAL_SHARE:.0%} of national count or <{MIN_ABSOLUTE:,} people in the DSD are excluded.*',
    ]

    for religion in RELIGIONS:
        religion_rows = [
            row for row in top_rows if row['religion'] == religion
        ]
        if not religion_rows:
            continue
        lines.extend(
            [
                '',
                f'### {religion}',
                '',
                '| DSD | District | Share 2012 | Share 2024 | Change (pp) |',
                '|---|---|---:|---:|---:|',
            ]
        )
        for row in religion_rows:
            lines.append(
                f"| {row['dsd']} | {row['district']} | {row['proportion_2012']:.1%} | {row['proportion_2024']:.1%} | {row['change'] * 100:+.1f}pp{triangle(row['change'])} |"
            )

    return '\n'.join(lines)
