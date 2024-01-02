import uuid
from apps import db
from sqlalchemy.dialects.postgresql import UUID

class Companies(db.Model):
    __tablename__ = 'companies'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Company {self.name}>'