from sqlmodel import Field
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders

class Himbo(Character):
    DESC = """
    The Himbo is a strong and charismatic character known for his physical prowess and charm.
    He excels in close combat and has a natural ability to inspire and lead his allies.
    Despite his muscular build, the Himbo is surprisingly agile and quick on his feet.
    """
    role: str = Field(default=CharacterClasses.HIMBO.value)
    description: str = Field(default=DESC.strip())
    gender: str = Field(default=Genders.MALE.value)

    # Override Basic Attributes
    max_health: int = Field(default=120)

    # Override Combat Stats
    physical_attack: int = Field(default=20)
    magical_attack: int = Field(default=0)
    physical_defense: int = Field(default=15)
    magical_defense: int = Field(default=5)
    speed: int = Field(default=10)

    def level_up(self) -> None:
        """Level up the Himbo character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 8
        self.physical_attack += 5
        self.magical_attack += 0
        self.physical_defense += 4
        self.magical_defense += 1
        self.speed += 2