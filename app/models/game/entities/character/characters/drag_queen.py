from sqlmodel import Field
from typing import ClassVar
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders

class DragQueen(Character):
    DESC: ClassVar[str] = """
    A fabulous drag queen who dazzles enemies with charisma and flair.
    She uses her performance skills to gag boot d and charm opponents.
    """
    role: str = Field(default=CharacterClasses.DRAG_QUEEN.value)
    description: str = Field(default=DESC.strip())
    gender: str = Field(default=Genders.MALE.value)

    # Override Basic Attributes
    max_health: int = Field(default=110)

    # Override Combat Stats
    physical_attack: int = Field(default=14)
    magical_attack: int = Field(default=14)
    physical_defense: int = Field(default=10)
    magical_defense: int = Field(default=10)
    speed: int = Field(default=2)

    # Override Combat Modifiers
    def level_up(self) -> None:
        """Level up the Drag Queen character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 7
        self.physical_attack += 4
        self.magical_attack += 4
        self.physical_defense += 2
        self.magical_defense += 2
        self.speed += 1