from gig import EntType

from lk_religion.analyses.by_entity import default_spec, run_by_entity


def run():
    return run_by_entity(default_spec(2, EntType.PROVINCE))
