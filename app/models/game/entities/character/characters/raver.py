from sqlmodel import Field
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders

class Raver(Character):
    DESC = """
    The Raver class is known for their high energy and agility, making them elusive targets in combat.
    They possess a balanced mix of physical and magical abilities, allowing them to adapt to various combat situations, however, 
    they focus more on physical attacks. Their high dodge rate makes them difficult to hit.
    """
    role: str = Field(default=CharacterClasses.RAVER.value)
    description: str = Field(default=DESC.strip())
    gender: str = Field(default=Genders.FEMALE.value)

    # Override Basic Attributes
    max_health: int = Field(default=90)

    # Override Combat Stats
    physical_attack: int = Field(default=16)
    magical_attack: int = Field(default=7)
    physical_defense: int = Field(default=5)
    magical_defense: int = Field(default=6)
    speed: int = Field(default=16)

    # Override Combat Modifiers
    dodge: float = Field(default=0.25)  # 25% dodge chance

    def level_up(self) -> None:
        """Level up the Raver Character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 4
        self.physical_attack += 5
        self.magical_attack += 2
        self.physical_defense += 2
        self.magical_defense += 2
        self.speed += 5