#!/usr/bin/env python3

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> <db_name> <state_name>")
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

    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"

    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
