import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / 'src'
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lk_religion.analyses.a0_national_totals import run as run_a0
from lk_religion.analyses.a1_by_country import run as run_a1
from lk_religion.analyses.a2_by_province import run as run_a2
from lk_religion.analyses.a3_by_district import run as run_a3
from lk_religion.analyses.a4_by_dsd import run as run_a4
from lk_religion.common.MarkdownUtils import read_child_readme, write_markdown

README_PATH = ROOT_DIR / 'README.md'
ANALYSIS_DIRS = [
    ROOT_DIR / 'analyses' / 'a0-national-population-by-religion',
    ROOT_DIR / 'analyses' / 'a1-religion-by-country-key-trends',
    ROOT_DIR / 'analyses' / 'a2-religion-by-province-key-trends',
    ROOT_DIR / 'analyses' / 'a3-religion-by-district-key-trends',
    ROOT_DIR / 'analyses' / 'a4-religion-by-dsd-key-trends',
]


def compile_root_readme():
    sections = [read_child_readme(analysis_dir, ROOT_DIR) for analysis_dir in ANALYSIS_DIRS]

    readme_content = (
        '# lk_religion\n\n'
        "Analyses of Sri Lanka's religious demographics, comparing the **2012 Census** and **2024 Census**.\n\n"
        'Each analysis now lives in its own folder under [`analyses/`](analyses/), together with its own README, workflow script, and related data files. '
        'The sections below are copied from those child READMEs.\n\n'
        '- [`analyses/a0-national-population-by-religion/`](analyses/a0-national-population-by-religion/)\n'
        '- [`analyses/a1-religion-by-country-key-trends/`](analyses/a1-religion-by-country-key-trends/)\n'
        '- [`analyses/a2-religion-by-province-key-trends/`](analyses/a2-religion-by-province-key-trends/)\n'
        '- [`analyses/a3-religion-by-district-key-trends/`](analyses/a3-religion-by-district-key-trends/)\n'
        '- [`analyses/a4-religion-by-dsd-key-trends/`](analyses/a4-religion-by-dsd-key-trends/)\n\n'
        '---\n\n'
        + '\n\n---\n\n'.join(sections)
        + '\n\n---\n\n'
        '*Data from the 2012 and 2024 Sri Lanka Census, accessed via '
        '[lanka_data](https://pypi.org/project/lanka-data/). '
        'Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*\n'
    )
    return write_markdown(README_PATH, readme_content)


def run():
    run_a0()
    run_a1()
    run_a2()
    run_a3()
    run_a4()
    return compile_root_readme()


if __name__ == '__main__':
    run()
