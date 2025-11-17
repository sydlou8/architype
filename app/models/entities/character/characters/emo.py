from typing import Any
from sqlmodel import Field

from models.entities.skills.base_skill import Skill
from models.entities.base_entity import BaseEntity
from models.entities.character.character import Character
from models.entities.enums.character_classes import CharacterClasses

class Emo(Character):
    role: str = Field(default=CharacterClasses.EMO.value)

    # Override Basic Attributes
    max_health: int = Field(default=120)

    # Override Combat Stats
    physical_attack: int = Field(default=8)
    magical_attack: int = Field(default=8)
    physical_defense: int = Field(default=8)
    magical_defense: int = Field(default=14)
    speed: int = Field(default=12)

    def level_up(self) -> None:
        """Level up the Emo Character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 10
        self.physical_attack += 2
        self.magical_attack += 2
        self.physical_defense += 2
        self.magical_defense += 2
        self.speed += 2
    
    def attack(self, skill: Skill, target: BaseEntity) -> None:
        skill.use(self, target)

    def defend(self, damage: int) -> None:
        pass  # Implementation of defend logic
    
    def take_damage(self, amount: int) -> None:
        pass  # Implementation of take damage logic
    
    def heal(self, amount: int) -> None:
        pass  # Implementation of heal logic