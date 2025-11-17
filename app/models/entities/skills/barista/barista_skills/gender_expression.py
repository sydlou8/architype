from sqlmodel import Field
from typing import Any

from models.entities.base_entity import BaseEntity
from models.entities.skills.base_skill import BaseSkill
from models.entities.enums.effect_type import EffectType
from models.entities.enums.skills.barista_skills import BaristaSkills

class GenderExpression(BaseSkill):
    name: str = Field(default=BaristaSkills.GENDER_EXPRESSION.value)
    description: str = Field(default="A skill that a chance to cause enemy rage for 5 turns, and increases self dodge.")

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Gender Expression skill on a target."""
        # TODO: Implement confusion and rage effects
        user.add_effect(EffectType.
AGILITY, duration=5)  # Increase dodge for 5 turns

        # 50% chance to apply rage effect
        import random
        if random.random() < 0.5:
            target.add_effect(EffectType.
RAGE, duration=5)  # Apply rage effect for 5 turns