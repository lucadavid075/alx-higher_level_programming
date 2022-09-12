#!/usr/bin/python3
""" Lists all states with a name starting with N (upper N) """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM `states`\
                   WHERE `name` REGEXP '^N' ORDER BY `id` ASC")
    rows = cur.fetchall()
    for row in rows:
        if ("N" in row[1]):
            print(row)
    cur.close()
    db.close()
