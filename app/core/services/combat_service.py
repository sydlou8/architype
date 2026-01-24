"""
Combat Service - Handles turn-based battle logic for Architype
"""
from uuid import uuid4

from models.game.party import Party
from models.game.entities.base_entity import BaseEntity
from models.game.entities.character.character import Character
from models.game.skills.base_skill import BaseSkill


class CombatService:
    """
    Manages turn-based combat between two parties.
    Handles turn order, damage calculation, effect resolution, and win conditions.
    """
    
    def __init__(self, player_party: Party, enemy_party: Party):
        """
        Initialize a new combat encounter.
        
        Args:
            player_party: The player's party
            enemy_party: The enemy party
        """
        self.battle_id: UUID = uuid4()
        self.player_party: Party = player_party
        self.enemy_party: Party = enemy_party
        self.turn_count: int = 0
        self.battle_log: list[str] = []
        self.is_active: bool = True
        
    def start_battle(self) -> dict:
        """
        Start the battle and return initial state.
        
        Returns:
            dict: Initial battle state
        """
        self.battle_log.append("=== BATTLE START ===")
        self.battle_log.append(f"Player Party: {len(self.player_party.members)} members")
        self.battle_log.append(f"Enemy Party: {len(self.enemy_party.members)} members")
        
        return self.get_battle_state()
    
    def get_turn_order(self) -> list[tuple[BaseEntity, str]]:
        """
        Calculate turn order based on speed stat.
        
        Returns:
            list: Entities in turn order with their party affiliation [(entity, "player"|"enemy"), ...]
        """
        all_entities = []
        
        # Add player entities
        for member in self.player_party.get_alive_members():
            all_entities.append((member, "player"))
        
        # Add enemy entities
        for member in self.enemy_party.get_alive_members():
            all_entities.append((member, "enemy"))
        
        # Sort by speed (highest first)
        all_entities.sort(key=lambda x: x[0].current_speed, reverse=True)
        
        return all_entities
    
    def execute_turn(self, attacker: BaseEntity, skill: BaseSkill, target: BaseEntity) -> dict:
        """
        Execute a single turn of combat.
        
        Args:
            attacker: The entity performing the action
            skill: The skill being used
            target: The target of the skill
            
        Returns:
            dict: Result of the turn including damage, effects, and battle state
        """
        if not self.is_active:
            return {"error": "Battle is not active", "battle_state": self.get_battle_state()}
        
        self.turn_count += 1
        turn_result = {
            "turn": self.turn_count,
            "attacker": attacker.role if hasattr(attacker, 'role') else "Enemy",
            "skill": skill.name,
            "target": target.role if hasattr(target, 'role') else "Enemy",
            "actions": []
        }
        
        # Check if target is alive
        if not target.is_alive:
            self.battle_log.append(f"Turn {self.turn_count}: Target is already dead!")
            turn_result["actions"].append("Target is already dead")
            return turn_result
        
        # Use the skill
        try:
            # Skills with use method that returns None (they handle effects internally)
            skill.use(attacker, target)
            
            action_log = f"{attacker.role if hasattr(attacker, 'role') else 'Enemy'} used {skill.name} on {target.role if hasattr(target, 'role') else 'Enemy'}"
            self.battle_log.append(action_log)
            turn_result["actions"].append(action_log)
            
            # Log health changes
            health_log = f"{target.role if hasattr(target, 'role') else 'Enemy'} HP: {target.current_health}/{target.max_health}"
            self.battle_log.append(health_log)
            turn_result["actions"].append(health_log)
            
            # Check if target died
            if not target.is_alive:
                death_log = f"{target.role if hasattr(target, 'role') else 'Enemy'} has been defeated!"
                self.battle_log.append(death_log)
                turn_result["actions"].append(death_log)
                
        except Exception as e:
            error_log = f"Error using skill: {str(e)}"
            self.battle_log.append(error_log)
            turn_result["actions"].append(error_log)
        
        # Resolve effects on all entities
        self._resolve_all_effects()
        
        # Check win condition
        battle_over = self.check_battle_over()
        if battle_over:
            self.is_active = False
            winner = self.get_winner()
            end_log = f"=== BATTLE END === Winner: {winner}"
            self.battle_log.append(end_log)
            turn_result["battle_over"] = True
            turn_result["winner"] = winner
        else:
            turn_result["battle_over"] = False
        
        turn_result["battle_state"] = self.get_battle_state()
        return turn_result
    
    def _resolve_all_effects(self) -> None:
        """
        Resolve effects (tick damage, duration decay) on all entities.
        """
        all_entities = (self.player_party.get_alive_members() + 
                       self.enemy_party.get_alive_members())
        
        for entity in all_entities:
            # Apply tick damage from effects (burn, poison, etc.)
            entity.apply_tick_damage()
            
            # Update effect durations
            entity.resolve_effects()
    
    def check_battle_over(self) -> bool:
        """
        Check if the battle is over.
        
        Returns:
            bool: True if battle is over, False otherwise
        """
        player_alive = len(self.player_party.get_alive_members()) > 0
        enemy_alive = len(self.enemy_party.get_alive_members()) > 0
        
        return not (player_alive and enemy_alive)
    
    def get_winner(self) -> str | None:
        """
        Determine the winner of the battle.
        
        Returns:
            str: "player", "enemy", or "draw"
        """
        player_alive = len(self.player_party.get_alive_members()) > 0
        enemy_alive = len(self.enemy_party.get_alive_members()) > 0
        
        if player_alive and not enemy_alive:
            return "player"
        elif enemy_alive and not player_alive:
            return "enemy"
        else:
            return "draw"
    
    def get_battle_state(self) -> dict:
        """
        Get the current state of the battle.
        
        Returns:
            dict: Complete battle state
        """
        return {
            "battle_id": str(self.battle_id),
            "turn": self.turn_count,
            "is_active": self.is_active,
            "player_party": {
                "members": [
                    {
                        "name": member.role if hasattr(member, 'role') else "Unknown",
                        "level": member.level,
                        "current_health": member.current_health,
                        "max_health": member.max_health,
                        "is_alive": member.is_alive,
                        "active_effects": [
                            {
                                "name": effect.effect_name if hasattr(effect, 'effect_name') else "Unknown",
                                "duration": effect.duration if hasattr(effect, 'duration') else 0
                            }
                            for effect in member.active_effects
                        ]
                    }
                    for member in self.player_party.members
                ],
                "alive_count": len(self.player_party.get_alive_members())
            },
            "enemy_party": {
                "members": [
                    {
                        "name": member.role if hasattr(member, 'role') else "Enemy",
                        "level": member.level,
                        "current_health": member.current_health,
                        "max_health": member.max_health,
                        "is_alive": member.is_alive,
                        "active_effects": [
                            {
                                "name": effect.effect_name if hasattr(effect, 'effect_name') else "Unknown",
                                "duration": effect.duration if hasattr(effect, 'duration') else 0
                            }
                            for effect in member.active_effects
                        ]
                    }
                    for member in self.enemy_party.members
                ],
                "alive_count": len(self.enemy_party.get_alive_members())
            },
            "battle_log": self.battle_log[-10:]  # Last 10 log entries
        }
    
    def auto_battle(self, max_turns: int = 50) -> dict:
        """
        Automatically execute battle turns until completion or max_turns reached.
        Each side attacks the first alive enemy.
        
        Args:
            max_turns: Maximum number of turns before forcing a draw
            
        Returns:
            dict: Final battle result
        """
        self.battle_log.append("=== AUTO BATTLE START ===")
        
        turn = 0
        while self.is_active and turn < max_turns:
            turn += 1
            
            # Get turn order
            turn_order = self.get_turn_order()
            
            for entity, party_type in turn_order:
                if not self.is_active:
                    break
                
                # Determine target party
                if party_type == "player":
                    target_party = self.enemy_party
                else:
                    target_party = self.player_party
                
                # Get first alive target
                alive_targets = target_party.get_alive_members()
                if not alive_targets:
                    break
                
                target = alive_targets[0]
                
                # Get first available skill (assuming characters have skills)
                if hasattr(entity, 'skills') and entity.skills:
                    # Get first skill from the skills dict
                    skill = list(entity.skills.values())[0] if entity.skills else None
                    if skill:
                        self.execute_turn(entity, skill, target)
                
                # Check if battle ended
                if self.check_battle_over():
                    self.is_active = False
                    break
        
        if turn >= max_turns:
            self.battle_log.append(f"Battle ended after {max_turns} turns (draw)")
            self.is_active = False
        
        return {
            "final_state": self.get_battle_state(),
            "winner": self.get_winner(),
            "turns_taken": turn
        }
