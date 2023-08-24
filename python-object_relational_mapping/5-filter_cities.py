#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         user_name=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name
                      FROM cities
                      JOIN states ON cities.state_id = states.id
                      WHERE states.name = %s
                      ORDER BY cities.id ASC""", (sys.argv[4],))

    cities = [city[1] for city in cursor.fetchall()]
    print(", ".join(cities))

    cursor.close()
    db.close()
