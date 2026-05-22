from gig import EntType

from lk_religion.analyses.by_entity import (
    ByEntityAnalysisSpec,
    default_spec,
    load_country_data,
    load_country_geometry,
    run_by_entity,
)


def run():
    spec = default_spec(1, EntType.COUNTRY)
    spec = ByEntityAnalysisSpec(
        **{
            **spec.__dict__,
            'data_loader': load_country_data,
            'geometry_loader': load_country_geometry,
            'low_population_threshold': None,
            'map_white_abs_pp_threshold': 0.01,
            'extra_row_data': lambda _code: {'country': 'Sri Lanka'},
        }
    )
    return run_by_entity(spec)
