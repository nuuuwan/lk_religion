import json
from pathlib import Path

from lanka_data import Db, RegionNames

ANALYSIS_DIR = Path(__file__).resolve().parent
README_PATH = ANALYSIS_DIR / 'README.md'
A4_ANALYSIS_PATH = (
    Path(__file__).resolve().parents[1]
    / 'a4_by_dsd'
    / 'religion_by_dsd_analysis.json'
)

RELIGIONS = [
    'Buddhist',
    'Hindu',
    'Islam',
    'RomanCatholic',
    'OtherChristian',
    'Other',
]
TOP_DSD = 50
MIN_ABSOLUTE = 1000
MIN_NATIONAL_SHARE = 0.01  # 1% of that religion's national count


def _shares(data):
    total = data.get('TotalPopulation') or sum(
        data.get(religion, 0) for religion in RELIGIONS
    )
    if total == 0:
        return {religion: 0.0 for religion in RELIGIONS}
    return {religion: data.get(religion, 0) / total for religion in RELIGIONS}


def run():
    print('=== 3) Largest change in religious proportion ===')

    db_dist_2012 = Db('/LK:Districts/Religion/2012')
    db_dist_2024 = Db('/LK:Districts/Religion/2024')
    db_dsd_2012 = Db('/LK:DSDs/Religion/2012')
    db_dsd_2024 = Db('/LK:DSDs/Religion/2024')
    national2024 = Db('/LK/Religion/2024')
    region_names = RegionNames()

    with open(A4_ANALYSIS_PATH) as f:
        dsd_analysis = json.load(f)
    excluded_dsds = {row['dsd_code'] for row in dsd_analysis['flagged']}

    district_rows = []
    for code in db_dist_2012:
        if code not in db_dist_2024:
            continue
        shares_2012 = _shares(db_dist_2012[code])
        shares_2024 = _shares(db_dist_2024[code])
        max_religion = max(
            RELIGIONS,
            key=lambda religion: abs(
                shares_2024[religion] - shares_2012[religion]
            ),
        )
        change = shares_2024[max_religion] - shares_2012[max_religion]
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
    district_rows.sort(key=lambda row: abs(row['change']), reverse=True)

    dsd_rows = []
    for code in db_dsd_2012:
        if code in excluded_dsds or code not in db_dsd_2024:
            continue
        shares_2012 = _shares(db_dsd_2012[code])
        shares_2024 = _shares(db_dsd_2024[code])
        eligible = [
            religion
            for religion in RELIGIONS
            if max(db_dsd_2012[code].get(religion, 0), db_dsd_2024[code].get(religion, 0))
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
    dsd_rows.sort(key=lambda row: abs(row['change']), reverse=True)

    with open(ANALYSIS_DIR / 'proportion_change_analysis.json', 'w') as f:
        json.dump(
            {'by_district': district_rows, 'by_dsd': dsd_rows}, f, indent=2
        )

    print('\n  By District:')
    print(
        f"  {'District':<16} {'Religion':<16} {'2012':>8} {'2024':>8} {'Change':>10}"
    )
    print('  ' + '-' * 62)
    for row in district_rows:
        print(
            f"  {row['district']:<16} {row['religion']:<16} {row['proportion_2012']:>8.1%} {row['proportion_2024']:>8.1%} {row['change']:>+10.1%}"
        )

    print(f'\n  By DSD (top {TOP_DSD}, excl. altered/new/removed):')
    print(
        f"  {'DSD':<22} {'District':<14} {'Religion':<16} {'2012':>8} {'2024':>8} {'Change':>10}"
    )
    print('  ' + '-' * 82)
    for row in dsd_rows[:TOP_DSD]:
        print(
            f"  {row['dsd']:<22} {row['district']:<14} {row['religion']:<16} {row['proportion_2012']:>8.1%} {row['proportion_2024']:>8.1%} {row['change']:>+10.1%}"
        )

    return _write_readme(_readme_section(district_rows, dsd_rows))


def _write_readme(content):
    README_PATH.write_text(content + '\n')
    return content


def _readme_section(district_rows, dsd_rows):
    lines = [
        '## A3. Largest Change in Religious Proportion',
        '',
        'For each district and DSD, the religion whose share of the local population changed most between 2012 and 2024.',
        '',
        '### By District',
        '',
        '| District | Religion | Share 2012 | Share 2024 | Change |',
        '|---|---|---:|---:|---:|',
    ]
    for row in district_rows:
        lines.append(
            f"| {row['district']} | {row['religion']} | {row['proportion_2012']:.1%} | {row['proportion_2024']:.1%} | {row['change']:+.1%} |"
        )

    lines += [
        '',
        '### By DSD',
        '',
        f'*Altered, new, and removed DSDs excluded. Religions with <{MIN_NATIONAL_SHARE:.0%} of national count or <{MIN_ABSOLUTE:,} people in the DSD are excluded.*',
        '',
        '| DSD | District | Religion | Share 2012 | Share 2024 | Change |',
        '|---|---|---|---:|---:|---:|',
    ]
    for row in dsd_rows[:TOP_DSD]:
        lines.append(
            f"| {row['dsd']} | {row['district']} | {row['religion']} | {row['proportion_2012']:.1%} | {row['proportion_2024']:.1%} | {row['change']:+.1%} |"
        )

    return '\n'.join(lines)
