from typing import Any

class Body(object):
    def __init__(self, data: Any = None) -> None:
        self.data = data

    def __str__(self) -> str:
        return (str(self.data))
    
    def __repr__(self) -> str:
        return (str(self.data))
    
    def to_string(self) -> str:
        return (str(self) if self.data else None)
    
