from typing import Optional

from app.models.player import Player
from app.models.schemas import TeamCreate
from app.models.team import Team
from sqlalchemy.orm import Session


def create_team(db: Session, team_create: TeamCreate):

    players = db.query(Player).filter(Player.id.in_(team_create.players)).all()
    
    team = Team(
        name=team_create.name,
        players = players
    )

    db.add(team)
    db.commit()
    db.refresh(team)
    return team

def get_player_by_name(db: Session, nickname: str):
    return db.query(Player).filter(Player.nickname == nickname).first()

def get_players(db: Session):
    return db.query(Player).all()