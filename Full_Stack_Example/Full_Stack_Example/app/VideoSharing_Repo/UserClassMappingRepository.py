from tkinter import E
import psycopg2
from VideoSharing_DTO.Class import Class
from VideoSharing_DTO.User import User
from VideoSharing_BL.UserService import UserService
from VideoSharing_BL.ClassService import ClassService



class UCMRepository:

    def __init__(self) -> None:
        self.user_svc = UserService()
        self.class_svc = ClassService()

    def get_classes_from_user(self, user_id: int) -> list:
        #returns a list of DTOs
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")

        try:
            stmt = "SELECT ClassId FROM UserClassMapping WHERE UserId = '"+str(user_id)+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            classes = cur.fetchall()
            if not cur.rowcount > 0:
                return None
            final_class = []
            for _class in classes:
                final_class.append(self.class_svc.get_class_from_id(_class[0])) 
            
            cur.close()
            return final_class

        except Exception as e:
            raise e
        finally:
            conn.close()

    def get_users_from_class(self, class_id: int) -> list:
        #returns a list of DTOs
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        

        try:
            stmt = "SELECT UserId FROM UserClassMapping WHERE ClassId = '"+str(class_id)+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            users = cur.fetchall()
            if not cur.rowcount > 0:
                return None

            final_users = []
            for user in users:
                final_users.append(self.user_svc.get_user_from_id(user[0]))#the index here is a guess
                
            cur.close()
            return final_users

        except Exception as e:
            raise e
        finally:
            conn.close()

    def get_pair(self, class_id: int, user_id:int) -> tuple:
        conn = psycopg2.connect(
            host = "postgres",
            database= "SSUVideoSharing",
            user= "postgres-user",
            password= "postgres-password")

        try:
            stmt = "SELECT ClassId, UserId FROM UserClassMapping WHERE ClassId = '"+str(class_id)+"' AND UserId = '"+str(user_id)+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            pair = cur.fetchall()
            if not cur.rowcount > 0:
                return None 

            cur.close()
            return (pair[0])

        except Exception as e:
            raise e
        finally:
            conn.close()

    def add_pair(self, class_id: int, user_id: int) -> bool:
        conn = psycopg2.connect(
            host = "postgres",
            database= "SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        try:
            stmt = "INSERT INTO UserClassMapping(ClassId, UserId) VALUES( '"+str(class_id)+"', '"+str(user_id)+"');"
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