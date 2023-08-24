#!/usr/bin/env python3
"""
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
