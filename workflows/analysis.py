from pathlib import Path
import re

ROOT_DIR = Path(__file__).resolve().parents[1]
README_PATH = ROOT_DIR / 'README.md'
ANALYSIS_DIRS = [
    ROOT_DIR / 'analyses' / 'a1_national_totals',
    ROOT_DIR / 'analyses' / 'a2_by_district',
    ROOT_DIR / 'analyses' / 'a4_by_dsd',
    ROOT_DIR / 'analyses' / 'a5_proportion_change_by_dsd',
]


IMAGE_PATTERN = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')


def _rewrite_relative_image_paths(content, analysis_dir):
    analysis_path = analysis_dir.relative_to(ROOT_DIR).as_posix()

    def repl(match):
        alt_text, raw_target = match.groups()
        parts = raw_target.strip().split(maxsplit=1)
        target = parts[0].strip('<>')
        suffix = f' {parts[1]}' if len(parts) > 1 else ''
        if (
            target.startswith(('http://', 'https://', '/', '#', 'data:'))
            or '://' in target
        ):
            return match.group(0)
        rewritten_target = f'{analysis_path}/{target}'
        if raw_target.startswith('<') and raw_target.endswith('>'):
            rewritten_target = f'<{rewritten_target}>'
        return f'![{alt_text}]({rewritten_target}{suffix})'

    return IMAGE_PATTERN.sub(repl, content)


def _read_child_readme(analysis_dir):
    content = (analysis_dir / 'README.md').read_text().strip()
    if content.endswith('\n---'):
        content = content[:-4].rstrip()
    elif content.endswith('---'):
        content = content[:-3].rstrip()
    return _rewrite_relative_image_paths(content, analysis_dir)


sections = [_read_child_readme(analysis_dir) for analysis_dir in ANALYSIS_DIRS]

readme_content = (
    '# lk_religion\n\n'
    "Analyses of Sri Lanka's religious demographics, comparing the **2012 Census** and **2024 Census**.\n\n"
    'Each analysis now lives in its own folder under [`analyses/`](analyses/), together with its own README, workflow script, and related data files. '
    'The sections below are copied from those child READMEs.\n\n'
    '- [`analyses/a1_national_totals/`](analyses/a1_national_totals/)\n'
    '- [`analyses/a2_by_district/`](analyses/a2_by_district/)\n'
    '- [`analyses/a4_by_dsd/`](analyses/a4_by_dsd/)\n'
    '- [`analyses/a5_proportion_change_by_dsd/`](analyses/a5_proportion_change_by_dsd/)\n\n'
    '---\n\n'
    + '\n\n---\n\n'.join(sections)
    + '\n\n---\n\n'
    '*Data from the 2012 and 2024 Sri Lanka Census, accessed via '
    '[lanka_data](https://pypi.org/project/lanka-data/). '
    'Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*\n'
)

README_PATH.write_text(readme_content)
