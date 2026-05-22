import json
from dataclasses import dataclass
from pathlib import Path

import geopandas as gpd
import pandas as pd
from gig import Ent, EntType

from lk_religion.common.RegionAnalysis import (
    RegionAnalysisConfig,
    run_religion_by_region,
)


@dataclass(frozen=True)
class ByEntityAnalysisSpec:
    analysis_dir: Path
    analysis_key: str
    analysis_heading: str
    image_alt: str
    region_singular: str
    region_plural: str
    region_level_label: str
    entity_type: object
    code_key: str
    name_key: str
    data_prefix: str
    low_population_threshold: int | None = None
    table_min_abs_pp: float | None = 1.0
    map_white_abs_pp_threshold: float | None = 0.01
    label_top_n: int | None = None
    print_row_limit: int | None = None
    extra_text: str | None = None
    extra_row_data: object | None = None
    excluded_codes: frozenset[str] = frozenset()
    extra_columns: tuple[tuple[str, str], ...] = tuple()
    data_loader: object | None = None
    geometry_loader: object | None = None


def get_default_entity_meta(entity_type):
    if entity_type == EntType.COUNTRY:
        return {
            'slug': 'country',
            'region_singular': 'Country',
            'region_plural': 'Countries',
            'region_level_label': 'country-level',
            'code_key': 'country_code',
            'name_key': 'country',
        }
    if entity_type == EntType.PROVINCE:
        return {
            'slug': 'province',
            'region_singular': 'Province',
            'region_plural': 'Provinces',
            'region_level_label': 'province-level',
            'code_key': 'province_code',
            'name_key': 'province',
        }
    if entity_type == EntType.DISTRICT:
        return {
            'slug': 'district',
            'region_singular': 'District',
            'region_plural': 'Districts',
            'region_level_label': 'district-level',
            'code_key': 'district_code',
            'name_key': 'district',
        }
    if entity_type == EntType.DSD:
        return {
            'slug': 'dsd',
            'region_singular': 'DSD',
            'region_plural': 'DSDs',
            'region_level_label': 'DSD-level',
            'code_key': 'dsd_code',
            'name_key': 'dsd',
        }
    raise ValueError(f'Unsupported entity type: {entity_type}')


def load_country_data(_config):
    try:
        from lanka_data import Db

        data_2012 = Db('/LK/Religion/2012')
        data_2024 = Db('/LK/Religion/2024')
    except Exception:
        root_dir = Path(__file__).resolve().parents[3]
        a1_dir = root_dir / 'analyses' / 'a0-national-population-by-religion'
        data_2012 = json.loads((a1_dir / 'religion_2012.json').read_text())
        data_2024 = json.loads((a1_dir / 'religion_2024.json').read_text())

    return {'LK': data_2012}, {'LK': data_2024}


def load_country_geometry(config):
    provinces = Ent.list_from_type(EntType.PROVINCE)
    gdfs = []
    for prov in provinces:
        gdf = prov.geo().copy()
        gdfs.append(gdf[['geometry']])
    combined = gpd.GeoDataFrame(
        pd.concat(gdfs, ignore_index=True),
        geometry='geometry',
        crs=gdfs[0].crs,
    )
    country_gdf = combined.dissolve().reset_index(drop=True)
    country_gdf[config.code_key] = 'LK'
    country_gdf[config.name_key] = 'Sri Lanka'
    return {'LK': 'Sri Lanka'}, country_gdf[[config.code_key, config.name_key, 'geometry']]


def run_by_entity(spec: ByEntityAnalysisSpec):
    return run_religion_by_region(
        RegionAnalysisConfig(
            analysis_dir=spec.analysis_dir,
            analysis_key=spec.analysis_key,
            analysis_heading=spec.analysis_heading,
            image_alt=spec.image_alt,
            region_singular=spec.region_singular,
            region_plural=spec.region_plural,
            region_level_label=spec.region_level_label,
            entity_type=spec.entity_type,
            code_key=spec.code_key,
            name_key=spec.name_key,
            data_2012_path=spec.analysis_dir / f'{spec.data_prefix}_2012.json',
            data_2024_path=spec.analysis_dir / f'{spec.data_prefix}_2024.json',
            analysis_json_path=spec.analysis_dir / f'{spec.data_prefix}_analysis.json',
            readme_path=spec.analysis_dir / 'README.md',
            chart_path=spec.analysis_dir / 'chart.png',
            low_population_threshold=spec.low_population_threshold,
            table_min_abs_pp=spec.table_min_abs_pp,
            map_white_abs_pp_threshold=spec.map_white_abs_pp_threshold,
            label_top_n=spec.label_top_n,
            print_row_limit=spec.print_row_limit,
            extra_text=spec.extra_text,
            extra_row_data=spec.extra_row_data,
            excluded_codes=spec.excluded_codes,
            extra_columns=spec.extra_columns,
            data_loader=spec.data_loader,
            geometry_loader=spec.geometry_loader,
        )
    )


def default_spec(analysis_number: int, entity_type):
    entity_meta = get_default_entity_meta(entity_type)
    analysis_key = f'A{analysis_number}'
    analysis_slug = f'a{analysis_number}-religion-by-{entity_meta["slug"]}-key-trends'
    root_dir = Path(__file__).resolve().parents[3]
    analysis_dir = root_dir / 'analyses' / analysis_slug
    return ByEntityAnalysisSpec(
        analysis_dir=analysis_dir,
        analysis_key=analysis_key,
        analysis_heading=f'Religion by {entity_meta["region_singular"]}: Key Trends',
        image_alt=f'{analysis_key} {entity_meta["region_singular"]} change maps',
        region_singular=entity_meta['region_singular'],
        region_plural=entity_meta['region_plural'],
        region_level_label=entity_meta['region_level_label'],
        entity_type=entity_type,
        code_key=entity_meta['code_key'],
        name_key=entity_meta['name_key'],
        data_prefix=f'religion_by_{entity_meta["slug"]}',
    )
