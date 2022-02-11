from hashlib import new
import psycopg2
from VideoSharing_DTO.User import User

class UserRepository:

    def __init__(self) -> None:
        pass

    def get_user(self,username) -> User:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")

        try:
            stmt = "SELECT UserId,Username FROM Users WHERE Username = '"+username+"';"
            cur = conn.cursor()
            cur.execute(stmt)
            user = cur.fetchall()
            if not cur.rowcount > 0:
                return None
            tempUser = user[0]

            newUser = User()
            newUser.UserId = tempUser[0]
            newUser.UserName = tempUser[1]
            newUser.LastLogin = tempUser[3]

            cur.close()
            return newUser

        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def add_user(self,user: User) -> bool:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")

        try:
            stmt = "INSERT INTO Users(Username, Pwd, LastLogin) VALUES( '"+user.UserName+"', '"+user.Pwd+"','"+str(user.LastLogin)+"');"
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