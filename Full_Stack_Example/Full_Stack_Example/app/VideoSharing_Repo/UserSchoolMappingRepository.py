from tkinter import E
from numpy import append
import psycopg2
from VideoSharing_DTO.School import School
from VideoSharing_DTO.User import User
from VideoSharing_BL.UserService import UserService


class USMRepository:

    def __init__(self) -> None:
        self.user_svc = UserService()

    def get_users_from_school(self, school: School) -> list:
        #returns a list of DTOs
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        school_id:str = school.SchoolId

        try:
            stmt = "SELECT UserID FROM UserSchoolMappingRepository WHERE SchoolID = '"+school_id+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            schools = cur.fetchall() # we need to be able to get a user by user id
            if not cur.rowcount > 0:
                return None
            final_schools = []
            for school in schools:

                tempSchool = school[0]

                newSchool = School()
                newSchool.SchoolId = tempSchool[0]
                newSchool.SchoolName = tempSchool[1]
                newSchool.SchoolState = tempSchool[2]
                newSchool.City = tempSchool[3]
                newSchool.Picture = tempSchool[4]
                final_schools.append(newSchool)
            
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
            stmt = "SELECT SchoolId FROM School WHERE UserID = '"+user_id+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            users = cur.fetchall()
            if not cur.rowcount > 0:
                return None

            final_users = []
            for user in users:
                tempUser = users[0]

                newUser = User()
                newUser.SchoolId = tempUser[0]
                newUser.SchoolName = tempUser[1]
                newUser.SchoolState = tempUser[2]
                newUser.City = tempUser[3]
                newUser.Picture = tempUser[4]
                final_users.append(self.user_svc.get_user)
                
            cur.close()
            return newSchool

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
            stmt = "INSERT INTO USM(UserID, SchoolID) VALUES( '"+school.SchoolId+"', '"+user.UserId+"');"
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