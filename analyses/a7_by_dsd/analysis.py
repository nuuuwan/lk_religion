import sys
import json
from pathlib import Path

from gig import Ent, EntType

ANALYSIS_DIR = Path(__file__).resolve().parent
SRC_DIR = ANALYSIS_DIR.parents[1] / 'src'
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lk_religion.religion_by_region import RegionAnalysisConfig, run_religion_by_region


def run():
    with open(
        ANALYSIS_DIR.parents[0] / 'a4_by_dsd' / 'religion_by_dsd_analysis.json'
    ) as f:
        boundary_analysis = json.load(f)
    return run_religion_by_region(
        RegionAnalysisConfig(
            analysis_dir=ANALYSIS_DIR,
            analysis_key='A7',
            analysis_heading='Religion by DSD: Key Trends',
            image_alt='A7 DSD change maps',
            region_singular='DSD',
            region_plural='DSDs',
            region_level_label='DSD-level',
            entity_type=EntType.DSD,
            code_key='dsd_code',
            name_key='dsd',
            data_2012_path=ANALYSIS_DIR / 'religion_by_dsd_2012.json',
            data_2024_path=ANALYSIS_DIR / 'religion_by_dsd_2024.json',
            analysis_json_path=ANALYSIS_DIR / 'religion_by_dsd_analysis.json',
            readme_path=ANALYSIS_DIR / 'README.md',
            chart_path=ANALYSIS_DIR / 'chart.png',
            label_top_n=0,
            print_row_limit=25,
            extra_text='*New, removed, and altered DSDs from A4 are excluded to avoid boundary-change artifacts.*',
            extra_row_data=lambda code: {'district': Ent.from_id(code[:5]).name},
            excluded_codes=frozenset(
                row['dsd_code'] for row in boundary_analysis['flagged']
            ),
            extra_columns=(('district', 'District'),),
        )
    )
