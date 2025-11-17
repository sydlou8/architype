from sqlmodel import Field
from models.skills.base_skill import BaseSkill
from models.entities.base_entity import BaseEntity
from models.enums.skill_types import SkillType
from models.enums.stat_types import StatType
from models.enums.skills.barista_skills import BaristaSkills
from models.enums.effect_types import EffectType
from models.effects.negative_effects.main_effects.burn import Burn
from models.effects.applied_effect import AppliedEffect

class EspressoBomb(BaseSkill):
    name: str = Field(default=BaristaSkills.ESPRESSO_BOMB.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="An area damage skill that deals physical damage and causes burn for 5 turns.")

    power: int = Field(default=50)  # Example power value

    is_multi_target: bool = Field(default=True)  # Affects multiple targets

    BURN_DURATION: int = 5  # Burn lasts for 5 turns
    BURN_TICK_DAMAGE: int = 3  # Burn deals 3 damage per turn

    def use(self, user: BaseEntity, target: BaseEntity) -> int:
        """
        Use the Espresso Bomb skill on a target -- applying additional effects and calculates base skill damage.
        Params:
        user: BaseEntity - The entity using the skill.
        target: BaseEntity - The target entity.
        Returns:
        int - The calculated base damage dealt by the skill.
        """
        # TODO: Implement area damage logic: once party has been defined.
        base_damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)

        # Apply burn effect to the target
        burn = Burn()
        burn_effects: list[AppliedEffect] = burn.generate_effects(
            duration=self.BURN_DURATION, 
            tick_value=self.BURN_TICK_DAMAGE
        )

        for effect in burn_effects:
            target.add_effect(effect)

        return base_damage
        