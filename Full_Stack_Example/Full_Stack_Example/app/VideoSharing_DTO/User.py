from sqlite3 import Timestamp


class User:
    UserId: int
    UserName: str
    Pwd: str
    LastLogin: Timestamp

    def __init__(self) -> None:
        pass