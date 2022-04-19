from hashlib import new
import psycopg2
from VideoSharing_DTO.Comment import Comment

class CommentRepository:

    def __init__(self) -> None:
        pass

    def get_comments_from_video_id(self, video_id:int) -> list:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")

        try:
            stmt = "SELECT * FROM Comments WHERE VideoId = '"+str(video_id)+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            tuple_list = cur.fetchall()
            if not cur.rowcount > 0:
                return None
            comment_list = []

            for tp in tuple_list:
                newComment = Comment()
                newComment.CommentId = tp[0]
                newComment.Content = tp[1]
                newComment.VideoId = tp[2]
                newComment.Username = tp[3]

                comment_list.append(newComment)

            cur.close()
            return comment_list

        except Exception as e:
            raise e
        finally:
            conn.close()
    
   

    def add_comment(self,comment: Comment) -> bool:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")

        try:
            stmt = "INSERT INTO Comments(Content, VideoId, Username) VALUES( '"+comment.Content+"', '"+str(comment.VideoId)+"','"+comment.Username+"');"
            cur = conn.cursor()
            cur.execute(stmt)
            conn.commit()
            rowcount = cur.rowcount

            cur.close()
            return rowcount > 0

        except Exception as e:
            raise e
        finally:
            conn.close()
    