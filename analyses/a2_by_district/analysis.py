import sys
from pathlib import Path

from gig import EntType

ANALYSIS_DIR = Path(__file__).resolve().parent
SRC_DIR = ANALYSIS_DIR.parents[1] / 'src'
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lk_religion.religion_by_region import (
    RegionAnalysisConfig,
    run_religion_by_region,
)


def run():
    return run_religion_by_region(
        RegionAnalysisConfig(
            analysis_dir=ANALYSIS_DIR,
            analysis_key='A2',
            analysis_heading='Religion by District: Key Trends',
            image_alt='A2 district change maps',
            region_singular='District',
            region_plural='Districts',
            region_level_label='district-level',
            entity_type=EntType.DISTRICT,
            code_key='district_code',
            name_key='district',
            data_2012_path=ANALYSIS_DIR / 'religion_by_district_2012.json',
            data_2024_path=ANALYSIS_DIR / 'religion_by_district_2024.json',
            analysis_json_path=ANALYSIS_DIR / 'religion_by_district_analysis.json',
            readme_path=ANALYSIS_DIR / 'README.md',
            chart_path=ANALYSIS_DIR / 'chart.png',
        )
    )
