from tkinter import E
import psycopg2
from VideoSharing_DTO.School import School
from VideoSharing_DTO.User import User
from VideoSharing_BL.UserService import UserService
from VideoSharing_BL.SchoolService import SchoolService



class USMRepository:

    def __init__(self) -> None:
        self.user_svc = UserService()
        self.school_svc = SchoolService()

    def get_schools_from_user(self, user_id: int) -> list:
        #returns a list of DTOs
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")

        try:
            stmt = "SELECT UserId FROM UserSchoolMapping WHERE SchoolId = '"+str(user_id)+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            schools = cur.fetchall()
            if not cur.rowcount > 0:
                return None
            final_schools = []
            for school in schools:
                final_schools.append(self.school_svc.get_school_from_id(school[0])) 
            
            cur.close()
            return final_schools

        except Exception as e:
            raise e
        finally:
            conn.close()

    def get_users_from_school(self, user: User) -> School:
        #returns a list of DTOs
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        user_id:str = user.UserId

        try:
            stmt = "SELECT SchoolId FROM UserSchoolMapping WHERE UserId = '"+user_id+"';"
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

    def get_pair(self, school_id: int, user_id:int) -> tuple:
        conn = psycopg2.connect(
            host = "postgres",
            database= "SSUVideoSharing",
            user= "postgres-user",
            password= "postgres-password")

        try:
            stmt = "SELECT SchoolId, UserId FROM UserSchoolMapping WHERE SchoolId = '"+str(school_id)+"' AND UserId = '"+str(user_id)+"'"
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

    def add_pair(self, school_id: int, user_id: int) -> bool:
        conn = psycopg2.connect(
            host = "postgres",
            database= "SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        try:
            stmt = "INSERT INTO UserSchoolMapping(SchoolId, UserId) VALUES( '"+str(school_id)+"', '"+str(user_id)+"');"
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