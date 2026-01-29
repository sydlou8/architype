from sqlmodel import Field
from typing import ClassVar
from models.game.entities.character.character import Character
from models.game.enums.character_classes import CharacterClasses
from models.game.enums.genders import Genders
from models.game.skills.barista.barista_skills.take_a_shot import TakeAShot
from models.game.skills.barista.barista_skills.double_shot import DoubleShot
from models.game.skills.barista.barista_skills.espresso_bomb import EspressoBomb

class Barista(Character):
    DESC: ClassVar[str] = """
    Masters of caffeinated concoctions, Baristas energize their allies and debilitate foes with potent brews.
    High speed and dodge -- mixed attacker with a physical attack focus. Strong use of burn debuffs.
    """

    role: str = Field(default=CharacterClasses.BARISTA.value)
    description: str = Field(default=DESC.strip())
    gender: str = Field(default= Genders.NON_BINARY.value)

    # Override Basic Attributes
    max_health: int = Field(default=80)

    # Override Combat Stats 
    physical_attack: int = Field(default=14)
    magical_attack: int = Field(default=9)
    physical_defense: int = Field(default=6)
    magical_defense: int = Field(default=6)
    speed: int = Field(default=15)

    # Override Combat Modifiers
    dodge: float = Field(default=0.3)  # 30% dodge chance

    def model_post_init(self, __context) -> None:
        """Initialize Barista with default skills after model creation."""
        super().model_post_init(__context)
        # Load default skills if none are set
        if not self.skills:
            self.skills = {
                "take_a_shot": TakeAShot(),
                "double_shot": DoubleShot(),
                "espresso_bomb": EspressoBomb()
            }

    # TODO: Eventually update to allow users to choose skill points allocation
    def level_up(self) -> None:
        """Level up the Barista character, increasing stats accordingly."""
        super().level_up()
        self.max_health += 8
        self.physical_attack += 3
        self.magical_attack += 2
        self.physical_defense += 2
        self.magical_defense += 1
        self.speed += 4
