from sqlalchemy import Boolean, Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


association_table = Table(
    "match_teams",
    Base.metadata,
    Column("match_id", ForeignKey("matchs.id"), primary_key=True),
    Column("team_id", ForeignKey("teams.id"), primary_key=True),
)

association_team_player = Table(
    "team_players",
    Base.metadata,
    Column("team_id", ForeignKey("teams.id"), primary_key=True),
    Column("player_id", ForeignKey("player.id"), primary_key=True),
)