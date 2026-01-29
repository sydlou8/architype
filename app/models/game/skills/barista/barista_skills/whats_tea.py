# party small heal that applies regeneration (2 hp per turn) for 3 turns.
# multi-target healing skill
from sqlmodel import Field

from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.barista_skills import BaristaSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.positive_effects.status_effects.regeneration import Regeneration
from models.game.effects.applied_effect import AppliedEffect


class WhatsTea(BaseSkill):
    name: str = Field(default=BaristaSkills.WHATS_TEA.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="Party small heal that applies regeneration (2 hp per turn) for 3 turns.")
    cooldown: int = Field(default=3)
    power: int = Field(default=30)  # Healing power
    is_multi_target: bool = Field(default=True)

    # ----------------------------------- CONSTANTS -----------------------------------
    REGEN_DURATION: int = 3
    REGEN_TICK_HEALING: int = 2

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """
        Use the What's Tea skill on targets (healing + regen).
        Params:
        user: BaseEntity - The entity using the skill.
        target: BaseEntity - The target entity.
        """
        # Calculate healing amount (power% of magical attack)
        healing_amount = int((self.power / 100) * user.current_magical_attack)
        
        # Apply healing to target
        target.heal(healing_amount)

        # Apply regeneration effect
        regen = Regeneration()
        regen_effects: list[AppliedEffect] = regen.generate_effects(
            duration=self.REGEN_DURATION, 
            tick_value=self.REGEN_TICK_HEALING
        )
        
        for effect in regen_effects:
            target.add_effect(effect)

    def level_up(self) -> None:
        """Level up What's Tea - increases healing power."""
        self.level += 1
        self.power += 5
