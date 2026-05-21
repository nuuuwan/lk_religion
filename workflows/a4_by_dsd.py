import json
import os
from collections import Counter

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
YEARS = 2024 - 2012
# A DSD in a boundary-affected district is flagged "altered" if its population
# growth deviates from the national growth by more than this multiplier.
BOUNDARY_POP_CHANGE_FACTOR = 2.0


def _shares(data):
    total = data.get("TotalPopulation") or sum(
        data.get(r, 0) for r in RELIGIONS
    )
    if total == 0:
        return {r: 0.0 for r in RELIGIONS}
    return {r: data.get(r, 0) / total for r in RELIGIONS}


def run():
    print("=== 4) DSD-level boundary and distributional change ===")

    db2012 = Db("/LK:DSDs/Religion/2012")
    db2024 = Db("/LK:DSDs/Religion/2024")
    national2012 = Db("/LK/Religion/2012")
    national2024 = Db("/LK/Religion/2024")
    rn = RegionNames()

    national_growth = (
        national2024["TotalPopulation"] / national2012["TotalPopulation"] - 1
    )

    # Districts whose DSD count changed
    dist_count_2012 = Counter(k[:5] for k in db2012)
    dist_count_2024 = Counter(k[:5] for k in db2024)
    boundary_districts = {
        d
        for d in set(dist_count_2012) | set(dist_count_2024)
        if dist_count_2012.get(d, 0) != dist_count_2024.get(d, 0)
    }

    keys_2012 = set(db2012)
    keys_2024 = set(db2024)
    all_keys = keys_2012 | keys_2024

    flagged = []  # new / altered / removed DSDs

    for code in sorted(all_keys):
        district_code = code[:5]
        in_boundary_district = district_code in boundary_districts
        new_dsd = code not in keys_2012
        removed_dsd = code not in keys_2024

        if new_dsd or removed_dsd:
            flagged.append(
                {
                    "status": "New" if new_dsd else "Removed",
                    "dsd_code": code,
                    "dsd": rn.name_for(code),
                    "district": rn.name_for(district_code),
                    "total_2012": (
                        db2012[code].get("TotalPopulation", 0)
                        if removed_dsd
                        else None
                    ),
                    "total_2024": (
                        db2024[code].get("TotalPopulation", 0)
                        if new_dsd
                        else None
                    ),
                    "pop_change_pct": None,
                }
            )
            continue

        if in_boundary_district:
            pop_2012 = db2012[code].get("TotalPopulation", 0)
            pop_2024 = db2024[code].get("TotalPopulation", 0)
            if pop_2012 > 0:
                dsd_growth = pop_2024 / pop_2012 - 1
                deviation = abs(dsd_growth - national_growth)
                if deviation > BOUNDARY_POP_CHANGE_FACTOR * abs(
                    national_growth
                ):
                    flagged.append(
                        {
                            "status": "Altered",
                            "dsd_code": code,
                            "dsd": rn.name_for(code),
                            "district": rn.name_for(district_code),
                            "total_2012": pop_2012,
                            "total_2024": pop_2024,
                            "pop_change_pct": round(dsd_growth * 100, 2),
                        }
                    )

    # All normal (non-new/removed) DSDs: compute distributional change
    normal_rows = []
    for code in keys_2012 & keys_2024:
        s2012 = _shares(db2012[code])
        s2024 = _shares(db2024[code])
        dist_change = sum(abs(s2024[r] - s2012[r]) for r in RELIGIONS)
        normal_rows.append(
            {
                "dsd_code": code,
                "dsd": rn.name_for(code),
                "district": rn.name_for(code[:5]),
                "total_2012": db2012[code].get("TotalPopulation", 0),
                "total_2024": db2024[code].get("TotalPopulation", 0),
                "distributional_change": round(dist_change, 6),
            }
        )
    normal_rows.sort(key=lambda r: r["distributional_change"], reverse=True)

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(
        os.path.join(DATA_DIR, "religion_by_dsd_analysis.json"), "w"
    ) as f:
        json.dump({"flagged": flagged, "all_dsds": normal_rows}, f, indent=2)

    print(f"\n  National population growth 2012→2024: {national_growth:+.2%}")
    print(f"  Boundary-affected districts: {sorted(boundary_districts)}")
    print(f"\n  Flagged DSDs (new / altered / removed): {len(flagged)}")
    for row in flagged:
        pc = (
            f"  pop change {row['pop_change_pct']:+.1f}%"
            if row["pop_change_pct"] is not None
            else ""
        )
        print(
            f"  [{row['status']:8s}] {row['dsd_code']} — {row['dsd']} ({row['district']}){pc}"
        )

    return _readme_section(
        flagged,
        dist_count_2012,
        dist_count_2024,
        boundary_districts,
        national_growth,
        rn,
    )


def _readme_section(
    flagged,
    dist_count_2012,
    dist_count_2024,
    boundary_districts,
    national_growth,
    rn,
):
    lines = [
        "## A4. DSD Boundary Changes",
        "",
        "Districts where the number of DSDs changed between censuses are listed below. "
        "Within those districts, DSDs whose population growth deviates from the national rate "
        f"({national_growth:+.2%} over 2012–2024) by more than "
        f"{BOUNDARY_POP_CHANGE_FACTOR:.0f}× are flagged as **Altered** — "
        "their apparent demographic shifts likely reflect re-demarcation rather than genuine change.",
        "",
    ]

    if boundary_districts:
        lines += ["**Districts with changed DSD boundaries:**", ""]
        lines.append("| District | DSDs 2012 | DSDs 2024 | Δ |")
        lines.append("|---|---:|---:|---:|")
        for d in sorted(boundary_districts):
            n2012 = dist_count_2012.get(d, 0)
            n2024 = dist_count_2024.get(d, 0)
            lines.append(
                f"| {rn.name_for(d)} | {n2012} | {n2024} | {n2024 - n2012:+d} |"
            )
        lines.append("")

    if flagged:
        lines += [
            "**New, Altered, and Removed DSDs:**",
            "",
            "| Status | Code | DSD | District | Pop 2012 | Pop 2024 | Pop Change |",
            "|---|---|---|---|---:|---:|---:|",
        ]
        for row in sorted(
            flagged, key=lambda r: (r["district"], {"Removed": 0, "Altered": 1, "New": 2}.get(r["status"], 3), r["dsd"])
        ):
            pop_2012 = (
                f"{row['total_2012']:,}"
                if row["total_2012"] is not None
                else "—"
            )
            pop_2024 = (
                f"{row['total_2024']:,}"
                if row["total_2024"] is not None
                else "—"
            )
            pop_chg = (
                f"{row['pop_change_pct']:+.1f}%"
                if row["pop_change_pct"] is not None
                else "—"
            )
            lines.append(
                f"| {row['status']} | {row['dsd_code']} | {row['dsd']} | {row['district']} "
                f"| {pop_2012} | {pop_2024} | {pop_chg} |"
            )

    return "\n".join(lines)
