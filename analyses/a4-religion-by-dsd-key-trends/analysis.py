import sys
from pathlib import Path

ANALYSIS_DIR = Path(__file__).resolve().parent
SRC_DIR = ANALYSIS_DIR.parents[1] / 'src'
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lk_religion.analyses.a4_by_dsd import run  # noqa: E402,F401


if __name__ == '__main__':
    run()
