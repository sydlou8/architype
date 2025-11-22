from sqlmodel import Field
from models.skills.base_skill import BaseSkill
from models.entities.base_entity import BaseEntity
from models.enums.skills.barista_skills import BaristaSkills
from models.enums.skill_types import SkillType
from models.effects.positive_effects.buffs.agility import Agility
from models.effects.mixed_effects.rage import Rage

class GenderEspressoN(BaseSkill):
    name: str = Field(default=BaristaSkills.GENDER_ESPRESSO_N.value)
    description: str = Field(default="A skill that a chance to cause enemy confusion and rage for 3 turns, and increases self dodge.")

    EFFECT_DURATION: int = 3

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Gender Expression skill on a target."""
        # TODO: Implement confusion and rage effects

        agility = Agility()
        user_effects = agility.generate_effects(duration=self.EFFECT_DURATION)

        # 50% chance to apply rage effect
        import random
        if random.random() < 0.5:
            rage = Rage()
            target_effects = rage.generate_effects(duration=self.EFFECT_DURATION)
            
            for effect in target_effects:
                target.add_effect(effect)