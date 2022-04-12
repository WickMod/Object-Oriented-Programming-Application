from tkinter import E
import psycopg2
from VideoSharing_DTO.Video import Video


class VideoRepository:

    def __init__(self) -> None:
        pass

    def get_video(self, video: Video) -> Video:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        video_id:str = video.VideoId
        class_id:str = video.ClassId


        #fill in rest when DTO is done

        try:
            stmt = "SELECT Subject, Content, Description, UploaderId, CreateDate, FROM Video WHERE VideoID = '"+video_id+"' AND ClassID = '"+class_id+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            video = cur.fetchall()
            if not cur.rowcount > 0:
                return None

            tempVideo = video[0]

            newVideo = Video()
            newVideo.VideoId = video_id
            newVideo.ClassId = class_id
            newVideo.Subject = tempVideo[0]
            newVideo.Content = tempVideo[1]
            newVideo.Description = tempVideo[2]
            newVideo.UploaderId = tempVideo[3]
            newVideo.CreateDate = tempVideo[4]

            
            cur.close()
            return newVideo

        except Exception as e:
            raise e
        finally:
            conn.close()

    def get_video_from_id(self, id: int) -> Video:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")

        try:
            stmt = "SELECT ClassId, Subject, Content, Description, UploaderId, CreateDate, FROM Video WHERE VideoID = '"+str(id)+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            video = cur.fetchall()
            if not cur.rowcount > 0:
                return None

            tempVideo = video[0]

            newVideo = Video()
            newVideo.VideoId = id
            newVideo.ClassId = tempVideo[0]
            newVideo.Subject = tempVideo[1]
            newVideo.Content = tempVideo[2]
            newVideo.Description = tempVideo[3]
            newVideo.UploaderId = tempVideo[4]
            newVideo.CreateDate = tempVideo[5]
            
            cur.close()
            return newVideo

        except Exception as e:
            raise e
        finally:
            conn.close()

    def find_videos(self, search_term: str) -> list:
        conn = psycopg2.connect(
            host = "postgres",
            database= "SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        try:
            stmt = "SELECT * FROM Video WHERE Subject LIKE '%"+search_term+"%';"
            cur = conn.cursor()
            cur.execute(stmt)
            conn.commit()
            tuple_list = cur.fetchall()

            video_list = []
            for tp in tuple_list:
                video = Video()
                video.VideoId = tp[0]
                video.Subject = tp[1]
                video.Content = tp[2]
                video.Description = tp[3]
                video.UploaderId = tp[4]
                video.CreateDate = tp[5]
                video.ClassId = tp[6]
                video_list.append(video)
            
            cur.close()
            return video_list

        except Exception as e:
            raise e
        finally:
            conn.close()

    def find_videos_from_class_id(self, class_id: int) -> list:
        conn = psycopg2.connect(
            host = "postgres",
            database= "SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        try:
            stmt = "SELECT * FROM Video WHERE ClassID = '"+str(class_id)+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            conn.commit()
            tuple_list = cur.fetchall()

            video_list = []
            for tp in tuple_list:
                video = Video()
                video.VideoId = tp[0]
                video.Subject = tp[1]
                video.Content = tp[2]
                video.Description = tp[3]
                video.UploaderId = tp[4]
                video.CreateDate = tp[5]
                video.ClassId = tp[6]
                video_list.append(video)
            
            cur.close()
            return video_list

        except Exception as e:
            raise e
        finally:
            conn.close()

    def add_video(self, video: Video) -> bool:
        conn = psycopg2.connect(
            host = "postgres",
            database= "SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        try:
            stmt = "INSERT INTO Video(VideoId, Subject, Content, Description, UploaderId, CreateDate, ClassId) VALUES( '"+video.VideoId+"', '"+video.Subject+"','"+video.Content+"' , '"+video.Description+"','"+video.UploaderId+"','"+video.CreateDate+"','"+video.ClassId+"');"
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