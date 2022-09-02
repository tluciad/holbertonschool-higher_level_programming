#!/usr/bin/python3
""""lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    """module to order display 1rst state"""

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3])
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')):

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
