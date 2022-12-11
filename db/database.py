import psycopg2


class Db():
    
    connection = None

    def __init__(self) -> None:
        
        try:
            self.connection = psycopg2.connect(
                host="db",
                user="root",
                password="R2D2-333",
                database="DataBase",
                port="5432"
            )
            print("Connection OK")

        except psycopg2.Error as err:
            print(f">>> DbError =   {err.pgcode} : {err.pgerror}")
            self.connection = None


    def insertTweet(self, data: dict, table: str):

        if self.connection != None:

            keys = list(data.keys())
            values = list(data.values())
            pointer = self.connection.cursor()
            query = f""" INSERT INTO {table} ({keys[0]}, {keys[1]}, {keys[2]}, {keys[3]})
                            VALUES ({values[0]},{values[1]},{values[2]},{values[3]}) """

            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                return e
            finally:
                pointer.close()
            return data


    def readTweet(self, user_id: int, table: str):

        if self.connection != None:

            pointer = self.connection.cursor()
            query = f""" SELECT * FROM {table}
                        WHERE id={user_id} """

            try:
                pointer.execute(query)
                self.connection.commit()
                data = pointer.fetchone()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                return e
            finally:
                pointer.close()        
            return data


    def updateTweet(self, data: dict, table: str, user_id: int):

        if self.connection != None:
            keys = list(data.keys())
            values = list(data.values())
            pointer = self.connection.cursor()
            query = f""" UPDATE {table}
                        SET {keys[0]}={values[0]},{keys[1]}={values[1]},{keys[2]}={values[2]},{keys[3]}={values[3]}'
                        WHERE id={user_id} """
            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e={}
                e[f"{err.pgcode}"]= err.pgerror
                return (e)        
            finally:
                pointer.close()
            return data


    def deleteTweet(self, user_id: int, table: str):

        if self.connection != None:
            pointer = self.connection.cursor()
            query = f""" DELETE FROM {table}
                        WHERE id={user_id} """
            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                return (e)
            finally:
                pointer.close()
            return user_id