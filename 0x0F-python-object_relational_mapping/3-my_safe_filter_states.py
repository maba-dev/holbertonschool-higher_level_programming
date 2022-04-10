#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa: """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE %s", (argv[4],))
    for i in cur.fetchall():
        if i[1] == argv[4]:
            print(i)

    cur.close()
    db.close()
