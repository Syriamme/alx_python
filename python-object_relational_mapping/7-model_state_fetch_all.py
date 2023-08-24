#!/usr/bin/env python3
"""
Script to list all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states(username, password, db_name):
    """List all State objects from the database."""
    # Create a connection to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query the State objects and sort by states.id
    states = session.query(State).order_by(State.id).all()
    
    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <db_name>")
        sys.exit(1)
    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    
    # Importing these here to ensure the script isn't executed on import
    from model_state import Base, State
    
    list_states(mysql_username, mysql_password, db_name)
