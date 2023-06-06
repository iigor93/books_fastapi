from fastapi import APIRouter
from user_profile import crud as user_profile_crud
from user_profile import schemas as user_profile_schemas

from sql_app.database import DB_SESSION

router = APIRouter()


@router.get("/{user_profile_id}/", response_model=user_profile_schemas.UserProfile)
def get_user_profile(db: DB_SESSION, user_profile_id: int = 1):
    user_profile = user_profile_crud.get_user_profile(db)
    return user_profile


@router.put("/{user_profile_id}/", response_model=user_profile_schemas.UserProfile)
async def update_user_profile(db: DB_SESSION, user_profile: user_profile_schemas.UserProfile, user_profile_id: int = 1):
    user_profile_updated = user_profile_crud.update_user_profile(db, user_profile)
    return user_profile_updated
