# 50% chance to stun enemy for 2 turns and applies shield for 1 turn that blocks incoming damage.
# Deals low physical damage.
import random
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.drag_queen_skills import DragQueenSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.status_effects.stun import Stun
from models.game.effects.modifier_effects.buffs.shield import Shield
from models.game.effects.applied_effect import AppliedEffect

class ClockIt(BaseSkill):
    name: str = Field(default=DragQueenSkills.CLOCK_IT.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="50% chance to stun enemy for 2 turns and applies shield for 1 turn that blocks incoming damage. Deals low physical damage.")
    cooldown: int = Field(default=3)
    power: int = Field(default=40)

    # ----------------------------------- CONSTANTS -----------------------------------
    STUN_CHANCE: float = 0.5  # 50%
    STUN_DURATION: int = 2
    SHIELD_DURATION: int = 1

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Clock It skill on a single target."""
        target = targets[0]  # Clock It is a single-target skill

        # Calculate damage
        damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)
        
        # Apply damage to target
        target.take_damage(damage)

        # Determine if stun is applied
        if random.random() < self.STUN_CHANCE:
            stun = Stun()
            stun_effects: list[AppliedEffect] = stun.generate_effects(duration=self.STUN_DURATION)
            for effect in stun_effects:
                target.add_effect(effect)

        # Apply shield to user
        shield = Shield()
        shield_effects: list[AppliedEffect] = shield.generate_effects(duration=self.SHIELD_DURATION)
        for effect in shield_effects:
            user.add_effect(effect)

    def level_up(self) -> None:
        """Level up Clock It - increases power."""
        self.level += 1
        self.power += 6