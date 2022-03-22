from tkinter import E
from numpy import append
import psycopg2
from VideoSharing_DTO.School import School
from VideoSharing_DTO.User import User
from VideoSharing_BL.UserService import UserService
from VideoSharing_BL.SchoolService import SchoolService



class USMRepository:

    def __init__(self) -> None:
        self.user_svc = UserService()
        self.school_svc = SchoolService()

    def get_users_from_school(self, school: School) -> list:
        #returns a list of DTOs
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        school_id:str = school.SchoolId

        try:
            stmt = "SELECT UserID FROM UserSchoolMappingRepository WHERE SchoolId = '"+school_id+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            schools = cur.fetchall()
            if not cur.rowcount > 0:
                return None
            final_schools = []
            for school in schools:
                final_schools.append(self.school_svc.get_school_from_id(school[0])) #a bit mixed up
            
            cur.close()
            return final_schools

        except Exception as e:
            raise e
        finally:
            conn.close()


    def get_schools_from_user(self, user: User) -> School:
        #returns a list of DTOs
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        user_id:str = user.UserId

        try:
            stmt = "SELECT SchoolId FROM UserSchoolMappingRepository WHERE UserId = '"+user_id+"';"
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

    def add_pair(self, school: School, user: User) -> bool:
        conn = psycopg2.connect(
            host = "postgres",
            database= "SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        try:
            stmt = "INSERT INTO UserSchoolMappingRepository(SchoolId, UserId) VALUES( '"+school.SchoolId+"', '"+user.UserId+"');"
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