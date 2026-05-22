import json
from pathlib import Path

from gig import Ent

from lk_religion.common.MarkdownUtils import write_markdown
from lk_religion.common.ReligionUtils import RELIGIONS, shares, triangle

ROOT_DIR = Path(__file__).resolve().parents[3]
ANALYSIS_DIR = ROOT_DIR / 'analyses' / 'a5_proportion_change_by_dsd'
README_PATH = ANALYSIS_DIR / 'README.md'
A4_ANALYSIS_PATH = ROOT_DIR / 'analyses' / 'a4_by_dsd' / 'religion_by_dsd_analysis.json'
A7_DIR = ROOT_DIR / 'analyses' / 'a7_by_dsd'

TOP_DSD = 50
MIN_ABSOLUTE = 1000
MIN_NATIONAL_SHARE = 0.01
MIN_CHANGE_ABS = 0.01


def run():
    print('=== 5) Largest change in religious proportion (DSD) ===')

    db_dsd_2012, db_dsd_2024, national2024, name_for = _load_data()

    dsd_analysis = json.loads(A4_ANALYSIS_PATH.read_text())
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
            key=lambda religion: abs(shares_2024[religion] - shares_2012[religion]),
        )
        change = shares_2024[max_religion] - shares_2012[max_religion]
        if abs(change) <= MIN_CHANGE_ABS:
            continue
        dsd_rows.append(
            {
                'dsd_code': code,
                'dsd': name_for(code),
                'district': name_for(code[:5]),
                'religion': max_religion,
                'proportion_2012': round(shares_2012[max_religion], 6),
                'proportion_2024': round(shares_2024[max_religion], 6),
                'change': round(change, 6),
            }
        )
    dsd_rows.sort(key=lambda row: row['change'], reverse=True)

    with open(ANALYSIS_DIR / 'proportion_change_by_dsd_analysis.json', 'w') as f:
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

    return write_markdown(README_PATH, _readme_section(dsd_rows))


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
        religion_rows = [row for row in top_rows if row['religion'] == religion]
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
            dsd_label = f"{row['dsd']} `{row['dsd_code']}`"
            district_label = f"{row['district']} `{row['dsd_code'][:5]}`"
            lines.append(
                f"| {dsd_label} | {district_label} | {row['proportion_2012']:.1%} | {row['proportion_2024']:.1%} | {row['change'] * 100:+.1f}pp{triangle(row['change'])} |"
            )

    return '\n'.join(lines)


def _name_for_ent(code):
    try:
        return Ent.from_id(code).name
    except Exception:
        return code


def _load_data():
    try:
        from lanka_data import Db, RegionNames

        region_names = RegionNames()
        return (
            Db('/LK:DSDs/Religion/2012'),
            Db('/LK:DSDs/Religion/2024'),
            Db('/LK/Religion/2024'),
            region_names.name_for,
        )
    except Exception:
        return (
            json.loads((A7_DIR / 'religion_by_dsd_2012.json').read_text()),
            json.loads((A7_DIR / 'religion_by_dsd_2024.json').read_text()),
            json.loads((ROOT_DIR / 'analyses' / 'a1_national_totals' / 'religion_2024.json').read_text()),
            _name_for_ent,
        )
