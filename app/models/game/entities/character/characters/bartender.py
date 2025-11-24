from sqlmodel import Field
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders

class Bartender(Character):
    DESC = """
    A charming bartender with a knack for mixology.
    She uses creates concoctions that can both heal, empower, or poison.
    """
    role: str = Field(default=CharacterClasses.BARTENDER.value)
    description: str = Field(default=DESC.strip())
    gender: str = Field(default=Genders.FEMALE.value)
    
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
        self.max_health += 9
        self.physical_attack += 1
        self.magical_attack += 4
        self.physical_defense += 1
        self.magical_defense += 2
        self.speed += 3