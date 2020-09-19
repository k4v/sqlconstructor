from enum import Enum

class OpTypes(Enum):
    SELECT = 'SELECT'
    UPDATE = 'UPDATE'
    INSERT = 'INSERT'
    DELETE = 'DELETE'
    JOIN = 'JOIN'