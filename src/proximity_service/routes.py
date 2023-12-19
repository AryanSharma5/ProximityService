from flask import jsonify

from . import proximity_service_bp


@proximity_service_bp.route("/")
def home():
    return jsonify({"statusCode": 200, "body": "Hello from proximity service"})
