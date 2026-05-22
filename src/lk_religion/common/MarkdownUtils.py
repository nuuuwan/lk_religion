import re
from pathlib import Path

IMAGE_PATTERN = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')


def write_markdown(path: Path, content: str):
    path.write_text(content.rstrip() + '\n')
    return content


def rewrite_relative_image_paths(content: str, analysis_dir: Path, root_dir: Path):
    analysis_path = analysis_dir.relative_to(root_dir).as_posix()

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


def read_child_readme(analysis_dir: Path, root_dir: Path):
    content = (analysis_dir / 'README.md').read_text().strip()
    if content.endswith('\n---'):
        content = content[:-4].rstrip()
    elif content.endswith('---'):
        content = content[:-3].rstrip()
    return rewrite_relative_image_paths(content, analysis_dir, root_dir)
