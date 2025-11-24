from models.game.entities.character.character import Character

class Musician(Character):
    role: str = Field(default=CharacterClasses.MUSICIAN.value)

    # Override Basic Attributes
    max_health: int = Field(default=60)

    # Override Combat Stats
    physical_attack: int = Field(default=5)
    magical_attack: int = Field(default=12)
    physical_defense: int = Field(default=8)
    magical_defense: int = Field(default=10)
    speed: int = Field(default=15)

    # Override Combat Modifiers
    dodge: float = Field(default=0.3)  # 30% dodge chance

    def level_up(self) -> None:
        """Level up the Musician Character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 5
        self.physical_attack += 1
        self.magical_attack += 5
        self.physical_defense += 2
        self.magical_defense += 2
        self.speed += 5