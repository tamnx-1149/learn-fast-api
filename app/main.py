from fastapi import FastAPI

from app.routers import users
from app.routers import projects
from app.routers import tasks


app = FastAPI(
    title="TaskHub API",
    description="TaskHub RESTful API",
    version="1.0.0",
)


app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {
        "message": "TaskHub API is running"
    }
