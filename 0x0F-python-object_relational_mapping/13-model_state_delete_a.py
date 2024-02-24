if __name__ == "__main__":
    """deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa"""
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        db_name = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, db_name),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).filter(State.name.like('%a%')).all()
        for state in states:
            session.delete(state)
        session.commit()
        session.close()
    else:
        print("Usage: {} username password database".format(argv[0]))