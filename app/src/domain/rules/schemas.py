from pydantic import BaseModel


class Rule(BaseModel):
    name = str
    value = int
    code = str