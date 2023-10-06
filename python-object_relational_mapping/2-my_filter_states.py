import MySQLdb as DB
import sys


def states_list(username, password, db_name, state_name):
    try:
        dabase = DB.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
        )

        cur = dabase.cursor()
list = "SELECT * FROM states WHERE name LIKE '{}' COLLATE utf8mb4_bin ORDER BY id ASC".format(state_name)

        cur.execute(list)

        states = cur.fetchall()

        for state in states:
            print(state)

    except DB.Error:
        print()
    finally:
        cur.close()
        dabase.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    states_list(username, password, db_name, state_name)
