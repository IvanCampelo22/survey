from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.sql.schema import ForeignKey
from db.session import Base

class Theme(Base):
    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(320), nullable=False)