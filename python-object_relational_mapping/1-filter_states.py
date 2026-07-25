#!/usr/bin/python3
"""Lists states with names starting with N from a MySQL database."""

import MySQLdb
import sys


if __name__ == "__main__":
    """Connects to MySQL and prints filtered states."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
