from pydantic import BaseModel
from typing import Optional



class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STaskRead(STaskAdd): 
    id: int


class STaskID(BaseModel):
    ok: bool = True
    task_id: int