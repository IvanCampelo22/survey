from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.sql.schema import ForeignKey
from db.session import Base
from sqlalchemy.orm import relationship
import datetime

class Survey(Base):
    __tablename__ = 'survey'

    id = Column(Integer, primary_key=True, index=True)
    theme_id = Column(Integer, ForeignKey('theme.id'), nullable=True)
    title = Column(String(320), nullable=False)
    description = Column(String(520), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now())
    created_at = Column(DateTime, default=datetime.datetime.now())

    themes = relationship('theme', back_populates='surveys')