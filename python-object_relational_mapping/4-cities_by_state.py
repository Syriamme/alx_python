#!/usr/bin/env python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    mysql_usnm = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_nm = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_usnm,
        passwd=mysql_pass,
        db=db_nm
    )

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities JOIN states ON cities.state_id = states.id "
                   "ORDER BY cities.id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
