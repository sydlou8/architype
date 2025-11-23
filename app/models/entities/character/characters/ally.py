from sqlmodel import Field
from models.entities.character.character import Character
from models.enums.character_classes import CharacterClasses

class Ally(Character):
    DESC = """
    Just a helpful ally. He is straight.
    """
    role: str = Field(default=CharacterClasses.ALLY.value)
    # Stats are not overrided, using base Character stats (all stats set to 10 by default)

    # TODO: Eventually update to allow users to choose skill points allocation
    def level_up(self) -> None:
        """Level up the Ally character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 5
        self.physical_attack += 3
        self.magical_attack += 3
        self.physical_defense += 3
        self.magical_defense += 3
        self.speed += 3
