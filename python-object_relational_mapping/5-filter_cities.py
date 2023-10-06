#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name \
        state_name".format(sys.argv[0]))
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect \
    (user=username, passwd=password, db=db_name, port=3306, host="localhost")
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = \
    states.id WHERE states.name=%s ORDER BY cities.id ASC", (state_name,))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
