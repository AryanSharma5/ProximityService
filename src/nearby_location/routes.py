from flask import request, jsonify, make_response
from haversine import haversine

from . import nearby_location_bp


@nearby_location_bp.route("/search/nearby")
def nearby_locations():
    lat = request.args.get("lat")
    long = request.args.get("long")
    radius = request.args.get("radius")
    return make_response(
        jsonify(
            {
                "body": {
                    "latitude": lat,
                    "longitude": long,
                    "radius": radius,
                    "nearByLocations": [],
                }
            }
        ),
        200,
    )
