from sqlmodel import Field
from models.entities.character.character import Character
from models.enums.character_classes import CharacterClasses

class Fairy(Character):
    role: str = Field(default=CharacterClasses.FAIRY.value)

    # Override Basic Attributes
    max_health: int = Field(default=50)

    # Override Combat Stats
    physical_attack: int = Field(default=0)
    magical_attack: int = Field(default=20)
    physical_defense: int = Field(default=5)
    magical_defense: int = Field(default=10)
    speed: int = Field(default=15)

    # Override Combat Modifiers
    dodge: float = Field(default=0.3)  # 30% dodge chance
    critical_chance: float = Field(default=0.3) # 30% critical hit chance

    def level_up(self) -> None:
        """Level up the Fairy Character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 7
        self.physical_attack += 0
        self.magical_attack += 5
        self.physical_defense += 1
        self.magical_defense += 3
        self.speed += 4