#!/usr/bin/python3

'''
Script that takes in the name of a state as an argument
and lists all cities of that state.

The script should take 4 arguments: mysql username,
mysql password, database name, and state name.
'''

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py mysql_username mysql_password database_name state_name")
        sys.exit(1)

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Fetch cities of the provided state
    cursor.execute("""SELECT cities.id, cities.name, states.name
                      FROM cities
                      JOIN states ON cities.state_id = states.id
                      WHERE states.name = %s
                      ORDER BY cities.id ASC""", (sys.argv[4],))

    # Fetch and format the results
    cities = [city[1] for city in cursor.fetchall()]
    print(", ".join(cities))

    # Close the cursor and the connection
    cursor.close()
    db.close()
