from sqlmodel import Field
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders

class GranolaBoy(Character):
    DESC = """
    The Granola Boy is a rugged outdoorsman who thrives in natural environments.
    He is resilient and strong, with a deep connection to nature that enhances his and his party's abilities.
    They utilize traps and gadgets to control the battlefield, making them formidable opponents.
    """
    role: str = Field(default=CharacterClasses.GRANOLA_BOY.value)
    description: str = Field(default=DESC.strip())
    gender: str = Field(default=Genders.MALE.value)

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