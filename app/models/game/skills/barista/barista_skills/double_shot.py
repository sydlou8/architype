# A ranged offensive skill that fires two quick shots at the target. 50% chance to burn the target for 3 damage for 3 turns.
# multi hit attack
# single target ranged damage skill
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.enums.skills.barista_skills import BaristaSkills

class DoubleShot(BaseSkill):
    name: str = Field(default=BaristaSkills.DOUBLE_SHOT.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="A ranged offensive skill that fires two quick shots at the target. 50% chance to burn the target for 3 damage for 3 turns.")
    cooldown: int = Field(default=2)
    power: int = Field(default=30)  
    is_multi_hit: bool = Field(default=True)    # Hits 2 times

    # ----------------------------------- CONSTANTS -----------------------------------
    HIT_QUANTITY: int = 2                       # Hits 2 times
    BURN_DURATION: int = 3                      # Burn lasts for 3 turns
    BURN_TICK_DAMAGE: int = 3                   # Burn deals 3 damage per turn
    BURN_CHANCE: float = 0.5                    # 50% chance to apply burn

    # -------------------------------- OVERRIDE METHOD --------------------------------
    def use(self, user: BaseEntity, target: BaseEntity) -> int:
        """
        Use the Double Shot skill on a target -- applying additional effects and calculates base skill damage.
        Params:
        user: BaseEntity - The entity using the skill.
        target: BaseEntity - The target entity.
        Returns:
        int - The calculated base damage dealt by the skill.
        """
        base_damage = self.calculate_base_damage(user, target, StatType.RANGED_ATTACK, StatType.RANGED_DEFENSE)

        # Apply burn effect to the target based on chance
        import random
        if random.random() < self.BURN_CHANCE:
            from models.game.effects.negative_effects.status_effects.burn import Burn
            from models.game.effects.applied_effect import AppliedEffect

            burn = Burn()
            burn_effects: list[AppliedEffect] = burn.generate_effects(
                duration=self.BURN_DURATION, 
                tick_value=self.BURN_TICK_DAMAGE
            )

            for effect in burn_effects:
                target.add_effect(effect)

        return base_damage