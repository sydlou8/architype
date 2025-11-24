from sqlmodel import Field
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders

class Chef(Character):
    DESC = """
    A skilled chef who uses culinary arts to enhance allies and debilitate foes.
    His dishes can provide buffs or inflict status effects in battle.
    """
    role: str = Field(default=CharacterClasses.CHEF.value)
    description: str = Field(default=DESC.strip())
    gender: str = Field(default=Genders.MALE.value)

    # Override Basic Attributes
    max_health: int = Field(default=100)

    # Override Combat Stats
    physical_attack: int = Field(default=15)
    magical_attack: int = Field(default=15)
    physical_defense: int = Field(default=4)
    magical_defense: int = Field(default=4)
    speed: int = Field(default=12)

    # Override Combat Modifiers
    dodge: float = Field(default=0.15)  # 15% dodge chance

    def level_up(self) -> None:
        """Level up the Chef character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 5
        self.physical_attack += 2
        self.magical_attack += 2
        self.physical_defense += 2
        self.magical_defense += 2
        self.speed += 2