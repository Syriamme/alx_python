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

    query = ("SELECT * "
             "FROM states "
             "WHERE BINARY name = '{}' "
             "ORDER BY id ASC").format(ste_nm)

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
