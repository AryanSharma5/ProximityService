from uuid import uuid4
from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql import UUID

from .. import db


class GeoSpatialModel(db.Model):
    __tablename__ = "geo_spatial"

    geohash = db.Column(db.String, primary_key=True)
    business_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("Business.id"),
        primary_key=True,
        default=uuid4,
    )

    def __str__(self):
        return f"geo_spatial: {self.geohash}, {self.business_id}"

    def to_dict(self):
        return {
            col.key: getattr(self, col.key) for col in inspect(self).mapper.column_attrs
        }
