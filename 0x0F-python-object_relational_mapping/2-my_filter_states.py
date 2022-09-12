#!/usr/bin/python3
""" Takes in an argument and displays all values in the states """

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
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name=('{}')\
                 ORDER BY id ASC".format(state_name)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        if (row[1] == state_name):
            print(row)
    cur.close()
    db.close()
