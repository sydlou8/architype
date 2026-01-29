import random

from sqlmodel import Field

from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.barista_skills import BaristaSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.positive_effects.buffs.agility import Agility
from models.game.effects.mixed_effects.rage import Rage

class GenderEspressoN(BaseSkill):
    name: str = Field(default=BaristaSkills.GENDER_ESPRESSO_N.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="A skill that a chance to cause enemy confusion and rage for 3 turns, and increases self dodge.")
    cooldown: int = Field(default=4)
    power: int = Field(default=0)  # No direct damage

    EFFECT_DURATION: int = 3
    RAGE_CHANCE: float = 0.5  # 50% chance

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Gender Expression skill on a target."""
        # Apply agility to user
        agility = Agility()
        user_effects = agility.generate_effects(duration=self.EFFECT_DURATION)
        for effect in user_effects:
            user.add_effect(effect)

        # 50% chance to apply rage effect to target
        if random.random() < self.RAGE_CHANCE:
            rage = Rage()
            target_effects = rage.generate_effects(duration=self.EFFECT_DURATION)
            
            for effect in target_effects:
                target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Gender Espresso-N - increases rage chance and duration."""
        self.level += 1
        self.RAGE_CHANCE = min(0.9, self.RAGE_CHANCE + 0.05)  # Max 90% chance
        self.EFFECT_DURATION = min(5, self.EFFECT_DURATION + 1)  # Max 5 turns
