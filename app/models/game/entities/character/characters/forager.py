from sqlmodel import Field
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders

class Forager(Character):
    DESC = """
    The Forager character is resourceful and skilled at gathering natural materials.
    They have a balanced set of combat abilities with a focus on magical defense.
    Foragers use concoctions they created from foraged plants to aid them in battle.
    """

    role: str = Field(default=CharacterClasses.FORAGER.value)
    description: str = Field(default=DESC)
    gender: str = Field(default

    # Override Combat Stats
    physical_attack: int = Field(default=0)
    magical_attack: int = Field(default=10)
    physical_defense: int = Field(default=10)
    magical_defense: int = Field(default=20)
    speed: int = Field(default=10)

    def level_up(self) -> None:
        """Level up the Forager Character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 8
        self.physical_attack += 0
        self.magical_attack += 3
        self.physical_defense += 2
        self.magical_defense += 5
        self.speed += 2