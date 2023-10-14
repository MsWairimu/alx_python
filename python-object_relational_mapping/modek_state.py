# Import SQLAlchemy module
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()

# Define a State class that inherits from Base
class State(Base):
    # Link to the MySQL table states
    __tablename__ = 'states'
    # Define the class attributes id and name
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

# Connect to a MySQL server running on localhost at port 3306
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa')

# Import all classes who inherit from Base before calling Base.metadata.create_all(engine)
from model_state import State

# Create all tables in the engine
Base.metadata.create_all(engine)
