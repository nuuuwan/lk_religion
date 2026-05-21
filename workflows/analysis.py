from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
README_PATH = ROOT_DIR / 'README.md'
ANALYSIS_DIRS = [
    ROOT_DIR / 'analyses' / 'a1_national_totals',
    ROOT_DIR / 'analyses' / 'a2_by_district',
    ROOT_DIR / 'analyses' / 'a3_proportion_change',
    ROOT_DIR / 'analyses' / 'a4_by_dsd',
]


def _read_child_readme(analysis_dir):
    content = (analysis_dir / 'README.md').read_text().strip()
    if content.endswith('\n---'):
        content = content[:-4].rstrip()
    elif content.endswith('---'):
        content = content[:-3].rstrip()
    return content


sections = [_read_child_readme(analysis_dir) for analysis_dir in ANALYSIS_DIRS]

readme_content = (
    '# lk_religion\n\n'
    "Analyses of Sri Lanka's religious demographics, comparing the **2012 Census** and **2024 Census**.\n\n"
    'Each analysis now lives in its own folder under [`analyses/`](analyses/), together with its own README, workflow script, and related data files. '
    'The sections below are copied from those child READMEs.\n\n'
    '- [`analyses/a1_national_totals/`](analyses/a1_national_totals/)\n'
    '- [`analyses/a2_by_district/`](analyses/a2_by_district/)\n'
    '- [`analyses/a3_proportion_change/`](analyses/a3_proportion_change/)\n'
    '- [`analyses/a4_by_dsd/`](analyses/a4_by_dsd/)\n\n'
    + '\n\n---\n\n'.join(sections)
    + '\n\n---\n\n'
    '*Data from the 2012 and 2024 Sri Lanka Census, accessed via '
    '[lanka_data](https://pypi.org/project/lanka-data/). '
    'Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*\n'
)

README_PATH.write_text(readme_content)
