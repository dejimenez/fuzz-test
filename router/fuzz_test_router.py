from typing import List
from uuid import UUID, uuid4
from fastapi import APIRouter, Depends, HTTPException
from enum import Enum
from pydantic import BaseModel

from fuzz.dto.fuzz_test_dto import FuzzTestCreate, FuzzTest
from fuzz.service.fuzz_test_service import get_fuzz_tests, get_fuzz_test, create_fuzz_test


from sqlalchemy.orm import Session
from .deps import get_db

# from ..dependencies import get_token_header


class ResponseStatus(str, Enum):
    success = "success"
    error = "error"


class ResponseFuzzTest(BaseModel):
    status: ResponseStatus
    data: FuzzTest


class ResponseListFuzzTest(BaseModel):
    status: ResponseStatus
    data: List[FuzzTest]


router = APIRouter(
    prefix="/fuzz-tests",
    tags=["fuzz-test"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=ResponseListFuzzTest)
async def get_all(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    fuzz_tests = await get_fuzz_tests(db, skip, limit)
    # fuzz_tests: List[FuzzTest] = [FuzzTest(name="Test1", url="http://url", status="created", id = uuid4())]

    return ResponseListFuzzTest(status=ResponseStatus.success, data=fuzz_tests)


@router.get("/{id}", response_model=ResponseFuzzTest)
async def find_by_id(id: UUID, db: Session = Depends(get_db)):
    fuzz_tests = await get_fuzz_test(db, id)

    return ResponseFuzzTest(status=ResponseStatus.success, data=fuzz_tests)


@router.post("/", response_model=ResponseFuzzTest)
async def create(fuzz_test: FuzzTestCreate, db: Session = Depends(get_db)):
    await create_fuzz_test(db, fuzz_test)

    return ResponseFuzzTest(status=ResponseStatus.success, data=fuzz_test)


@router.patch("/", response_model=ResponseFuzzTest)
async def create(fuzz_test: FuzzTestCreate, db: Session = Depends(get_db)):
    await create_fuzz_test(db, fuzz_test)

    return ResponseFuzzTest(status=ResponseStatus.success, data=fuzz_test)


@router.post("/compile")
def compile(fuzz_test: FuzzTest):
    print(fuzz_test.url, flush=True)
    # restler.compile()

    return {"status": "success", "url": fuzz_test.url}
