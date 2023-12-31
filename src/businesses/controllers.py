from uuid import uuid4
from typing import Any

from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from .. import db
from .models import Business
from ..exceptions import BadRequestException
from ..nearby_location.controllers import add_business_in_geo_spatial_model


def add_businesses_controller(business_data: dict[str, Any]) -> str:
    business_data["id"] = uuid4()
    try:
        db.session.add(Business(**business_data))
        db.session.commit()
        add_business_in_geo_spatial_model(
            business_data["id"], business_data["latitude"], business_data["longitude"]
        )
    except IntegrityError as exp:
        if isinstance(exp.orig, UniqueViolation):
            raise BadRequestException from exp
    return business_data["id"]


def get_business_controller(business_id: str) -> dict[str, Any]:
    business_data_obj = db.session.query(Business).get(business_id)
    business_data = business_data_obj.to_dict() if business_data_obj else None
    return business_data


def update_business_controller(business_id: str, business_info: dict[str, Any]) -> bool:
    rows_updated = (
        db.session.query(Business)
        .filter(Business.id == business_id)
        .update(business_info)
    )
    db.session.commit()
    return rows_updated


def delete_business_controller(business_id: str) -> bool:
    deleted_rows = (
        db.session.query(Business).filter(Business.id == business_id).delete()
    )
    db.session.commit()
    return deleted_rows
