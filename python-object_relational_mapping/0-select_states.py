#!/usr/bin/env python3

"""
a script that lists a states from the database htbn_0e_0_usa
The script will take three arguments: username, password and name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    mysql_usname = sys.argv[1]
    mysql_pass = sys.argv[2]
    dbt_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_usname,
        passwd=mysql_pass,
        db=dbt_name
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
