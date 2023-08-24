#!/usr/bin/env python3

"""
a script that lists a states from the database htbn_0e_0_usa
The script will take three arguments: username, password and name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <db_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=db_name)

    # Create a cursor
    cursor = db.cursor()

    # Execute a query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
