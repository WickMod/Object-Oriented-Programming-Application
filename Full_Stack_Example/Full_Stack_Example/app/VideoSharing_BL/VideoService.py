from VideoSharing_BL.UserService import UserService
from VideoSharing_Repo.VideoRepository import VideoRepository
from VideoSharing_DTO.User import User
from VideoSharing_DTO.Video import Video


class VideoService:

    # For the future, commenting should be done with its own 
    # barebones comment DTO because it'll have an owner and a string

    user_svc : UserService
    video_repo : VideoRepository

    def __init__(self) -> None:
        self.user_svc = UserService()
        self.video_repo = VideoRepository()

    def add_video(self, video: Video) -> int:
        return self.video_repo.add_video(video)

    def get_video_from_video_id(self, video_id: int) -> Video:
        return self.video_repo.get_video_from_id(video_id)

    def get_videos_from_class_id(self, class_id: int) -> list:
        return self.video_repo.find_videos_from_class_id(class_id)

    def search_videos(self, search_term:str, class_id:int) -> list:
        return self.video_repo.find_videos(search_term, class_id)
