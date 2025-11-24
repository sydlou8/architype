from models.game.entities.character.character import Character

class Coder(Character):
    role: str = Field(default=CharacterClasses.CODER.value)

    # Override Basic Attributes
    max_health: int = Field(default=100)

    # Override Combat Stats
    physical_attack: int = Field(default=2)
    magical_attack: int = Field(default=12)
    physical_defense: int = Field(default=8)
    magical_defense: int = Field(default=18)
    speed: int = Field(default=10)

    def level_up(self) -> None:
        """Level up the Coder character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 10
        self.physical_attack += 1
        self.magical_attack += 2
        self.physical_defense += 1
        self.magical_defense += 4
        self.speed += 2