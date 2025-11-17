from typing import Any
from sqlmodel import Field

from models.entities.skills.base_skill import Skill
from models.entities.base_entity import BaseEntity
from models.entities.character.character import Character
from models.entities.enums.character_classes import CharacterClasses

class Bartender(Character):
    role: str = Field(default=CharacterClasses.BARTENDER.value)
    
    # Override Basic Attributes
    max_health: int = Field(default=90)

    # Override Combat Stats
    physical_attack: int = Field(default=5)
    magical_attack: int = Field(default=16)
    physical_defense: int = Field(default=7)
    magical_defense: int = Field(default=10)
    speed: int = Field(default=12)

    # Override Combat Modifiers
    dodge: float = Field(default=0.2)  # 20% dodge chance

    def level_up(self) -> None:
        """Level up the Bartender character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 10
        self.physical_attack += 1
        self.magical_attack += 3
        self.physical_defense += 1
        self.magical_defense += 2
        self.speed += 3

    def attack(self, skill: Skill, target: BaseEntity) -> None:
        skill.use(self, target)

    def defend(self, damage: int) -> None:
        pass  # Implementation of defend logic
    
    def take_damage(self, amount: int) -> None:
        pass  # Implementation of take damage logic
    
    def heal(self, amount: int) -> None:
        pass  # Implementation of heal logic