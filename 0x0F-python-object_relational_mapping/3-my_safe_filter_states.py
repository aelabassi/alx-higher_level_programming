#!/usr/bin/python3
"""  filter all states by name from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match_ = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (match_,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
