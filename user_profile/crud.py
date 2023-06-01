from sqlalchemy.orm import Session

import user_profile.models as models
from user_profile import schemas


def get_user_profile(db: Session):
    """ Get user profile """

    user_profile = db.query(models.UserProfileDB).get(1)
    if not user_profile:
        user_profile = models.UserProfileDB()
        db.add(user_profile)
        db.commit()
        db.refresh(user_profile)
    return user_profile


def update_user_profile(db: Session, user_profile: schemas.UserProfile):
    """ Update user profile """

    user_profile_db = db.query(models.UserProfileDB).get(1)

    for key, value in user_profile.dict().items():
        setattr(user_profile_db, key, value)

    db.add(user_profile_db)
    db.commit()
    db.refresh(user_profile_db)
    return user_profile_db
