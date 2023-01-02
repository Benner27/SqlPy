import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Trail to contemporary directory
base_dir = os.path.dirname(os.path.realpath(__file__))

# Invents database URL
db_uri = "sqlite:///" + os.path.join(base_dir, 'main.db')

# Engine development
engine = create_engine(db_uri)

# Establishes session for performing crud
Session = sessionmaker()

# Produces base class used to fabricate model classes
Base = declarative_base()

