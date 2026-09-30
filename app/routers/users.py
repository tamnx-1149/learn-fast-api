from fastapi import APIRouter


router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
)


@router.get("")
def users():
    return {
        "message": "Users API"
    }
