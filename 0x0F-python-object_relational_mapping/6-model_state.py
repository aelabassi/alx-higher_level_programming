#!/usr/bin/python3
"""
connect to the database using sqlalchemy emgine

"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
    Base.metadata.create_all(engine)
