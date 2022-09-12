#!/usr/bin/python3
""" Safe from SQL Injection """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cursor = db.cursor()

    query = """
    SELECT * FROM `states` WHERE `name`=(%s)
    COLLATE latin1_general_cs
    ORDER BY states.id ASC;
    """

    cursor.execute(query, (state_name, ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
