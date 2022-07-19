import os
from typing import List
from uuid import UUID, uuid4
from fuzz.model.fuzz_test import FuzzTestModel
from fuzz.dto.fuzz_test_dto import FuzzTestCreate, FuzzTest, FuzzTestStatus
from sqlalchemy.orm import Session
from datetime import datetime

import json
import requests

from restler.compiler import compile


async def get_fuzz_test(db: Session, id: UUID):
    return db.query(FuzzTestModel).filter(FuzzTestModel.id == str(id)).first()


async def get_fuzz_tests(db: Session, skip: int, limit: int):

    # return [FuzzTest(name="Test1", url="http://url", status="created", id=uuid4())]
    return db.query(FuzzTestModel).offset(skip).limit(limit).all()


async def create_fuzz_test(db: Session, fuzz_test: FuzzTestCreate):
    db_fuzz_test = FuzzTestModel(
        id=str(fuzz_test.id),
        name=fuzz_test.name,
        url=fuzz_test.url,
        created_at=datetime.utcnow()
    )
    db.add(db_fuzz_test)
    db.commit()
    db.refresh(db_fuzz_test)

    await get_openapi(db_fuzz_test)

    return db_fuzz_test


async def get_openapi(fuzz_test: FuzzTest):
    r = requests.get(url=fuzz_test.url)
    data = r.json()
    directory = str(fuzz_test.id)

    os.mkdir(f"tofuzz/{directory}")
    with open(f"tofuzz/{directory}/spec.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    await compile_fuzz_test(directory)


async def compile_fuzz_test(directory: str):
    compile(f"tofuzz/{directory}")
