from flask import request, jsonify, make_response

from . import businesses_bp


@businesses_bp.route("/businesses", methods=["POST"])
def add_businesses():
    body = request.json
    return make_response(jsonify({"body": "success"}), 200)


@businesses_bp.route("/businesses/<id>", methods=["GET"])
def get_business(id: str):
    return make_response(jsonify({"body": "success"}), 200)


@businesses_bp.route("/businesses/<id>", methods=["PUT"])
def update_business(id: str):
    return make_response(jsonify({"body": "success"}), 200)


@businesses_bp.route("/businesses/<id>", methods=["DELETE"])
def delete_business(id: str):
    return make_response(jsonify({"body": "success"}), 200)
