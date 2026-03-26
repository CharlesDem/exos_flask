"""
Modèle SQLAlchemy représentant la table Match.
"""

from enum import Enum

from sqlalchemy import Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.team import Team
from app.models.liaison import association_table


class Match(Base):
    """
    Modèle ORM utilisateur.

    Cette classe décrit la structure de la table match.
    """

    __tablename__ = "matchs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    winner_team_id: Mapped[int | None] = mapped_column(
        ForeignKey("teams.id"),
        nullable=True
    )

    teams: Mapped[list[Team]] = relationship(
        "Team",
        secondary=association_table
    )
