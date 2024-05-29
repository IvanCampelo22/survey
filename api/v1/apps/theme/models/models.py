from sqlalchemy import Integer, String, DateTime, Column
from db.session import Base
from sqlalchemy.orm import relationship
import datetime


class Theme(Base):
    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(320), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now())
    created_at = Column(DateTime, default=datetime.datetime.now())


    surveys = relationship('survey', back_populates='themes')