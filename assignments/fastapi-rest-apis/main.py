from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    description: str = ""


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Task API"}


@app.get("/tasks", response_model=list[Task], tags=["Tasks"])
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def get_task(task_id: int):
    # TODO: Return the requested task or raise HTTPException with status 404.
    pass


@app.post(
    "/tasks",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
    tags=["Tasks"],
)
def create_task(task: TaskCreate):
    # TODO: Assign an ID, save the task, and return it.
    pass


@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: int, task_update: TaskCreate):
    # TODO: Update the task or raise HTTPException with status 404.
    pass


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Tasks"],
)
def delete_task(task_id: int):
    # TODO: Delete the task or raise HTTPException with status 404.
    pass
