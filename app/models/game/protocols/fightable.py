from typing import Protocol
from models.game.skills.base_skill import BaseSkill

class Fightable(Protocol):
    def attack(self, skill: BaseSkill, target: Fightable) -> None:
        """Perform an attack on the target Fightable entity."""
        ...

    def defend(self, damage: int) -> None:
        """Defend against an incoming attack with specified damage."""
        ...

    def take_damage(self, damage: int) -> None:
        """Take damage and update health accordingly."""
        ...