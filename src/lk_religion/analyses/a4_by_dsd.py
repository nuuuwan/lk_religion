from gig import Ent, EntType

from lk_religion.analyses.by_entity import default_spec, run_by_entity

RECENT_CHANGE_DSD_STATUS = {
    'LK-2303': 'Revised',
    'LK-2304': 'New',
    'LK-2306': 'Revised',
    'LK-2307': 'New',
    'LK-2309': 'Revised',
    'LK-2310': 'New',
    'LK-2312': 'Revised',
    'LK-2313': 'New',
    'LK-2315': 'Revised',
    'LK-2316': 'New',
    'LK-3127': 'Revised',
    'LK-3128': 'New',
    'LK-3136': 'Revised',
    'LK-3137': 'New',
    'LK-3138': 'New',
    'LK-5221': 'Revised',
    'LK-5224': 'Removed',
    'LK-9118': 'Revised',
    'LK-9119': 'New',
}


def _ignored_recent_change_text():
    status_codes = {}
    for code, status in RECENT_CHANGE_DSD_STATUS.items():
        status_codes.setdefault(status, []).append(code)
    parts = []
    for status in ('Revised', 'New', 'Removed'):
        codes = sorted(status_codes.get(status, []))
        if not codes:
            continue
        parts.append(f'**{status}**: {", ".join(codes)}')
    return (
        '*DSDs with legal recent administrative changes are ignored from analysis '
        '(from `nuuuwan/lk_admin_regions/README.recent-changes.md`). '
        + ' · '.join(parts)
        + '.*'
    )


def run():
    spec = default_spec(4, EntType.DSD)
    spec = spec.__class__(
        **{
            **spec.__dict__,
            'label_top_n': 0,
            'print_row_limit': 25,
            'extra_text': _ignored_recent_change_text(),
            'extra_row_data': lambda code: {'district': Ent.from_id(code[:5]).name},
            'excluded_codes': frozenset(RECENT_CHANGE_DSD_STATUS),
            'map_grey_codes': frozenset(RECENT_CHANGE_DSD_STATUS),
            'map_grey_label': (
                'recent legal admin changes '
                '(revised/new/removed DSD IDs from lk_admin_regions)'
            ),
            'extra_columns': (('district', 'District'),),
        }
    )
    return run_by_entity(spec)
