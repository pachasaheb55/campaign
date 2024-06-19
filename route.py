from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from database import engine, Sessionlocal
from sqlalchemy.orm import Session


app = FastAPI(
    title="admin",
description="Administrative System.",
version="0.1.0",
docs_url='/api/database',
redoc_url=None,
openapi_url='/api/openapi.json' ,
# dependencies=[Depends(verify_token)]
)


def get_db():
    db = Sessionlocal()
    try: 
        yield db

    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

from raw_sql import get_rows
    
@app.get("/read_db")
async def read_db():  
    data = get_rows()
    return data