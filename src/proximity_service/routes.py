from flask import jsonify, make_response

from . import proximity_service_bp


@proximity_service_bp.route("/")
def home():
    return make_response(
        jsonify({"statusCode": 200, "body": "Hello from proximity service"}), 200
    )
