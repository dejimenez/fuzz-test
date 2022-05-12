import sys
sys.path.append("..") 

from fastapi import FastAPI
from router import fuzz_test_router


# from model import fuzz_test as models
from fuzz.database.database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Fuzz testing", openapi_url=f"/openapi.json"
)

app.include_router(fuzz_test_router.router)
