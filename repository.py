from schemas import STask, STaskAdd
from database import new_session, TasksOrm
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TasksOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @staticmethod
    def orm_to_dict(task_model: TasksOrm) -> dict:
        return {
            "id": task_model.id,
            "name": task_model.name,
            "description": task_model.description,
        }

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(cls.orm_to_dict(task_model)) for task_model in task_models]
            return task_schemas
