#!/usr/bin/python3

"""
a script that lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
"""

#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py mysql_username mysql_password database_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create a connection string and then use it for the engine
    connection_string = (f'mysql+mysqldb://{username}:{password}'
                         f'@localhost:3306/{db_name}')
    engine = create_engine(connection_string)

    # Create a Session class, bound to this engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query for states containing the letter 'a' in their names
    query = session.query(State)
    states_with_a = query.filter(State.name.contains('a')).order_by(State.id)

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
