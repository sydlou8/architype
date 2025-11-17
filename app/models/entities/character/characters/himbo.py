from models.entities.character.character import Character

class Himbo(Character):
    role: str = Field(default=CharacterClasses.HIMBO.value)

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
        self.max_health += 12
        self.physical_attack += 3
        self.magical_attack += 0
        self.physical_defense += 2
        self.magical_defense += 1
        self.speed += 2