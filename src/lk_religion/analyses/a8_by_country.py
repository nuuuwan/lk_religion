from gig import EntType

from lk_religion.analyses.by_entity import (
    ByEntityAnalysisSpec,
    default_spec,
    load_country_data,
    run_by_entity,
)


def run():
    spec = default_spec(
        'a8_by_country',
        'A8',
        'Religion by Country: Key Trends',
        'A8 country change maps',
        'Country',
        'Countries',
        'country-level',
        EntType.COUNTRY,
        'country_code',
        'country',
        'religion_by_country',
    )
    spec = ByEntityAnalysisSpec(
        **{
            **spec.__dict__,
            'data_loader': load_country_data,
            'low_population_threshold': None,
            'map_white_abs_pp_threshold': 0.01,
            'extra_row_data': lambda _code: {'country': 'Sri Lanka'},
        }
    )
    return run_by_entity(spec)
