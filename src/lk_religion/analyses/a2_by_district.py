from gig import EntType

from lk_religion.analyses.by_entity import default_spec, run_by_entity


def run():
    return run_by_entity(
        default_spec(
            'a2_by_district',
            'A2',
            'Religion by District: Key Trends',
            'A2 district change maps',
            'District',
            'Districts',
            'district-level',
            EntType.DISTRICT,
            'district_code',
            'district',
            'religion_by_district',
        )
    )
