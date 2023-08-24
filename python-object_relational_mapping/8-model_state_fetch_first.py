#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    user = sys.argv[1]
    passwd = sys.argv[2]
    db_nm = sys.argv[3]

    connecting_string = (f'mysql+mysqldb://{user}:{passwd}'
                         f'@localhost:3306/{db_nm}')
    engine = create_engine(connecting_string)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
        session.close()
