from datetime import datetime
from fuzz.database.database import Base

from sqlalchemy import Column, String, DateTime


class FuzzTestModel(Base):
    __tablename__ = "fuzz_tests"
    
    id         = Column(String, primary_key=True, index=True)
    name       = Column(String)
    url        = Column(String)
    status     = Column(String)
    created_at = Column(DateTime)
