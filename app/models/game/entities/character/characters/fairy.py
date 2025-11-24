from sqlmodel import Field
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders

class Fairy(Character):
    DESC = """
    The Fairy character is whimsical and enchanting, possessing magical abilities that can heal allies and mame enemies.
    They are agile and have a high chance to dodge attacks, making them elusive in battle.
    Fairies excel in magical attack and speed, but have lower physical defense.
    """
    role: str = Field(default=CharacterClasses.FAIRY.value)
    description: str = Field(default=DESC)
    gender: str = Field(default=Genders.FEMALE.value)

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