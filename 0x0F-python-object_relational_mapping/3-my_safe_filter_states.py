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
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM `states`\
                   WHERE `name`=(%s) ORDER BY `id` ASC", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
