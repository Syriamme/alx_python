#!/usr/bin/python3

"""
a script that lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    usnm = sys.argv[1]
    passwd = sys.argv[2]
    db_nm = sys.argv[3]

    connecting_string = (f'mysql+mysqldb://{usnm}:{passwd}'
                         f'@localhost:3306/{db_nm}')
    engine = create_engine(connecting_string)

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State)
    states_with_a = query.filter(State.name.contains('a')).order_by(State.id)

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
