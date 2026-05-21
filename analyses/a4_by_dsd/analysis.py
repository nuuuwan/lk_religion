import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
from lanka_data import Db, RegionNames

from analyses.proportion_change_common import triangle

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
BOUNDARY_POP_CHANGE_FACTOR = 2.0


def _shares(data):
    total = data.get('TotalPopulation') or sum(
        data.get(religion, 0) for religion in RELIGIONS
    )
    if total == 0:
        return {religion: 0.0 for religion in RELIGIONS}
    return {religion: data.get(religion, 0) / total for religion in RELIGIONS}


def run():
    print('=== 4) DSD-level boundary and distributional change ===')

    db2012 = Db('/LK:DSDs/Religion/2012')
    db2024 = Db('/LK:DSDs/Religion/2024')
    national2012 = Db('/LK/Religion/2012')
    national2024 = Db('/LK/Religion/2024')
    region_names = RegionNames()

    national_growth = (
        national2024['TotalPopulation'] / national2012['TotalPopulation'] - 1
    )

    dist_count_2012 = Counter(key[:5] for key in db2012)
    dist_count_2024 = Counter(key[:5] for key in db2024)
    boundary_districts = {
        district
        for district in set(dist_count_2012) | set(dist_count_2024)
        if dist_count_2012.get(district, 0) != dist_count_2024.get(district, 0)
    }

    keys_2012 = set(db2012)
    keys_2024 = set(db2024)
    all_keys = keys_2012 | keys_2024

    flagged = []

    for code in sorted(all_keys):
        district_code = code[:5]
        in_boundary_district = district_code in boundary_districts
        new_dsd = code not in keys_2012
        removed_dsd = code not in keys_2024

        if new_dsd or removed_dsd:
            flagged.append(
                {
                    'status': 'New' if new_dsd else 'Removed',
                    'dsd_code': code,
                    'dsd': region_names.name_for(code),
                    'district': region_names.name_for(district_code),
                    'total_2012': (
                        db2012[code].get('TotalPopulation', 0)
                        if removed_dsd
                        else None
                    ),
                    'total_2024': (
                        db2024[code].get('TotalPopulation', 0)
                        if new_dsd
                        else None
                    ),
                    'pop_change_pct': None,
                }
            )
            continue

        if in_boundary_district:
            pop_2012 = db2012[code].get('TotalPopulation', 0)
            pop_2024 = db2024[code].get('TotalPopulation', 0)
            if pop_2012 > 0:
                dsd_growth = pop_2024 / pop_2012 - 1
                deviation = abs(dsd_growth - national_growth)
                if deviation > BOUNDARY_POP_CHANGE_FACTOR * abs(
                    national_growth
                ):
                    flagged.append(
                        {
                            'status': 'Altered',
                            'dsd_code': code,
                            'dsd': region_names.name_for(code),
                            'district': region_names.name_for(district_code),
                            'total_2012': pop_2012,
                            'total_2024': pop_2024,
                            'pop_change_pct': round(dsd_growth * 100, 2),
                        }
                    )

    normal_rows = []
    for code in keys_2012 & keys_2024:
        shares_2012 = _shares(db2012[code])
        shares_2024 = _shares(db2024[code])
        dist_change = sum(
            abs(shares_2024[religion] - shares_2012[religion])
            for religion in RELIGIONS
        )
        normal_rows.append(
            {
                'dsd_code': code,
                'dsd': region_names.name_for(code),
                'district': region_names.name_for(code[:5]),
                'total_2012': db2012[code].get('TotalPopulation', 0),
                'total_2024': db2024[code].get('TotalPopulation', 0),
                'distributional_change': round(dist_change, 6),
            }
        )
    normal_rows.sort(
        key=lambda row: row['distributional_change'], reverse=True
    )

    with open(ANALYSIS_DIR / 'religion_by_dsd_analysis.json', 'w') as f:
        json.dump({'flagged': flagged, 'all_dsds': normal_rows}, f, indent=2)

    _write_chart(flagged)

    print(f'\n  National population growth 2012→2024: {national_growth:+.2%}')
    print(f'  Boundary-affected districts: {sorted(boundary_districts)}')
    print(f'\n  Flagged DSDs (new / altered / removed): {len(flagged)}')
    for row in flagged:
        pop_change = (
            f"  pop change {row['pop_change_pct']:+.1f}%"
            if row['pop_change_pct'] is not None
            else ''
        )
        print(
            f"  [{row['status']:8s}] {row['dsd_code']} — {row['dsd']} ({row['district']}){pop_change}"
        )

    return _write_readme(
        _readme_section(
            flagged,
            dist_count_2012,
            dist_count_2024,
            boundary_districts,
            national_growth,
            region_names,
        )
    )


def _write_readme(content):
    README_PATH.write_text(content + '\n')
    return content


def _readme_section(
    flagged,
    dist_count_2012,
    dist_count_2024,
    boundary_districts,
    national_growth,
    region_names,
):
    lines = [
        '## A4. DSD Boundary Changes',
        '',
        '![A4 representative chart](chart.png)',
        '',
        'Districts where the number of DSDs changed between censuses are listed below. Within those districts, DSDs whose population growth deviates from the national rate '
        f'({national_growth:+.2%} over 2012–2024) by more than '
        f'{BOUNDARY_POP_CHANGE_FACTOR:.0f}× are flagged as **Altered** — '
        'their apparent demographic shifts likely reflect re-demarcation rather than genuine change.',
        '',
    ]

    if boundary_districts:
        lines += ['**Districts with changed DSD boundaries:**', '']
        lines.append('| District | DSDs 2012 | DSDs 2024 | Δ |')
        lines.append('|---|---:|---:|---:|')
        for district in sorted(boundary_districts):
            n2012 = dist_count_2012.get(district, 0)
            n2024 = dist_count_2024.get(district, 0)
            delta = n2024 - n2012
            lines.append(
                f"| {region_names.name_for(district)} | {n2012} | {n2024} | {delta:+d}{triangle(delta)} |"
            )
        lines.append('')

    if flagged:
        lines += [
            '**New, Altered, and Removed DSDs:**',
            '',
            '| Status | Code | DSD | District | Pop 2012 | Pop 2024 | Pop Change |',
            '|---|---|---|---|---:|---:|---:|',
        ]
        for row in sorted(
            flagged,
            key=lambda item: (
                item['district'],
                {'Removed': 0, 'Altered': 1, 'New': 2}.get(item['status'], 3),
                item['dsd'],
            ),
        ):
            pop_2012 = (
                f"{row['total_2012']:,}" if row['total_2012'] is not None else '—'
            )
            pop_2024 = (
                f"{row['total_2024']:,}" if row['total_2024'] is not None else '—'
            )
            pop_change_val = row['pop_change_pct']
            pop_change = (
                f"{pop_change_val:+.1f}%{triangle(pop_change_val)}"
                if pop_change_val is not None
                else '—'
            )
            lines.append(
                f"| {row['status']} | {row['dsd_code']} | {row['dsd']} | {row['district']} | {pop_2012} | {pop_2024} | {pop_change} |"
            )

    return '\n'.join(lines)


def _write_chart(flagged):
    counts = Counter(row['status'] for row in flagged)
    labels = ['Removed', 'Altered', 'New']
    values = [counts.get(label, 0) for label in labels]
    colors = ['#f28e2b', '#4e79a7', '#59a14f']

    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.bar(labels, values, color=colors)
    ax.set_title('Flagged DSD status counts')
    ax.set_ylabel('Count')
    fig.tight_layout()
    fig.savefig(CHART_PATH, dpi=150)
    plt.close(fig)
