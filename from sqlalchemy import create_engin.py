from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create an engine to connect to a SQLite database
engine = create_engine('sqlite:///t20_cricket.db', echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define the Match entity
class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    batting_team = Column(String)
    bowling_team = Column(String)
    overs_played = Column(Integer)
    runs_scored = Column(Integer)
    wickets_fallen = Column(Integer)
    venue_id = Column(Integer, ForeignKey('venues.id'))

    venue = relationship("Venue", back_populates="matches")
    prediction = relationship("Prediction", uselist=False, back_populates="match")

# Define the Team entity
class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    captain = Column(String)
    coach = Column(String)
    players = relationship("Player", back_populates="team")

# Define the Player entity
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    team_id = Column(Integer, ForeignKey('teams.id'))

    team = relationship("Team", back_populates="players")

# Define the Venue entity
class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    matches = relationship("Match", back_populates="venue")

# Define the Prediction entity
class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True)
    predicted_score = Column(Integer)
    actual_score = Column(Integer)
    match_id = Column(Integer, ForeignKey('matches.id'))

    match = relationship("Match", back_populates="prediction")

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
