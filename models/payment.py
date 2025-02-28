from repository.database import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Payment(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime)