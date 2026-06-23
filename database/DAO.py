from database.DB_connect import DBConnect
from model.Constructor import Constructor


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = ("SELECT distinct year "
                 "FROM seasons s  "
                 "ORDER BY year")

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getCostruttori(annoI, annoF):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(re.constructorId) as ID
                    from results re, races ra
                    where ra.raceId = re.raceId and re.`position` is not null and ra.`year` >= %s and ra.`year` <= %s 
                    order by re.constructorId """

        cursor.execute(query, (annoI, annoF))

        for row in cursor:
            results.append(row["ID"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllCostruttori():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from constructors c """

        cursor.execute(query)

        for row in cursor:
            results.append(Constructor(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEdges(annoI, annoF):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.constructorId as c1, t2.constructorId as c2, count(*) as peso
                    from (select r.constructorId, r.driverId, ra.`year` 
                    from results r, races ra 
                    where r.raceId = ra.raceId and ra.`year` <= %s and ra.`year` >= %s and r.position is not null
                    group by r.constructorId, r.driverId) as t1, 
                    (select r.constructorId, r.driverId, ra.`year` 
                    from results r, races ra 
                    where r.raceId = ra.raceId and ra.`year` <= %s and ra.`year` >= %s and r.position is not null
                    group by r.constructorId, r.driverId) as t2
                    where t1.driverId = t2.driverId and t1.constructorId <> t2.constructorId and t1.constructorId < t2.constructorId
                    group by t1.constructorId, t2.constructorId"""

        cursor.execute(query, (annoF, annoI, annoF, annoI))

        for row in cursor:
            results.append((row["c1"], row["c2"], row["peso"]))

        cursor.close()
        conn.close()
        return results



