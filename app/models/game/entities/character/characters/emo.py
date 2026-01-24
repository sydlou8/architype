from sqlmodel import Field
from typing import ClassVar
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders

class Emo(Character):
    DESC: ClassVar[str] = """
    The Emo character is introspective and artistic, often expressing deep emotions through music and poetry.
    They have the ability to create curses that can weaken their enemies over time.
    Emo characters excel in magical defense and have balanced attack stats, making them versatile in combat.
    """
    role: str = Field(default=CharacterClasses.EMO.value)
    description: str = Field(default=DESC)
    gender: str = Field(default=Genders.NON_BINARY.value)

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
    