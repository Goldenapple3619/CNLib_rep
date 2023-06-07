from typing import Iterable

class Header(object):
    def __init__(self, data: dict = {}, **kwargs) -> None:
        if (not isinstance(data, Iterable)):
            raise TypeError()
        
        if (not isinstance(data, dict)):
            data: dict = dict(data)

        temp: dict = dict(data, **kwargs)

        self.keys = temp.keys()
        self.values = temp.values()
        self.data = temp.copy()

    def __repr__(self) -> str:
        temp: str = '\n'

        return (f"""header: {temp}{temp.join(f'    {item}: {self.data[item]}' for item in self.data)}""")

    def __str__(self) -> str:
        temp: str = '\n'

        return (f"""header: {temp}{temp.join(f'    {item}: {self.data[item]}' for item in self.data)}""")
