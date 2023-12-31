from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql import UUID

from .. import db


class Business(db.Model):
    __tablename__ = "Business"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    type = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(100), nullable=False, unique=True)
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    latitude = db.Column(db.Double(5), nullable=False, unique=True)
    longitude = db.Column(db.Double(5), nullable=False, unique=True)

    def __str__(self):
        return (
            f"Business: {self.id}, {self.type}, {self.address}, {self.city}"
            + f"{self.state}, {self.country}, {self.latitude}, {self.longitude}"
        )

    def to_dict(self):
        return {
            col.key: getattr(self, col.key)
            for col in inspect(self).mapper.column_attrs
            if col.key != "id"
        }
