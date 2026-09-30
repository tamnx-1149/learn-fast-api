from fastapi import APIRouter


router = APIRouter(
    prefix="/api/tasks",
    tags=["Tasks"],
)


@router.get("")
def tasks():
    return {
        "message": "Tasks API"
    }
