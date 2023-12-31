from flask import request, jsonify, make_response

from . import nearby_location_bp
from .controllers import get_nearby_locations
from ..exceptions import BadRequestException


@nearby_location_bp.route("/search/nearby")
def nearby_locations():
    lat = float(request.args.get("lat"))
    long = float(request.args.get("long"))
    radius = int(request.args.get("radius"))
    try:
        nearby_services = get_nearby_locations(
            latitude=lat, longitude=long, radius=radius
        )
    except BadRequestException as exp:
        print(exp)
        return make_response(jsonify({"statusCode": 502, "body": "Bad input"}), 502)
    return make_response(
        jsonify(
            {
                "body": {
                    "latitude": lat,
                    "longitude": long,
                    "radius": radius,
                    "nearByLocations": [nearby_services],
                }
            }
        ),
        200,
    )
