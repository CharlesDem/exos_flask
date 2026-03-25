from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./exos/EXO_BLUEPRINT/exo4-test.db")

SessionLocal = sessionmaker(bind=engine)