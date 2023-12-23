from uuid import uuid4
from typing import Dict, Any

from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from .. import db
from .models import Business
from ..exceptions import BadRequestException


def add_businesses_controller(business_data: Dict[str, Any]) -> str:
    business_data["id"] = uuid4()
    try:
        db.session.add(Business(**business_data))
        db.session.commit()
    except IntegrityError as exp:
        if isinstance(exp.orig, UniqueViolation):
            raise BadRequestException from exp
    return business_data["id"]


def get_business_controller(business_id: str) -> Dict[str, Any]:
    business_data_obj = Business.query.get(business_id)
    business_data = business_data_obj.to_dict() if business_data_obj else None
    return business_data


def update_business_controller(business_id: str, business_info: Dict[str, Any]) -> bool:
    rows_updated = Business.query.filter(Business.id == business_id).update(
        business_info
    )
    db.session.commit()
    return rows_updated


def delete_business_controller(business_id: str) -> bool:
    deleted_rows = Business.query.filter(Business.id == business_id).delete()
    db.session.commit()
    return deleted_rows
