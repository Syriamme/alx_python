#!/usr/bin/env python3

"""
a script that takes in an argument and displays all values 
in the states table of hbtn_0e_0_usa 
where name matches the argument
"""


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

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor
    cursor = db.cursor()

    # Construct the query using user input and format
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"

    # Execute the query to retrieve matching states
    cursor.execute(query, (state_name,))

    # Fetch the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
