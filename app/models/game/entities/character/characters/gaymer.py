from models.game.entities.character.character import Character

class Gaymer(Character):
    DESC = """
    The Gaymer class is a tech-savvy character who excels in both physical and magical defenses.
    They are known for their strategic thinking and adaptability in various combat situations.
    They often use gadgets and spells to outmaneuver their opponents.
    """
    role: str = Field(default=CharacterClasses.GAYMER.value)
    description: str = Field(default=DESC.strip())
    gender: str = Field(default=Genders.MALE.value)

    # Override Combat Stats
    physical_attack: int = Field(default=6)
    magical_attack: int = Field(default=2)
    physical_defense: int = Field(default=20)
    magical_defense: int = Field(default=20)
    speed: int = Field(default=2)

    def level_up(self) -> None:
        """Level up the Gaymer character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 5
        self.physical_attack += 2
        self.magical_attack += 2
        self.physical_defense += 5
        self.magical_defense += 5
        self.speed += 1