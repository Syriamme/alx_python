#!/usr/bin/python3

"""
write one that is safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    mysql_usnm = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_nm = sys.argv[3]
    ste_nm = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_usnm,
        passwd=mysql_pass,
        db=db_nm
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (ste_nm,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
