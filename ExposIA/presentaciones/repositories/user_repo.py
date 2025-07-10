from ...common.database import SessionLocal
from ..models.user import User, UserOrm


def create_user(user: User) -> User:
    with SessionLocal() as session:
        obj = UserOrm(nombre=user.nombre, email=user.email, password=user.password)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return User(**obj.__dict__)


def list_users() -> list[User]:
    with SessionLocal() as session:
        objs = session.query(UserOrm).all()
        return [User(**o.__dict__) for o in objs]


def get_user(user_id: int) -> User | None:
    with SessionLocal() as session:
        obj = session.get(UserOrm, user_id)
        return User(**obj.__dict__) if obj else None


def update_user(user_id: int, user: User) -> User | None:
    with SessionLocal() as session:
        obj = session.get(UserOrm, user_id)
        if not obj:
            return None
        for f, v in user.model_dump(exclude={"id"}).items():
            setattr(obj, f, v)
        session.commit()
        return User(**obj.__dict__)


def delete_user(user_id: int) -> bool:
    with SessionLocal() as session:
        obj = session.get(UserOrm, user_id)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True
