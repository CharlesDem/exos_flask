from typing import Optional

from app.models.player import Player
from sqlalchemy.orm import Session


def create_player(db: Session, nickname:str, user_id: Optional[int]):
    
    player = Player(
        nickname=nickname,
        user_id=user_id
    )

    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def get_player_by_name(db: Session, nickname: str):
    return db.query(Player).filter(Player.nickname == nickname).first()

def get_players(db: Session):
    return db.query(Player).all()