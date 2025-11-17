from models.entities.character.character import Character

class Jock(Character):
    role: str = Field(default=CharacterClasses.JOCK.value)

    # Override Basic Attributes
    max_health: int = Field(default=60)

    # Override Combat Stats
    physical_attack: int = Field(default=15)
    magical_attack: int = Field(default=15)
    physical_defense: int = Field(default=3)
    magical_defense: int = Field(default=2)
    speed: int = Field(default=15)

    # Override Combat Modifiers
    dodge: float = Field(default=0.2)  # 20% dodge chance
    critical_chance: float = Field(default=0.4) # 40% critical hit chance

    def level_up(self) -> None:
        """Level up the Jock Character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 5
        self.physical_attack += 4
        self.magical_attack += 4
        self.physical_defense += 1
        self.magical_defense += 1
        self.speed += 5
    