# A ranged offensive skill that fires two quick shots at the target. 50% chance to burn the target for 3 damage for 3 turns.
# multi hit attack
# single target ranged damage skill
import random

from sqlmodel import Field

from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.enums.skills.barista_skills import BaristaSkills
from models.game.effects.negative_effects.status_effects.burn import Burn
from models.game.effects.applied_effect import AppliedEffect

class DoubleShot(BaseSkill):
    name: str = Field(default=BaristaSkills.DOUBLE_SHOT.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="A ranged offensive skill that fires two quick shots at the target. 50% chance to burn the target for 3 damage for 3 turns.")
    cooldown: int = Field(default=2)
    power: int = Field(default=60)  
    is_multi_hit: bool = Field(default=True)    # Hits 2 times

    # ----------------------------------- CONSTANTS -----------------------------------
    HIT_QUANTITY: int = 2                       # Hits 2 times
    BURN_DURATION: int = 3                      # Burn lasts for 3 turns
    BURN_TICK_DAMAGE: int = 3                   # Burn deals 3 damage per turn
    BURN_CHANCE: float = 0.5                    # 50% chance to apply burn

    # -------------------------------- OVERRIDE METHOD --------------------------------
    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """
        Use the Double Shot skill on a target -- applying damage and additional effects.
        Params:
        user: BaseEntity - The entity using the skill.
        target: BaseEntity - The target entity.
        """
        # Calculate damage (hits twice because is_multi_hit=True)
        base_damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)
        total_damage = base_damage * self.HIT_QUANTITY  # Hits 2 times
        
        # Apply damage to target
        target.take_damage(total_damage)

        # Apply burn effect to the target based on chance
        if random.random() < self.BURN_CHANCE:
            burn = Burn()
            burn_effects: list[AppliedEffect] = burn.generate_effects(
                duration=self.BURN_DURATION, 
                tick_value=self.BURN_TICK_DAMAGE
            )

            for effect in burn_effects:
                target.add_effect(effect)
    
    def level_up(self) -> None:
        """Level up Double Shot - increases power and burn chance."""
        self.level += 1
        self.power += 5  # Increase damage
        self.BURN_CHANCE = min(1.0, self.BURN_CHANCE + 0.05)  # Increase burn chance by 5%, max 100%