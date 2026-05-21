import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import a1_national_totals
import a2_by_district

README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")

# --- Run analyses ---
sections = [
    a1_national_totals.run(),
    a2_by_district.run(),
]

# --- Write README ---
readme_content = (
    "# lk_religion\n\n"
    "Analyses of Sri Lanka's religious demographics, comparing the **2012 Census** and **2024 Census**.\n\n"
    + "\n\n---\n\n".join(sections)
    + "\n\n---\n\n"
    "*Data from the 2012 and 2024 Sri Lanka Census, accessed via "
    "[lanka_data](https://pypi.org/project/lanka-data/). "
    "Raw data and derived tables are in [`data/`](data/).*\n"
)

with open(README_PATH, "w") as f:
    f.write(readme_content)
