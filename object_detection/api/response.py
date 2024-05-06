from pydantic import BaseModel
from typing import Any


class SuccesfullResponse(BaseModel):
    people: Any
    cars: Any
