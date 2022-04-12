from sqlite3 import Timestamp

class Video:
    VideoId: int
    Subject: str
    Content: str
    Description: str
    UploaderId: int
    CreateDate: Timestamp
    ClassId: int

    def __init__(self) -> None:
        pass    