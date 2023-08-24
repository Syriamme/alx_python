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

    # Create an engine and connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    
    # Create a Session class, bound to this engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query for the first state
    state = session.query(State).order_by(State.id).first()

    # Check if state exists, else print "Nothing"
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
