from sqlite3 import Timestamp

class Video:
    VideoId: int
    Subject: str
    Content: str
    Description: str
    Uploader: str
    CreateDate: Timestamp
    LectureData: int
    ClassID: int

    def __init__(self) -> None:
        pass