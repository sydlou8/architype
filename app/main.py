"""
Architype - FastAPI Application
A turn-based RPG fighting game with queer archetype characters
"""
import sys
from pathlib import Path

# Add app directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from uuid import uuid4
from datetime import timedelta

from models.game.party import Party
from models.game.entities.character.characters.barista import Barista
from models.game.entities.character.characters.drag_queen import DragQueen
from models.game.entities.character.characters.emo import Emo
from models.game.entities.character.characters.jock import Jock
from models.game.entities.character.characters.raver import Raver
from core.services.combat_service import CombatService

# Auth imports
from models.user.user import User, UserCreate, UserLogin, UserResponse, Token
from core.auth.auth_utils import (
    verify_password, 
    get_password_hash, 
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from core.auth.dependencies import get_current_active_user, fake_users_db

# Initialize FastAPI app
app = FastAPI(
    title="Architype API",
    description="Turn-based RPG fighting game API",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for active battles
# TODO: Replace with database in production
active_battles: dict[str, CombatService] = {}

# Available character classes
AVAILABLE_CHARACTERS = {
    "barista": Barista,
    "drag_queen": DragQueen,
    "emo": Emo,
    "jock": Jock,
    "raver": Raver,
}


# ============================================================================
# Request/Response Models
# ============================================================================

class StartBattleRequest(BaseModel):
    player_characters: list[str] = ["barista", "jock", "emo"]  # Character class names
    enemy_characters: list[str] = ["drag_queen", "raver"]


class ExecuteTurnRequest(BaseModel):
    attacker_index: int  # Index of attacking character in party
    target_index: int    # Index of target in enemy party
    damage: int = 15     # Damage amount (temporary - will use skills later)


# ============================================================================
# Authentication Endpoints
# ============================================================================

@app.post("/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate):
    """
    Register a new user account
    
    Args:
        user_data: Username, email, and password
        
    Returns:
        Created user information (without password)
    """
    # Check if username already exists
    if user_data.username in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Check if email already exists
    for user in fake_users_db.values():
        if user.email == user_data.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    
    # Create new user
    hashed_password = get_password_hash(user_data.password)
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )
    
    # Store user (in-memory for now)
    fake_users_db[new_user.username] = new_user
    
    return UserResponse(
        id=new_user.id,
        username=new_user.username,
        email=new_user.email,
        is_active=new_user.is_active,
        created_at=new_user.created_at
    )


@app.post("/auth/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login and receive JWT access token
    
    Args:
        form_data: Username and password (OAuth2 form)
        
    Returns:
        JWT access token
    """
    # Get user
    user = fake_users_db.get(form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verify password
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, 
        expires_delta=access_token_expires
    )
    
    return Token(access_token=access_token, token_type="bearer")


@app.get("/auth/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    """
    Get current authenticated user information
    
    Requires valid JWT token in Authorization header
    """
    return UserResponse(
        id=current_user.id,
        username=current_user.username,
        email=current_user.email,
        is_active=current_user.is_active,
        created_at=current_user.created_at
    )


# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/")
def root():
    """Health check endpoint"""
    return {
        "message": "Architype API is running!",
        "version": "0.1.0",
        "status": "healthy"
    }


@app.get("/health")
def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "active_battles": len(active_battles),
        "available_characters": list(AVAILABLE_CHARACTERS.keys())
    }


@app.get("/characters")
def list_characters():
    """List all available character classes"""
    characters = []
    for name, char_class in AVAILABLE_CHARACTERS.items():
        # Create temporary instance to get stats
        temp = char_class()
        characters.append({
            "name": name,
            "class": temp.role if hasattr(temp, 'role') else name,
            "description": temp.description if hasattr(temp, 'description') else "",
            "max_health": temp.max_health,
            "physical_attack": temp.physical_attack,
            "magical_attack": temp.magical_attack,
            "speed": temp.speed,
            "dodge": temp.dodge,
        })
    return {"characters": characters}


@app.post("/battle/start")
def start_battle(request: StartBattleRequest):
    """
    Start a new battle with selected characters
    
    Returns battle_id and initial state
    """
    # Validate character names
    for char_name in request.player_characters + request.enemy_characters:
        if char_name not in AVAILABLE_CHARACTERS:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid character: {char_name}. Available: {list(AVAILABLE_CHARACTERS.keys())}"
            )
    
    # Create player party
    player_members = [AVAILABLE_CHARACTERS[name]() for name in request.player_characters]
    player_party = Party(members=player_members)
    
    # Create enemy party
    enemy_members = [AVAILABLE_CHARACTERS[name]() for name in request.enemy_characters]
    enemy_party = Party(members=enemy_members)
    
    # Initialize combat
    combat = CombatService(player_party, enemy_party)
    initial_state = combat.start_battle()
    
    # Store battle
    battle_id = str(combat.battle_id)
    active_battles[battle_id] = combat
    
    return {
        "message": "Battle started!",
        "battle_id": battle_id,
        "battle_state": initial_state
    }


@app.get("/battle/{battle_id}")
def get_battle_state(battle_id: str):
    """Get current state of a battle"""
    if battle_id not in active_battles:
        raise HTTPException(status_code=404, detail="Battle not found")
    
    combat = active_battles[battle_id]
    return combat.get_battle_state()


@app.post("/battle/{battle_id}/turn")
def execute_turn(battle_id: str, request: ExecuteTurnRequest):
    """
    Execute a turn in the battle
    
    The attacker deals damage to the target
    """
    if battle_id not in active_battles:
        raise HTTPException(status_code=404, detail="Battle not found")
    
    combat = active_battles[battle_id]
    
    if not combat.is_active:
        return {
            "error": "Battle is already over",
            "winner": combat.get_winner(),
            "battle_state": combat.get_battle_state()
        }
    
    # Get attacker from player party
    player_members = combat.player_party.get_alive_members()
    if request.attacker_index >= len(player_members):
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid attacker index. Available: 0-{len(player_members)-1}"
        )
    
    attacker = player_members[request.attacker_index]
    
    # Get target from enemy party
    enemy_members = combat.enemy_party.get_alive_members()
    if request.target_index >= len(enemy_members):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid target index. Available: 0-{len(enemy_members)-1}"
        )
    
    target = enemy_members[request.target_index]
    
    # Execute attack (simple damage for now)
    combat.turn_count += 1
    
    attacker_name = attacker.role if hasattr(attacker, 'role') else "Player"
    target_name = target.role if hasattr(target, 'role') else "Enemy"
    
    # Apply damage
    target.take_damage(request.damage)
    
    combat.battle_log.append(
        f"Turn {combat.turn_count}: {attacker_name} attacks {target_name} for {request.damage} damage"
    )
    combat.battle_log.append(
        f"{target_name} HP: {target.current_health}/{target.max_health}"
    )
    
    if not target.is_alive:
        combat.battle_log.append(f"{target_name} has been defeated!")
    
    # Resolve effects
    combat._resolve_all_effects()
    
    # Check if battle is over
    battle_over = combat.check_battle_over()
    if battle_over:
        combat.is_active = False
        winner = combat.get_winner()
        combat.battle_log.append(f"=== BATTLE END === Winner: {winner}")
    
    return {
        "turn": combat.turn_count,
        "action": f"{attacker_name} attacked {target_name} for {request.damage} damage",
        "battle_over": battle_over,
        "winner": combat.get_winner() if battle_over else None,
        "battle_state": combat.get_battle_state()
    }


@app.delete("/battle/{battle_id}")
def end_battle(battle_id: str):
    """End a battle and clean up resources"""
    if battle_id not in active_battles:
        raise HTTPException(status_code=404, detail="Battle not found")
    
    del active_battles[battle_id]
    return {"message": "Battle ended and cleaned up"}


@app.get("/battles")
def list_active_battles():
    """List all active battles"""
    battles = []
    for battle_id, combat in active_battles.items():
        battles.append({
            "battle_id": battle_id,
            "turn": combat.turn_count,
            "is_active": combat.is_active,
            "player_alive": len(combat.player_party.get_alive_members()),
            "enemy_alive": len(combat.enemy_party.get_alive_members())
        })
    return {"active_battles": battles, "count": len(battles)}


# ============================================================================
# Run with: uvicorn app.main:app --reload
# ============================================================================