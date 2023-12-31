from typing import Any

import haversine
from geolib import geohash as gh
from sqlalchemy.sql import text

from ..exceptions import BadRequestException
from ..utils import create_geohash
from .. import db
from .models import GeoSpatialModel

RADIUS_GEOHASH_PRECISION_MAP = {0.5: 6, 1: 5, 2: 5, 5: 4, 20: 4}
FETCH_NEARBY_SERVICE_SQL_QUERY = (
    "SELECT id, geohash, type, address, city, state, country, latitude, longitude FROM "
    + '"Business"'
    + " INNER JOIN"
    + " geo_spatial ON id=geo_spatial.business_id"
    + " where geo_spatial.geohash like :geohash AND type=:business_type;"
)


def _get_geohash_neighbors(geohash: str) -> list[str]:
    return list(gh.neighbours(geohash))


def _fetch_nearby_services(
    geohash_search_space: list[str], service_type: str = "SHOPPING MALL"
) -> list[dict[str, Any]]:
    nearby_services = []
    for geohash in geohash_search_space:
        query_result_iter = db.session.execute(
            text(FETCH_NEARBY_SERVICE_SQL_QUERY),
            {"geohash": f"{geohash}%", "business_type": f"{service_type}"},
        )
        for query_r in query_result_iter:
            nearby_services.append(query_r._asdict())
    return nearby_services


def _rank_by_distance(
    nearby_services: list[dict[str, Any]], *args
) -> list[dict[str, Any]]:
    nearby_services.sort(
        key=lambda x: haversine.haversine(args, (x["latitude"], x["longitude"]))
    )
    return nearby_services


def get_nearby_locations(
    latitude: float, longitude: float, radius: int
) -> list[dict[str, Any]]:
    geohash_search_space = []
    try:
        geohash_precision = RADIUS_GEOHASH_PRECISION_MAP[radius]
    except KeyError as exp:
        raise BadRequestException from exp
    geohash = create_geohash(latitude, longitude, geohash_precision)
    geohash_neighbors = _get_geohash_neighbors(geohash)
    geohash_search_space.append(geohash)
    geohash_search_space.extend(geohash_neighbors)
    nearby_services = _fetch_nearby_services(geohash_search_space)
    return _rank_by_distance(nearby_services, latitude, longitude)


def add_business_in_geo_spatial_model(
    business_id: str, latitude: float, longitude: float
):
    geohash = create_geohash(latitude, longitude, geohash_precision=6)
    db.session.add(GeoSpatialModel(geohash=geohash, business_id=business_id))
    db.session.commit()
