from tkinter import E
import psycopg2
from VideoSharing_DTO.School import School


class SchoolRepository:

    def __init__(self) -> None:
        pass

    def get_school(self, school: School) -> School:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        school_name:str = school.SchoolName
        school_state:str = school.SchoolState
        school_city:str = school.City

        try:
            stmt = "SELECT SchoolId, SchoolName, SchoolState, City, Picture FROM School WHERE SchoolName = '"+school_name+"' AND SchoolState = '"+school_state+"' AND City = '"+school_city+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            school = cur.fetchall()
            if not cur.rowcount > 0:
                return None

            tempSchool = school[0]

            newSchool = School()
            newSchool.SchoolId = tempSchool[0]
            newSchool.SchoolName = tempSchool[1]
            newSchool.SchoolState = tempSchool[2]
            newSchool.City = tempSchool[3]
            newSchool.Picture = tempSchool[4]
            
            cur.close()
            return newSchool

        except Exception as e:
            raise e
        finally:
            conn.close()

    def get_school(self, id: int) -> School:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")

        try:
            stmt = "SELECT SchoolId, SchoolName, SchoolState, City, Picture FROM School WHERE SchoolId = '"+id+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            school = cur.fetchall()
            if not cur.rowcount > 0:
                return None

            tempSchool = school[0]

            newSchool = School()
            newSchool.SchoolId = tempSchool[0]
            newSchool.SchoolName = tempSchool[1]
            newSchool.SchoolState = tempSchool[2]
            newSchool.City = tempSchool[3]
            newSchool.Picture = tempSchool[4]
            
            cur.close()
            return newSchool

        except Exception as e:
            raise e
        finally:
            conn.close()

    def find_schools(self, search_term: str) -> list:
        conn = psycopg2.connect(
            host = "postgres",
            database= "SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        try:
            stmt = "SELECT * FROM School WHERE SchoolName LIKE '"+search_term+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            conn.commit()
            tuple_list = cur.fetchall()

            school_list = []
            for tp in tuple_list:
                school = School()
                school.SchoolId = tp[0]
                school.SchoolName = tp[1]
                school.SchoolState = tp[2]
                school.City = tp[3]
                school.Picture = tp[4]
                school_list.append(school)
            
            cur.close()
            return school_list

        except Exception as e:
            raise e
        finally:
            conn.close()

    def add_school(self, school: School) -> bool:
        conn = psycopg2.connect(
            host = "postgres",
            database= "SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")
        
        try:
            stmt = "INSERT INTO School(SchoolName, SchoolState, City, Picture) VALUES( '"+school.SchoolName+"', '"+school.SchoolState+"','"+school.City+"' , '"+school.Picture+"');"
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