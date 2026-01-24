from sqlmodel import Field
from typing import ClassVar
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders

class Biker(Character):
    DESC: ClassVar[str] = """
    A tough biker who relies on brute strength and resilience.
    She excels in physical combat and can take a lot of damage.
    """
    role: str = Field(default=CharacterClasses.BIKER.value)
    description: str = Field(default=DESC.strip())
    gender: str = Field(default=Genders.FEMALE.value)
    
    # Override Basic Attributes
    max_health: int = Field(default=130)

    # Override Combat Stats
    physical_attack: int = Field(default=17)
    magical_attack: int = Field(default=0)
    physical_defense: int = Field(default=11)
    magical_defense: int = Field(default=5)
    speed: int = Field(default=17)

    def level_up(self) -> None:
        """Level up the biker character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 9
        self.physical_attack += 5
        self.magical_attack += 0
        self.physical_defense += 2
        self.magical_defense += 0
        self.speed += 4