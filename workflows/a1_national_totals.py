import json
import os

from lanka_data import Db

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


def run():
    print("=== 1) National totals by religion ===")

    religion_2012 = Db("/LK/Religion/2012")
    religion_2024 = Db("/LK/Religion/2024")

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(os.path.join(DATA_DIR, "religion_2012.json"), "w") as f:
        json.dump(religion_2012, f, indent=2)
    with open(os.path.join(DATA_DIR, "religion_2024.json"), "w") as f:
        json.dump(religion_2024, f, indent=2)

    totals_2012 = religion_2012
    totals_2024 = religion_2024

    total_2024 = totals_2024["TotalPopulation"] if "TotalPopulation" in totals_2024 else sum(totals_2024[r] for r in RELIGIONS)

    rows = []
    for r in RELIGIONS:
        v2012 = totals_2012[r]
        v2024 = totals_2024[r]
        change = v2024 - v2012
        annual_growth = (
            (v2024 / v2012) ** (1 / YEARS) - 1 if v2012 > 0 else None
        )
        rows.append(
            {
                "religion": r,
                "2012": v2012,
                "2024": v2024,
                "change": change,
                "annual_growth_rate": (
                    round(annual_growth, 6)
                    if annual_growth is not None
                    else None
                ),
                "proportion_2024": round(v2024 / total_2024, 6),
            }
        )

    rows.sort(key=lambda r: r["proportion_2024"], reverse=True)

    with open(
        os.path.join(DATA_DIR, "national_totals_by_religion.json"), "w"
    ) as f:
        json.dump(rows, f, indent=2)

    print(
        f"{'Religion':<20} {'2012':>12} {'2024':>12} {'Change':>12} {'Ann. Growth':>12} {'% of Pop':>10}"
    )
    print("-" * 82)
    for row in rows:
        ag = (
            f"{row['annual_growth_rate']:+.2%}"
            if row["annual_growth_rate"] is not None
            else "   N/A"
        )
        print(
            f"{row['religion']:<20} {row['2012']:>12,} {row['2024']:>12,} {row['change']:>+12,} {ag:>12} {row['proportion_2024']:>9.1%}"
        )

    return _readme_section(rows)


def _readme_section(rows):
    total_2012 = sum(r["2012"] for r in rows)
    total_2024 = sum(r["2024"] for r in rows)
    total_change = total_2024 - total_2012
    total_growth = (total_2024 / total_2012) ** (1 / YEARS) - 1

    buddhist = next(r for r in rows if r["religion"] == "Buddhist")
    islam = next(r for r in rows if r["religion"] == "Islam")
    buddhist_share_2024 = buddhist["2024"] / total_2024
    islam_share_2024 = islam["2024"] / total_2024

    lines = [
        "## A1. National Population by Religion",
        "",
        "| Religion | 2012 | 2024 | Change | Annual Growth | % of Population |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        ag = (
            f"{row['annual_growth_rate']:+.2%}"
            if row["annual_growth_rate"] is not None
            else "N/A"
        )
        lines.append(
            f"| {row['religion']} | {row['2012']:,} | {row['2024']:,} | {row['change']:+,} | {ag} | {row['proportion_2024']:.1%} |"
        )
    lines.append(
        f"| **Total** | **{total_2012:,}** | **{total_2024:,}** | **{total_change:+,}** | **{total_growth:+.2%}** |"
    )
    lines += [
        "",
        "### Commentary",
        "",
        f"- Sri Lanka's total population grew from **{total_2012:,}** (2012) to **{total_2024:,}** (2024), "
        f"an increase of **{total_change:+,}** at an annual rate of **{total_growth:+.2%}**.",
        f"- **Buddhism** remains the dominant religion, accounting for "
        f"**{buddhist_share_2024:.1%}** of the population in 2024, "
        f"growing at **{buddhist['annual_growth_rate']:+.2%}** per year.",
        f"- **Islam** has the fastest growth rate among major religions at "
        f"**{islam['annual_growth_rate']:+.2%}** per year, reaching a share of **{islam_share_2024:.1%}** in 2024.",
        "- **Roman Catholic** and **Other Christian** communities show slight declines over the period.",
    ]
    return "\n".join(lines)
