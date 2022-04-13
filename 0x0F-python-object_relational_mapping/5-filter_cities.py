#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_4_usa: """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s", (argv[4],))
    result = []
    for i in cur.fetchall():
        result.append(i[0])
    print(", ".join(result))
    cur.close()
    db.close()
