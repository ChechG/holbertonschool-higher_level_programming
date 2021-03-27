#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    MY_STATE = argv[4]
    try:
        db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS,
                             db=MY_DB)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY \
                     id".format(MY_STATE))
        rows = cur.fetchall()
        for r in rows:
            if r[1] == MY_STATE:
                print(r)
    except Exception as e:
        print("Error: {}".format(e))
