from VideoSharing_Repo.CommentRepository import CommentRepository
from VideoSharing_DTO.Comment import Comment


#class variables are named _class by necessity of syntax

#To do
#->add a way to add the class and school id
#->link to create class from the school page instead of the top bar
#->improve classname.html to not be so shitty

class CommentService:

    comment_repo:CommentRepository

    def __init__(self) -> None:
        self.comment_repo = CommentRepository()

    def register_comment(self, text: str, video_id:int, username:str) -> bool:
        new_comment = Comment()
        new_comment.Content = text
        new_comment.VideoId = video_id
        new_comment.Username = username
        return self.comment_repo.add_comment(new_comment)

    def get_comments_from_video_id(self, video_id:int) -> list:
        returned_value = self.comment_repo.get_comments_from_video_id(video_id)

        if returned_value is not None:
            return returned_value
        else:
            return []