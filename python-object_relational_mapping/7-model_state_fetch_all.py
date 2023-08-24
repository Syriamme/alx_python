#!/usr/bin/env python3

"""
Script to list all State objects from the database hbtn_0e_6_usa.
"""


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def list_states(username, password, db_name):
    """List all State objects from the database."""
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_nm = sys.argv[3]
    from model_state import Base, State

    list_states(mysql_username, mysql_pwd, db_nm)
