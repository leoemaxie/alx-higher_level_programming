#!/usr/bin/python3
if __name__ == "__main__":
    """lists all State objects that contain the letter a from the database hbtn_0e_6_usa"""
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like('%a%')).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
