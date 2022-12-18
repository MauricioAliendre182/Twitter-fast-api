import psycopg2
from uuid import UUID

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


    def insertTweet(self, data: dict, uuid: UUID):

        if self.connection != None:

            keys = list(data.keys())
            values = list(data.values())
            pointer = self.connection.cursor()
            query = f""" INSERT INTO tweets ({keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}, user_id)
                            VALUES ('{values[0]}','{values[1]}','{values[2]}','{values[3]}', '{uuid}') """

            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return e
            finally:
                pointer.close()
            return data


    def readTweet(self, tweet_id: UUID):

        if self.connection != None:

            pointer = self.connection.cursor()
            query = f""" SELECT * FROM tweets
                        WHERE tweet_id='{tweet_id}' """

            try:
                pointer.execute(query)
                self.connection.commit()
                data = pointer.fetchone()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return e
            finally:
                pointer.close()        
            return data

    def readAllTweets(self):

        if self.connection != None:

            pointer = self.connection.cursor()
            query = f""" SELECT u.user_id, u.email, u.first_name, u.last_name, u.birth_date, t.tweet_id, t.content, t.created_at, t.update_at
                         FROM users u
                         INNER JOIN tweets t
                         ON u.user_id = t.user_id"""

            try:
                pointer.execute(query)
                self.connection.commit()
                data = pointer.fetchall()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return e
            finally:
                pointer.close()
            tweet_dictionary = {num: value for (num, value) in zip(range(len(data)), data)}        
            return tweet_dictionary      

    def updateTweet(self, data: dict, tweet_id: UUID):

        if self.connection != None:
            keys = list(data.keys())
            values = list(data.values())
            pointer = self.connection.cursor()
            query = f""" UPDATE tweets
                        SET {keys[0]}='{values[0]}',{keys[1]}='{values[1]}',{keys[2]}='{values[2]}'
                        WHERE tweet_id='{tweet_id}' """
            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e={}
                e[f"{err.pgcode}"]= err.pgerror
                self.connection.rollback()
                return (e)        
            finally:
                pointer.close()
            return data


    def deleteTweet(self, tweet_id: UUID):

        if self.connection != None:
            pointer = self.connection.cursor()
            query = f""" DELETE FROM tweets
                        WHERE tweet_id='{tweet_id}' """
            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return (e)
            finally:
                pointer.close()
            return tweet_id
    
    def insertUser(self, data: dict):

        if self.connection != None:

            keys = list(data.keys())
            values = list(data.values())
            pointer = self.connection.cursor()
            query = f""" INSERT INTO users ({keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}, {keys[4]})
                            VALUES ('{values[0]}','{values[1]}','{values[2]}','{values[3]}','{values[4]}') """

            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return e
            finally:
                pointer.close()
            return data


    def readUser(self, user_id: UUID):

        if self.connection != None:

            pointer = self.connection.cursor()
            query = f""" SELECT * FROM users
                        WHERE user_id='{user_id}' """

            try:
                pointer.execute(query)
                self.connection.commit()
                data = pointer.fetchone()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return e
            finally:
                pointer.close()        
            return data
    
    def readRegisterUser(self, user_id: UUID, email: str, password: str):

        if self.connection != None:

            pointer = self.connection.cursor()
            query = f""" SELECT u.user_id, u.email, p.password
                         FROM users u
                         INNER JOIN passwords p
                         ON u.user_id = p.user_id
                         WHERE u.user_id='{user_id}' AND u.email='{email}' AND p.password='{password}' """

            try:
                pointer.execute(query)
                self.connection.commit()
                data = pointer.fetchone()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return e
            finally:
                pointer.close()        
            return data

    def readAllUsers(self):

        if self.connection != None:

            pointer = self.connection.cursor()
            query = f""" SELECT * FROM users"""

            try:
                pointer.execute(query)
                self.connection.commit()
                data = pointer.fetchall()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return e
            finally:
                pointer.close()
            user_dictionary = {num: value for (num, value) in zip(range(len(data)), data)}        
            return user_dictionary

    def updateUser(self, data: dict, user_id: UUID):

        if self.connection != None:
            keys = list(data.keys())
            values = list(data.values())
            pointer = self.connection.cursor()
            query = f""" UPDATE users
                        SET {keys[0]}='{values[0]}',{keys[1]}='{values[1]}',{keys[2]}='{values[2]}',{keys[3]}='{values[3]}'
                        WHERE user_id='{user_id}' """
            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e={}
                e[f"{err.pgcode}"]= err.pgerror
                self.connection.rollback()
                return (e)        
            finally:
                pointer.close()
            return data


    def deleteUser(self, user_id: UUID):

        if self.connection != None:
            pointer = self.connection.cursor()
            query = f""" DELETE FROM users
                        WHERE user_id='{user_id}' """
            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return (e)
            finally:
                pointer.close()
            return user_id
    
    def insertPassword(self, user_password: str, user_id: UUID):

        if self.connection != None:
            pointer = self.connection.cursor()
            query = f""" INSERT INTO passwords (password, user_id)
                            VALUES ('{user_password}', '{user_id}') """

            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return e
            finally:
                pointer.close()
            message = {"password_message": "Password introduced succesfully"}
            return message

    def updatePassword(self, user_password: str, user_id: UUID):

        if self.connection != None:
            pointer = self.connection.cursor()
            query = f""" UPDATE passwords
                        SET password='{user_password}'
                        WHERE user_id='{user_id}'"""

            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return e
            finally:
                pointer.close()
            message = {"password_message": "Password updated succesfully"}
            return message
    

    def deletePassword(self, user_id: UUID):

        if self.connection != None:
            pointer = self.connection.cursor()
            query = f""" DELETE FROM passwords
                        WHERE user_id='{user_id}' """
            try:
                pointer.execute(query)
                self.connection.commit()
            except psycopg2.Error as err:
                e = {}
                e[f"{err.pgcode}"] = err.pgerror
                self.connection.rollback()
                return (e)
            finally:
                pointer.close()
            return user_id