from typing import List

from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_db

from ..domain.rules import service, schemas

router = APIRouter(
    prefix="/rule",
    tags=["rule"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Rule, status_code=201)
def create_rule(rule: schemas.Rule, db = Depends(get_db)):
    return service.create_rule(db=db, rule=rule)


@router.get("/list", response_model=str)
def get_rules():
    return 'Oi moanoite'
