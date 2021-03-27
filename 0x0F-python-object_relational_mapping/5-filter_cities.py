#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    STATE = argv[4]
    try:
        db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS,
                             db=MY_DB)
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM states INNER JOIN cities \
                     ON states.id = cities.state_id WHERE states.name = %s \
                     ORDER BY cities.id;", (STATE,))
        rows = cur.fetchall()
        rows = [i[0] for i in rows]
        if rows:
            for j in range(len(rows)):
                if j is len(rows) - 1:
                    print("{}".format(rows[j]))
                else:
                    print("{}, ".format(rows[j]), end="")
        else:
            print()
    except Exception as e:
        print("Error: {}".format(e))
