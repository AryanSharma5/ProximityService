from flask import request, jsonify, make_response

from ..exceptions import BadRequestException
from . import businesses_bp
from .controllers import (
    add_businesses_controller,
    get_business_controller,
    update_business_controller,
    delete_business_controller,
)


@businesses_bp.route("/businesses", methods=["POST"])
def add_businesses():
    body = request.json
    try:
        _id = add_businesses_controller(body)
    except BadRequestException as exp:
        print(exp)
        return make_response(jsonify({"statusCode": 502, "body": "Bad input"}), 502)
    return make_response(jsonify({"statusCode": 200, "body": {"id": _id}}), 200)


@businesses_bp.route("/businesses/<_id>", methods=["GET"])
def get_business(_id: str):
    print(_id)
    business = get_business_controller(_id)
    print(business)
    if not business:
        return make_response(
            jsonify(
                {
                    "statusCode": 404,
                }
            ),
            404,
        )
    return make_response(jsonify({"statusCode": 200, "body": business}), 200)


@businesses_bp.route("/businesses/<_id>", methods=["PUT"])
def update_business(_id: str):
    business_info = request.json
    is_updated = update_business_controller(_id, business_info)
    if not is_updated:
        return make_response(
            jsonify({"statusCode": 404, "body": f"{_id} not found"}), 404
        )
    return make_response(jsonify({"statusCode": 200, "body": {"id": _id}}), 200)


@businesses_bp.route("/businesses/<_id>", methods=["DELETE"])
def delete_business(_id: str):
    is_deleted = delete_business_controller(_id)
    if not is_deleted:
        return make_response(
            jsonify({"statusCode": 404, "body": f"{_id} not found"}), 404
        )
    return make_response(jsonify({"statusCode": 200, "body": "success"}), 200)
