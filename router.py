from fastapi import APIRouter

from typing import Annotated
from fastapi import Depends

from schemas import STask, STaskAdd, STaskId
from repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    ...
    task_id = await TaskRepository.add_one(task)
    response = {"ok": True, "task_id": task_id}

    return response


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    # data = {"data": tasks}

    return tasks

