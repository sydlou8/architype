# inflicts small physical damage to all enemies.
# applies burn for 4 turns (2 damage per turn)
# multi-target physical damage skill
import random

from sqlmodel import Field

from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.enums.skills.barista_skills import BaristaSkills
from models.game.effects.negative_effects.status_effects.burn import Burn
from models.game.effects.applied_effect import AppliedEffect


class BatchBrew(BaseSkill):
    name: str = Field(default=BaristaSkills.BATCH_BREW.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Multi-target attack that inflicts small physical damage to all enemies. Applies burn for 4 turns (2 damage per turn).")
    cooldown: int = Field(default=4)
    power: int = Field(default=40)
    is_multi_target: bool = Field(default=True)

    # ----------------------------------- CONSTANTS -----------------------------------
    BURN_DURATION: int = 4
    BURN_TICK_DAMAGE: int = 2
    BURN_CHANCE: float = 0.7  # 70% chance to apply burn

    # -------------------------------- OVERRIDE METHOD --------------------------------
    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """
        Use the Batch Brew skill on targets.
        Params:
        user: BaseEntity - The entity using the skill.
        target: BaseEntity - The target entity (or list for multi-target).
        """
        # Calculate damage
        base_damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)
        
        # Apply damage to target
        target.take_damage(base_damage)

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
        """Level up Batch Brew - increases power."""
        self.level += 1
        self.power += 3
