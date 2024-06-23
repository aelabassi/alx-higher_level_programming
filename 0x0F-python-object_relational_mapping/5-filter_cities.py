#!/usr/bin/python3
"""
List all cities of state
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s\
        ORDER BY cities.id", (argv[4],))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
