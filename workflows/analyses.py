import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / 'src'
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lk_religion.analyses.a1_national_totals import run as run_a1
from lk_religion.analyses.a2_by_district import run as run_a2
from lk_religion.analyses.a3_proportion_change import run as run_a3
from lk_religion.analyses.a4_by_dsd import run as run_a4
from lk_religion.analyses.a5_proportion_change_by_dsd import run as run_a5
from lk_religion.analyses.a6_by_province import run as run_a6
from lk_religion.analyses.a7_by_dsd import run as run_a7
from lk_religion.analyses.a8_by_country import run as run_a8
from lk_religion.common.MarkdownUtils import read_child_readme, write_markdown

README_PATH = ROOT_DIR / 'README.md'
ANALYSIS_DIRS = [
    ROOT_DIR / 'analyses' / 'a1_national_totals',
    ROOT_DIR / 'analyses' / 'a2_by_district',
    ROOT_DIR / 'analyses' / 'a4_by_dsd',
    ROOT_DIR / 'analyses' / 'a6_by_province',
    ROOT_DIR / 'analyses' / 'a7_by_dsd',
    ROOT_DIR / 'analyses' / 'a8_by_country',
]


def compile_root_readme():
    sections = [read_child_readme(analysis_dir, ROOT_DIR) for analysis_dir in ANALYSIS_DIRS]

    readme_content = (
        '# lk_religion\n\n'
        "Analyses of Sri Lanka's religious demographics, comparing the **2012 Census** and **2024 Census**.\n\n"
        'Each analysis now lives in its own folder under [`analyses/`](analyses/), together with its own README, workflow script, and related data files. '
        'The sections below are copied from those child READMEs.\n\n'
        '- [`analyses/a1_national_totals/`](analyses/a1_national_totals/)\n'
        '- [`analyses/a2_by_district/`](analyses/a2_by_district/)\n'
        '- [`analyses/a4_by_dsd/`](analyses/a4_by_dsd/)\n'
        '- [`analyses/a6_by_province/`](analyses/a6_by_province/)\n'
        '- [`analyses/a7_by_dsd/`](analyses/a7_by_dsd/)\n'
        '- [`analyses/a8_by_country/`](analyses/a8_by_country/)\n\n'
        '---\n\n'
        + '\n\n---\n\n'.join(sections)
        + '\n\n---\n\n'
        '*Data from the 2012 and 2024 Sri Lanka Census, accessed via '
        '[lanka_data](https://pypi.org/project/lanka-data/). '
        'Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*\n'
    )
    return write_markdown(README_PATH, readme_content)


def run():
    run_a1()
    run_a2()
    run_a3()
    run_a4()
    run_a5()
    run_a6()
    run_a7()
    run_a8()
    return compile_root_readme()


if __name__ == '__main__':
    run()
