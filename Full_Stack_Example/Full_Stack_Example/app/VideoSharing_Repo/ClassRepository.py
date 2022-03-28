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
            stmt = "SELECT ClassId, ClassName, ClassCode, ClassCode, Section, Semester, Teacher, SchoolId FROM Classes WHERE ClassId = '"+id+"'"
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

