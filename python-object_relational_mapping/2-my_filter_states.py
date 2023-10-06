#!/usr/bin/python3
"""
Script that lists all states with a name starting with n (lowercase n) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def states_list(username, password, db_name):
    try:
        dabase = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
        )

        cur = dabase.cursor()

        list = "SELECT * FROM states WHERE name LIKE 'n%' COLLATE utf8mb4_bin"

        cur.execute(list)

        states = cur.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error:
        print()
    finally:
        cur.close()
        dabase.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    states_list(username, password, db_name)
