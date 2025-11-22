from sqlmodel import Field
from models.entities.character.character import Character
from models.enums.character_classes import CharacterClasses

class GranolaBoy(Character):
    role: str = Field(default=CharacterClasses.GRANOLA_BOY.value)

    # Override Basic Attributes
    max_health: int = Field(default=100)

    # Override Combat Stats
    physical_attack: int = Field(default=10)
    magical_attack: int = Field(default=0)
    physical_defense: int = Field(default=20)
    magical_defense: int = Field(default=10)
    speed: int = Field(default=10)

    def level_up(self) -> None:
        """Level up the Granola Boy Character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 8
        self.physical_attack += 3
        self.magical_attack += 0
        self.physical_defense += 5
        self.magical_defense += 2
        self.speed += 2