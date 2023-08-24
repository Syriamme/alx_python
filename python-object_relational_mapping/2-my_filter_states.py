#!/usr/bin/env python3

"""
a script that takes in an argument and displays all values 
in the states table of hbtn_0e_0_usa
where name matches the argument
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

    query = """
    SELECT *
    FROM states
    WHERE name LIKE %s
    ORDER BY id ASC
    """

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
