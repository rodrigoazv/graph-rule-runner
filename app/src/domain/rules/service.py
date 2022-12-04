from ...database import driver

from fastapi import HTTPException

from . import repository, schemas

def create_rule(db: driver, rule: schemas.Rule):
    return repository.create_rule(db, rule);
