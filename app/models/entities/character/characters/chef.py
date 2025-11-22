from sqlmodel import Field
from models.entities.character.character import Character
from models.enums.character_classes import CharacterClasses

class Chef(Character):
    role: str = Field(default=CharacterClasses.CHEF.value)

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