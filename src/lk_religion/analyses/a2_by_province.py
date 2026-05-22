from gig import EntType

from lk_religion.analyses.by_entity import default_spec, run_by_entity


def run():
    return run_by_entity(
        default_spec(
            'a2-religion-by-province-key-trends',
            'A2',
            'Religion by Province: Key Trends',
            'A2 province change maps',
            'Province',
            'Provinces',
            'province-level',
            EntType.PROVINCE,
            'province_code',
            'province',
            'religion_by_province',
        )
    )
