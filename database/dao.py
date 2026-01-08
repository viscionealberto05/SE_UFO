from database.DB_connect import DBConnect
from model.stato import Stato
class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_anni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT s_datetime \
                    FROM  sighting"""

        cursor.execute(query)

        for row in cursor:
            #print(row['s_datetime'])
            anno = str(row['s_datetime'])
            #print(anno[0:4])
            if anno[0:4] not in result and int(anno[0:4]) >= 1910 and int(anno[0:4])<=2014:
                result.append(anno[0:4])

        print(result)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_forme():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT shape \
                    FROM sighting
                    WHERE shape != "" """

        cursor.execute(query)

        for row in cursor:
            result.append(row['shape'])

        print(result)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_stati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT *
                    FROM state"""

        cursor.execute(query)

        for row in cursor:
            result.append(Stato(**row))

        print(result)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_edges(forma,anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT n.state1, n.state2, count(*) AS weight
                    FROM neighbor n, sighting s 
                    WHERE (n.state1 = s.state or n.state2 = s.state) AND s.shape = %s AND YEAR(s.s_datetime) = %s 
                    GROUP BY n.state1, n.state2"""


        cursor.execute(query, [forma, anno],)

        for row in cursor:
            result.append([row['state1'],row['state2'],row['weight']]) #lista di liste

        #print(result)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_vicini():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT *
                    FROM neighbor"""

        cursor.execute(query)

        for row in cursor:
            result.append((row['state1'],row['state2'])) #lista di tuple

        #print(result)

        cursor.close()
        conn.close()
        return result

