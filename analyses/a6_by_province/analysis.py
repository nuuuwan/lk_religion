import sys
from pathlib import Path

from gig import EntType

ANALYSIS_DIR = Path(__file__).resolve().parent
SRC_DIR = ANALYSIS_DIR.parents[1] / 'src'
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lk_religion.religion_by_region import RegionAnalysisConfig, run_religion_by_region


def run():
    return run_religion_by_region(
        RegionAnalysisConfig(
            analysis_dir=ANALYSIS_DIR,
            analysis_key='A6',
            analysis_heading='Religion by Province: Key Trends',
            image_alt='A6 province change maps',
            region_singular='Province',
            region_plural='Provinces',
            region_level_label='province-level',
            entity_type=EntType.PROVINCE,
            code_key='province_code',
            name_key='province',
            data_2012_path=ANALYSIS_DIR / 'religion_by_province_2012.json',
            data_2024_path=ANALYSIS_DIR / 'religion_by_province_2024.json',
            analysis_json_path=ANALYSIS_DIR / 'religion_by_province_analysis.json',
            readme_path=ANALYSIS_DIR / 'README.md',
            chart_path=ANALYSIS_DIR / 'chart.png',
            low_population_threshold=None,
            table_min_abs_pp=1.0,
            map_white_abs_pp_threshold=0.01,
        )
    )
