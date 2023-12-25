from geolib import geohash as gh


def create_geohash(latitude: float, longitude: float, geohash_precision: int) -> str:
    return gh.encode(latitude, longitude, geohash_precision)
