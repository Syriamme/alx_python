#!/usr/bin/env python3

"""
a script that lists a states from the database htbn_0e_0_usa
The script will take three arguments: username, password and name
"""

import MySQLdb
import sys

if __name__ == "__main__":
    #checking the 3 arguments
    if len(sys.argv) != 4:
        sys.exit(1)

    mysql_usname = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_nm = sys.argv[3]


    # Connecting to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user_name=mysql_usname,
        password=mysql_pass,
        dtname=db_nm
    )
    # Creating a cursor
    cursor = db.cursor()

    # Executing a query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching the results
    results = cursor.fetchall()

    # Printing the results
    for row in results:
        print(row)

    # Closing the connection and cursor
    cursor.close()
    db.close()
