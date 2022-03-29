from VideoSharing_DTO.Class import Class
import psycopg2

class ClassRepository:

    def __init__(self) -> None:
        pass

    def get_class_from_class_id(self, id: int) -> Class:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-passwords")

        try:
            stmt = "SELECT ClassId, ClassName, ClassCode, ClassCode, Section, Semester, Teacher, SchoolId FROM Classes WHERE ClassId = '"+id+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            _class = cur.fetchall()
            if not cur.rowcount > 0:
                return None
            temp_class = _class[0]

            new_class = Class()
            new_class.ClassId = temp_class[0]
            new_class.ClassName = temp_class[1]
            new_class.ClassCode = temp_class[2]
            new_class.Section = temp_class[3]
            new_class.Semester = temp_class[4]
            new_class.Teacher = temp_class[5]
            new_class.SchoolId = temp_class[6]

            cur.close()
            return new_class

        except Exception as e:
            raise e
        finally:
            conn.close()

    def get_class(self, _class: Class) -> Class:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-passwords")
        
        class_name:str = _class.ClassName
        class_code:str = _class.ClassCode
        class_section:str = _class.Section
        class_semester:str = _class.Semester
        class_teacher:str = _class.Teacher

        try:
            stmt = "SELECT ClassId, ClassName, ClassCode, ClassCode, Section, Semester, Teacher, SchoolId FROM Classes WHERE ClassName = '"+class_name+"' AND ClassCode = '"+class_code+"' AND Section = '"+class_section+"' AND Semester = '"+class_semester+"' AND Teacher = '"+class_teacher+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            _class = cur.fetchall()
            if not cur.rowcount > 0:
                return None
            temp_class = _class[0]

            new_class = Class()
            new_class.ClassId = temp_class[0]
            new_class.ClassName = temp_class[1]
            new_class.ClassCode = temp_class[2]
            new_class.Section = temp_class[3]
            new_class.Semester = temp_class[4]
            new_class.Teacher = temp_class[5]
            new_class.SchoolId = temp_class[6]

            cur.close()
            return new_class

        except Exception as e:
            raise e
        finally:
            conn.close()

    def find_classes(self, search_term:str, school_id:int) -> list:
        conn = psycopg2.connect(
        host = "postgres",
        database= "SSUVideoSharing",
        user="postgres-user",
        password="postgres-password")
        
        try:
            stmt = "SELECT * FROM Classes WHERE ClassName LIKE '%"+search_term+"%' AND SchoolId = '"+school_id+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            conn.commit()
            tuple_list = cur.fetchall()

            class_list = []
            for tp in tuple_list:
                _class = Class()
                _class.ClassId = tp[0]
                _class.ClassName = tp[1]
                _class.ClassCode = tp[2]
                _class.Section = tp[3]
                _class.Semester = tp[4]
                _class.Teacher = tp[5]
                _class.SchoolId = tp[6]
                class_list.append(_class)
            
            cur.close()
            return class_list

        except Exception as e:
            raise e
        finally:
            conn.close()

    def add_class(self, _class:Class) -> bool:
        conn = psycopg2.connect(
             host="postgres",
             database= "SSUVideoSharing",
             user="postgres-user",
             password="postgres-password")
        
        try:
            stmt = "INSERT INTO Classes(ClassName, ClassCode, Section, Semester, Teacher, SchoolId) VALUES('"+_class.ClassName+"', '"+_class.ClassCode+"', '"+_class.Section+"', '"+_class.Semester+"', '"+_class.Teacher+"', '"+_class.SchoolId+"');"
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