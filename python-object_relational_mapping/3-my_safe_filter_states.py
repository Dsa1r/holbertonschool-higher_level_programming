#!/usr/bin/python3
"""
This script safely displays states where the name matches a user input
from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (argv[4],)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
