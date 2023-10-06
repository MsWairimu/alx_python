#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys
import pycodestyle

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host="localhost",
                         port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

    # Validate code against PEP8 standards
    style = pycodestyle.StyleGuide()
    result = style.check_files(['script.py'])
    print(result.total_errors)
