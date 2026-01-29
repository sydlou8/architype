from abc import ABC, abstractmethod
from typing import Any, TYPE_CHECKING
from sqlmodel import Field

from models.game.entities.base_entity import BaseEntity
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.stat_types import StatType
from models.game.enums.skill_types import SkillType
from models.game.enums.effect_types import EffectType, effect_registry, register_effect
from models.game.effects.applied_effect import AppliedEffect

if TYPE_CHECKING:
    from models.game.skills.base_skill import BaseSkill

class Character(BaseEntity, ABC):
    role: str | None = None 
    current_experience: int = Field(default=0)
    max_experience: int = Field(default=100)
    # skills --> this will be a dictionary of skill names as enums and function of the skill
    # characters can only have 4 skills at a time
    skills: dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id),
            "role": self.role,
            "level": self.level,
            "current_health": self.current_health,
            "max_health": self.max_health,
            "is_alive": self.is_alive,
            "current_experience": self.current_experience,
            "max_experience": self.max_experience,
            "skills": list(self.skills.keys()),
            "active_effects": list(self.active_effects.keys()),
        }

    def from_dict(self, data: dict[str, Any]) -> "Character":
        self.id = data.get("id", self.id)
        self.level = data.get("level", self.level)
        self.current_health = data.get("current_health", self.current_health)
        self.max_health = data.get("max_health", self.max_health)
        self.is_alive = data.get("is_alive", self.is_alive)
        self.current_experience = data.get("current_experience", self.current_experience)
        self.max_experience = data.get("max_experience", self.max_experience)
        # skills would need to be handled separately
        return self
    
    def level_up(self) -> None:
        """Level up the character, increasing stats accordingly."""
        self.level += 1
        self.current_experience = 0
        self.max_experience = int(self.max_experience * 1.5)  # Increase required XP for next level
    
    def attack(self, skill: "BaseSkill", target: BaseEntity) -> None:
        damage = skill.use(self, target)
        target.take_damage(damage)

    def defend(self) -> None:
        applied_effect = AppliedEffect(
            effect_name=EffectType.DEFEND.value,
            description="Increases defense for one turn.",
            target=StatType.PHYSICAL_DEFENSE,
            is_unique_effect=True,
            stat_magnifier=5.0,
            duration=1
        )
        self.add_effect(applied_effect)

    def take_damage(self, amount: int) -> None:
        """Apply damage to the character."""
        if amount < 0:
            amount = 0
        self.current_health = max(0, self.current_health - amount)
        self.is_alive = self.check_alive()
    
    def heal(self, amount: int) -> None:
        """Heal the character."""
        if amount < 0:
            amount = 0
        # Apply healing modifier
        healing = int(amount * self.current_healing_modifier)
        self.current_health = min(self.max_health, self.current_health + healing)
        self.is_alive = self.check_alive()

    def equip_skill(self, skill_enum, skill_instance: "BaseSkill") -> bool:
        """
        Equip a skill to the character's loadout.
        
        Args:
            skill_enum: The enum representing the skill
            skill_instance: The instantiated skill object
            
        Returns:
            bool: True if skill was equipped successfully, False otherwise
        """
        # Check if character already has 4 skills
        if len(self.skills) >= 4:
            return False
        
        # Get the skill name (enum value) as the key
        skill_name = skill_enum.value
        
        # Check if skill is already equipped
        if skill_name in self.skills:
            return False
        
        # Equip the skill
        self.skills[skill_name] = skill_instance
        return True
    
    def unequip_skill(self, skill_name: str) -> bool:
        """
        Unequip a skill from the character's loadout.
        
        Args:
            skill_name: The name (enum value) of the skill to remove
            
        Returns:
            bool: True if skill was unequipped successfully, False otherwise
        """
        if skill_name not in self.skills:
            return False
        
        del self.skills[skill_name]
        return True
    
    def swap_skill(self, old_skill_name: str, new_skill_enum, new_skill_instance: "BaseSkill") -> bool:
        """
        Swap one skill for another atomically.
        
        Args:
            old_skill_name: The name (enum value) of the skill to replace
            new_skill_enum: The enum representing the new skill
            new_skill_instance: The instantiated new skill object
            
        Returns:
            bool: True if swap was successful, False otherwise
        """
        # Verify old skill exists
        if old_skill_name not in self.skills:
            return False
        
        new_skill_name = new_skill_enum.value
        
        # Check if new skill is already equipped
        if new_skill_name in self.skills:
            return False
        
        # Perform atomic swap
        del self.skills[old_skill_name]
        self.skills[new_skill_name] = new_skill_instance
        return True