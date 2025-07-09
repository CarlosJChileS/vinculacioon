from typing import Dict, Generic, List, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

class InMemoryRepository(Generic[T]):
    def __init__(self):
        self._db: Dict[int, T] = {}
        self._counter = 1

    def create(self, obj: T) -> T:
        obj_dict = obj.model_dump()
        obj_dict['id'] = self._counter
        obj = obj.__class__(**obj_dict)
        self._db[self._counter] = obj
        self._counter += 1
        return obj

    def list(self) -> List[T]:
        return list(self._db.values())

    def get(self, obj_id: int) -> Optional[T]:
        return self._db.get(obj_id)

    def update(self, obj_id: int, obj: T) -> Optional[T]:
        if obj_id in self._db:
            obj_dict = obj.model_dump()
            obj_dict['id'] = obj_id
            updated = obj.__class__(**obj_dict)
            self._db[obj_id] = updated
            return updated
        return None

    def delete(self, obj_id: int) -> bool:
        return self._db.pop(obj_id, None) is not None
