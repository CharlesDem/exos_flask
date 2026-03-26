"""
Modèle SQLAlchemy représentant la table Player.
"""

from enum import Enum

from sqlalchemy import Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base



class Player(Base):
    """
    Modèle ORM utilisateur.

    Cette classe décrit la structure de la table player. Un player n'est pas forcément un user
    """

    __tablename__ = "player"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nickname: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

