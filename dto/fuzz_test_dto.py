from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class FuzzTestStatus(str, Enum):
    created = "created"
    compiled = "compiled"


class FuzzTestBase(BaseModel):
    name:   str
    url:    str


class FuzzTestCreate(FuzzTestBase):
    id: Optional[UUID] = uuid4()
    status: Optional[FuzzTestStatus] = FuzzTestStatus.created
    pass


class FuzzTest(FuzzTestBase):
    id: UUID

    class Config:
        orm_mode = True
