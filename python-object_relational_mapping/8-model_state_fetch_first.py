# Import SQLAlchemy module
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import State and Base from model_state
from model_state import Base, State
# Import sys module to access command line arguments
import sys

if __name__ == "__main__":
    # Create an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create a session object to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query the first State object and assign it to a variable
    first_state = session.query(State).first()
    # Print the state's id and name if it exists, otherwise print Nothing
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    # Close the session
    session.close()
