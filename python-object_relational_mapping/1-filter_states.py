#!/usr/bin/python3
#!/usr/bin/python3
"""
List all states with a name starting with n from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys
import main_3_0

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host="localhost",
                         port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'n%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
