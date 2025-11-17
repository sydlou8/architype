from models.entities.skills.base_skill import BaseSkill
from models.entities.enums.effect_type import EffectType
from models.entities.enums.skills.barista_skills import BaristaSkills
from models.entities.effects.negative_effects.burn import Burn
from models.entities.effects.applied_effect import AppliedEffect

class EspressoBomb(BaseSkill):
    name: str = Field(default=BaristaSkills.ESPRESSO_BOMB.value)
    skill_type: str = Field(default=SkillType.PHYSICAL.value)
    description: str = Field(default="An area damage skill that deals physical damage and causes burn for 5 turns.")

    power: int = Field(default=50)  # Example power value

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
        base_damage = calculate_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)

        # Apply burn effect to the target
        burn = Burn()
        burn_effects: list[AppliedEffect] = burn.apply(
            entity=target, 
            duration=self.BURN_DURATION, 
            tick_value=self.BURN_TICK_DAMAGE
        )

        for effect in burn_effects:
            target.add_effect(effect)

        return base_damage
        