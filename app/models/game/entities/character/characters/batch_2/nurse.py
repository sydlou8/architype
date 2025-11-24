from models.game.entities.character.character import Character

class Nurse(Character):
    role: str = Field(default=CharacterClasses.NURSE.value)

    # Override Basic Attributes
    max_health: int = Field(default=120)

    # Override Combat Stats
    physical_attack: int = Field(default=5)
    magical_attack: int = Field(default=5)
    physical_defense: int = Field(default=15)
    magical_defense: int = Field(default=15)
    speed: int = Field(default=10)

    def level_up(self) -> None:
        """Level up the Nurse Character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 10
        self.physical_attack += 1
        self.magical_attack += 1
        self.physical_defense += 3
        self.magical_defense += 3
        self.speed += 2