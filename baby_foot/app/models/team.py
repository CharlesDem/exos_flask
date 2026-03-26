from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Boolean, Integer, String
from app.core.database import Base
from app.models.liaison import association_team_player


class Team(Base):
    __tablename__ = "teams"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    players = relationship("Player", secondary=association_team_player)