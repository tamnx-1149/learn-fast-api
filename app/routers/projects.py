from fastapi import APIRouter


router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"],
)


@router.get("")
def projects():
    return {
        "message": "Projects API"
    }
