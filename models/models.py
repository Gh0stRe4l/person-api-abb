from pydantic import BaseModel
from typing import Optional

class Location(BaseModel):
    code: str
    name: str
    state: str
    is_capital: Optional[bool] = False  # Campo opcional con valor por defecto False
