from models.game.entities.character.character import Character

class Academic(Character):
    role: str = Field(default=CharacterClasses.ACADEMIC.value)

    # Override Basic Attributes
    max_health: int = Field(default=90)

    # Override Combat Stats
    physical_attack: int = Field(default=10)
    magical_attack: int = Field(default=13)
    physical_defense: int = Field(default=5)
    magical_defense: int = Field(default=12)
    speed: int = Field(default=10)

    # Override Combat Modifiers
    critical_chance: float = Field(default=0.3) # 30% critical hit chance

    def level_up(self) -> None:
        """Level up the Academic Character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 7
        self.physical_attack += 2
        self.magical_attack += 4
        self.physical_defense += 1
        self.magical_defense += 4
        self.speed += 2
    