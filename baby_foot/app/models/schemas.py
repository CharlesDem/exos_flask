"""
Schémas Pydantic utilisés pour valider les entrées/sorties de l'API.
"""

from typing import List, Optional

from pydantic import BaseModel, Field

#   "password": "pass1234TT("
class UserRegister(BaseModel):
    """
    Données attendues pour l'inscription d'un nouvel utilisateur.
    """
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=2, max_length=100)
    password: str = Field(..., min_length=6, max_length=128)

class PlayerCreate(BaseModel):
    nickname: str = Field(..., min_length=3, max_length=25)
    user_id: Optional[int] = None

class PlayerResponse(BaseModel):
    id: int
    nickname: str = Field(..., min_length=3, max_length=25)
    user_id: Optional[int] = None

class TeamCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=25)
    players: List[int] = Field(..., min_length=1, max_length=2)

class TeamResponse(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=25)

class MatchCreate(BaseModel):
    winner_team_id: Optional[int] = None
    teams: List[int] = Field(..., min_length=2, max_length=2)

class UserLogin(BaseModel):
    """
    Données attendues pour la connexion.
    """
    username: str
    password: str


class UserPublic(BaseModel):
    """
    Représentation publique d'un utilisateur.
    Aucun mot de passe ni hash ne doit sortir ici.
    """
    id: int
    username: str
    full_name: str
    role: str
    is_active: bool

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    """
    Réponse renvoyée après un login ou un refresh.
    """
    access_token: str
    token_type: str = "bearer"


class MessageResponse(BaseModel):
    """
    Petit schéma utilitaire pour les réponses simples.
    """
    message: str


class LoginResponse(TokenResponse):
    """
    Variante un peu plus riche de la réponse de login, pour que l'utilisateur
    sache immédiatement quel compte il vient d'authentifier.
    """
    user: UserPublic
    expires_in: int
