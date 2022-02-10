import psycopg2

class AppSettingsRepository:

    def __init__(self) -> None:
        pass

    def app_version(self) -> str:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")

        try:
            stmt = "SELECT app_value FROM ApplicationSettings WHERE app_key = 'ApplicationVersion';"
            cur = conn.cursor()
            cur.execute(stmt)

            app_version = cur.fetchone()[0]

            cur.close()
            return app_version

        except Exception as e:
            raise e
        finally:
            conn.close()


    def app_name(self) -> str:
        conn = psycopg2.connect(
            host="postgres",
            database="SSUVideoSharing",
            user="postgres-user",
            password="postgres-password")

        try:
            stmt = "SELECT app_value FROM ApplicationSettings WHERE app_key = 'ApplicationName';"
            cur = conn.cursor()
            cur.execute(stmt)

            app_name = cur.fetchone()[0]

            cur.close()
            return app_name

        except Exception as e:
            raise e
        finally:
            conn.close()

