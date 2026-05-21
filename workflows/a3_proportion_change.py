import json
import os

from lanka_data import Db, RegionNames

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

RELIGIONS = [
    "Buddhist",
    "Hindu",
    "Islam",
    "RomanCatholic",
    "OtherChristian",
    "Other",
]
TOP_DSD = 50
MIN_ABSOLUTE = 1000
MIN_NATIONAL_SHARE = 0.01  # 1% of that religion's national count


def _shares(data):
    total = data.get("TotalPopulation") or sum(
        data.get(r, 0) for r in RELIGIONS
    )
    if total == 0:
        return {r: 0.0 for r in RELIGIONS}
    return {r: data.get(r, 0) / total for r in RELIGIONS}


def run():
    print("=== 3) Largest change in religious proportion ===")

    db_dist_2012 = Db("/LK:Districts/Religion/2012")
    db_dist_2024 = Db("/LK:Districts/Religion/2024")
    db_dsd_2012 = Db("/LK:DSDs/Religion/2012")
    db_dsd_2024 = Db("/LK:DSDs/Religion/2024")
    national2024 = Db("/LK/Religion/2024")
    rn = RegionNames()

    # Load excluded DSDs (altered / new / removed) from A3 output
    with open(os.path.join(DATA_DIR, "religion_by_dsd_analysis.json")) as f:
        dsd_analysis = json.load(f)
    excluded_dsds = {r["dsd_code"] for r in dsd_analysis["flagged"]}

    # --- By District ---
    district_rows = []
    for code in db_dist_2012:
        if code not in db_dist_2024:
            continue
        s2012 = _shares(db_dist_2012[code])
        s2024 = _shares(db_dist_2024[code])
        max_religion = max(RELIGIONS, key=lambda r: abs(s2024[r] - s2012[r]))
        change = s2024[max_religion] - s2012[max_religion]
        district_rows.append(
            {
                "district_code": code,
                "district": rn.name_for(code),
                "religion": max_religion,
                "proportion_2012": round(s2012[max_religion], 6),
                "proportion_2024": round(s2024[max_religion], 6),
                "change": round(change, 6),
            }
        )
    district_rows.sort(key=lambda r: abs(r["change"]), reverse=True)

    # --- By DSD ---
    dsd_rows = []
    for code in db_dsd_2012:
        if code in excluded_dsds or code not in db_dsd_2024:
            continue
        s2012 = _shares(db_dsd_2012[code])
        s2024 = _shares(db_dsd_2024[code])
        eligible = [
            r
            for r in RELIGIONS
            if max(db_dsd_2012[code].get(r, 0), db_dsd_2024[code].get(r, 0))
            >= MIN_ABSOLUTE
            and max(db_dsd_2012[code].get(r, 0), db_dsd_2024[code].get(r, 0))
            >= national2024[r] * MIN_NATIONAL_SHARE
        ]
        if not eligible:
            continue
        max_religion = max(eligible, key=lambda r: abs(s2024[r] - s2012[r]))
        change = s2024[max_religion] - s2012[max_religion]
        dsd_rows.append(
            {
                "dsd_code": code,
                "dsd": rn.name_for(code),
                "district": rn.name_for(code[:5]),
                "religion": max_religion,
                "proportion_2012": round(s2012[max_religion], 6),
                "proportion_2024": round(s2024[max_religion], 6),
                "change": round(change, 6),
            }
        )
    dsd_rows.sort(key=lambda r: abs(r["change"]), reverse=True)

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(
        os.path.join(DATA_DIR, "proportion_change_analysis.json"), "w"
    ) as f:
        json.dump(
            {"by_district": district_rows, "by_dsd": dsd_rows}, f, indent=2
        )

    print(f"\n  By District:")
    print(
        f"  {'District':<16} {'Religion':<16} {'2012':>8} {'2024':>8} {'Change':>10}"
    )
    print("  " + "-" * 62)
    for row in district_rows:
        print(
            f"  {row['district']:<16} {row['religion']:<16} {row['proportion_2012']:>8.1%} {row['proportion_2024']:>8.1%} {row['change']:>+10.1%}"
        )

    print(f"\n  By DSD (top {TOP_DSD}, excl. altered/new/removed):")
    print(
        f"  {'DSD':<22} {'District':<14} {'Religion':<16} {'2012':>8} {'2024':>8} {'Change':>10}"
    )
    print("  " + "-" * 82)
    for row in dsd_rows[:TOP_DSD]:
        print(
            f"  {row['dsd']:<22} {row['district']:<14} {row['religion']:<16} {row['proportion_2012']:>8.1%} {row['proportion_2024']:>8.1%} {row['change']:>+10.1%}"
        )

    return _readme_section(district_rows, dsd_rows)


def _readme_section(district_rows, dsd_rows):
    lines = [
        "## A3. Largest Change in Religious Proportion",
        "",
        "For each district and DSD, the religion whose share of the local population "
        "changed most between 2012 and 2024.",
        "",
        "### By District",
        "",
        "| District | Religion | Share 2012 | Share 2024 | Change |",
        "|---|---|---:|---:|---:|",
    ]
    for row in district_rows:
        lines.append(
            f"| {row['district']} | {row['religion']} | {row['proportion_2012']:.1%} "
            f"| {row['proportion_2024']:.1%} | {row['change']:+.1%} |"
        )

    lines += [
        "",
        "### By DSD",
        "",
        f"*Altered, new, and removed DSDs excluded. Religions with <{MIN_NATIONAL_SHARE:.0%} of "
        f"national count or <{MIN_ABSOLUTE:,} people in the DSD are excluded.*",
        "",
        "| DSD | District | Religion | Share 2012 | Share 2024 | Change |",
        "|---|---|---|---:|---:|---:|",
    ]
    for row in dsd_rows[:TOP_DSD]:
        lines.append(
            f"| {row['dsd']} | {row['district']} | {row['religion']} | {row['proportion_2012']:.1%} "
            f"| {row['proportion_2024']:.1%} | {row['change']:+.1%} |"
        )

    return "\n".join(lines)
