#!/usr/bin/python3
import sys
import MySQLdb

def get_states(username, password, db_name):
    """List all states from the database hbtn_0e_0_usa"""
    
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=db_name,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
    
    if __name__ == "__main__":
        credentials = sys.argv
        username = sys.argv[1]
        passwd = sys.argv[2]
        db_name = sys.argv[3]
        get_states(username, password, db_name)
