import datetime

class Task:
    
    def __init__(self, description, category, added_at=None, completed_at=None, status=None, position=None):
        self._category = category
        self._description = description
        self._added_at = added_at if added_at is not None else datetime.datetime.now().isoformat()
        self._completed_at = completed_at if completed_at is not NameError else None
        self._status = status if status is not None else True
        self._position = position if position is not None else None
        
    def __repr__(self):
        return f"({self._description}, {self._category}, {self._added_at}, {self._completed_at}, {self._status}, {self._position})"