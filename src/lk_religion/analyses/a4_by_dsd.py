import json
from pathlib import Path

from gig import Ent, EntType

from lk_religion.analyses.by_entity import default_spec, run_by_entity


ROOT_DIR = Path(__file__).resolve().parents[3]
BOUNDARY_ANALYSIS_PATH = (
    ROOT_DIR / 'analyses' / 'a4-religion-by-dsd-key-trends' / 'dsd_boundary_analysis.json'
)


def run():
    boundary_analysis = json.loads(BOUNDARY_ANALYSIS_PATH.read_text())
    spec = default_spec(
        'a4-religion-by-dsd-key-trends',
        'A4',
        'Religion by DSD: Key Trends',
        'A4 DSD change maps',
        'DSD',
        'DSDs',
        'DSD-level',
        EntType.DSD,
        'dsd_code',
        'dsd',
        'religion_by_dsd',
    )
    spec = spec.__class__(
        **{
            **spec.__dict__,
            'label_top_n': 0,
            'print_row_limit': 25,
            'extra_text': '*New, removed, and altered DSDs are excluded to avoid boundary-change artifacts.*',
            'extra_row_data': lambda code: {'district': Ent.from_id(code[:5]).name},
            'excluded_codes': frozenset(row['dsd_code'] for row in boundary_analysis['flagged']),
            'extra_columns': (('district', 'District'),),
        }
    )
    return run_by_entity(spec)
