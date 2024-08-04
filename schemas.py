from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STaskGet(STaskAdd):
    id: int


class STask(STaskAdd):
    id: int
    model_config = ConfigDict()


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
