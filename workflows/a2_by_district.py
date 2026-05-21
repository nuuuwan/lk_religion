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
YEARS = 2024 - 2012
SIGNIFICANT_THRESHOLD = 0.01  # 1% of national total
MIN_ABSOLUTE = 1000  # minimum absolute count


def run():
    print("=== 2) By-district analysis per religion ===")

    db2012 = Db("/LK:Districts/Religion/2012")
    db2024 = Db("/LK:Districts/Religion/2024")
    national2024 = Db("/LK/Religion/2024")

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(
        os.path.join(DATA_DIR, "religion_by_district_2012.json"), "w"
    ) as f:
        json.dump(db2012, f, indent=2)
    with open(
        os.path.join(DATA_DIR, "religion_by_district_2024.json"), "w"
    ) as f:
        json.dump(db2024, f, indent=2)

    rn = RegionNames()

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
                    "district_code": code,
                    "district": rn.name_for(code),
                    "2012": v2012,
                    "2024": v2024,
                    "change": change,
                    "annual_growth_rate": (
                        round(annual_growth, 6)
                        if annual_growth is not None
                        else None
                    ),
                    "proportion_national": (
                        round(v2024 / national2024[religion], 6)
                        if national2024[religion] > 0
                        else 0
                    ),
                }
            )

        rows.sort(
            key=lambda r: r["proportion_national"],
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
                    "district_code": None,
                    "district": "Other (<1% or <1,000)",
                    "2012": other_2012,
                    "2024": other_2024,
                    "change": other_change,
                    "annual_growth_rate": (
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
        print("  " + "-" * 72)
        for row in rows:
            ag = (
                f"{row['annual_growth_rate']:+.2%}"
                if row["annual_growth_rate"] is not None
                else "N/A"
            )
            pn = (
                f"{row['proportion_national']:.1%}"
                if row.get("proportion_national") is not None
                else ""
            )
            print(
                f"  {row['district']:<16} {row['2012']:>10,} {row['2024']:>10,} {row['change']:>+10,} {ag:>12} {pn:>10}"
            )

    with open(
        os.path.join(DATA_DIR, "religion_by_district_analysis.json"), "w"
    ) as f:
        json.dump(results, f, indent=2)

    return _readme_section(results)


def _readme_section(results):
    lines = ["## A2. Religion by District: Key Trends", ""]

    for religion, rows in results.items():
        if not rows:
            continue

        significant_rows = [r for r in rows if r["district_code"] is not None]
        other_row = next((r for r in rows if r["district_code"] is None), None)

        if not significant_rows:
            continue

        fastest_growing = significant_rows[0]
        fastest_declining = significant_rows[-1]
        largest_absolute = max(significant_rows, key=lambda r: r["change"])

        lines += [
            f"### {religion}",
            "",
            f"| District | 2012 | 2024 | Change | Annual Growth | % of Natl |",
            f"|---|---:|---:|---:|---:|---:|",
        ]
        for row in significant_rows:
            ag = (
                f"{row['annual_growth_rate']:+.2%}"
                if row["annual_growth_rate"] is not None
                else "N/A"
            )
            pn = (
                f"{row['proportion_national']:.1%}"
                if row.get("proportion_national") is not None
                else ""
            )
            lines.append(
                f"| {row['district']} | {row['2012']:,} | {row['2024']:,} | {row['change']:+,} | {ag} | {pn} |"
            )
        if other_row:
            ag = (
                f"{other_row['annual_growth_rate']:+.2%}"
                if other_row["annual_growth_rate"] is not None
                else "N/A"
            )
            lines.append(
                f"| *{other_row['district']}* | *{other_row['2012']:,}* | *{other_row['2024']:,}* | *{other_row['change']:+,}* | *{ag}* | |"
            )

        highlights = []
        if (
            fastest_growing["annual_growth_rate"]
            and fastest_growing["annual_growth_rate"] > 0
        ):
            highlights.append(
                f"**{fastest_growing['district']}** grew fastest at "
                f"**{fastest_growing['annual_growth_rate']:+.2%}/yr**."
            )
        if (
            fastest_declining["annual_growth_rate"]
            and fastest_declining["annual_growth_rate"] < 0
        ):
            highlights.append(
                f"**{fastest_declining['district']}** saw the steepest decline at "
                f"**{fastest_declining['annual_growth_rate']:+.2%}/yr**."
            )
        elif fastest_declining != fastest_growing:
            highlights.append(
                f"**{fastest_declining['district']}** had the slowest growth at "
                f"**{fastest_declining['annual_growth_rate']:+.2%}/yr**."
            )
        if (
            largest_absolute != fastest_growing
            and largest_absolute["change"] > 0
        ):
            highlights.append(
                f"**{largest_absolute['district']}** had the largest absolute increase "
                f"(**{largest_absolute['change']:+,}**)."
            )

        if highlights:
            lines += ["", "*" + " ".join(highlights) + "*"]

        lines.append("")

    return "\n".join(lines)
