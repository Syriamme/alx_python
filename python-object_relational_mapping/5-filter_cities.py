#!/usr/bin/python3
""" List all cities from a state """

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py mysql_username mysql_password database_name state_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", 
                          port=3306, 
                          user=username, 
                          passwd=password, 
                          db=db_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Query for all cities in the provided state
    query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the results
    rows = cursor.fetchall()

    if not rows:
        print("No cities found for the state:", state_name)
    else:
        for row in rows:
            print("{}: {}".format(row[0], row[1]))

    # Close the cursor and the connection
    cursor.close()
    db.close()
