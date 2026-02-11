# Powerful attack that has a chance to stun the target for 1 turn. The damage is increased by 20% if the target is already stunned.
import random
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.biker_skills import BikerSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.negative_effects.status_effects.stunned import Stunned
from models.game.effects.applied_effect import AppliedEffect

class Crash(BaseSkill):
    name: str = Field(default=BikerSkills.CRASH.value)
    skill_type: str = Field(default=SkillType.ATTACK.value)
    description: str = Field(default="Powerful attack that has a chance to stun the target for 1 turn. The damage is increased by 20% if the target is already stunned.")
    cooldown: int = Field(default=5)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Crash skill to attack the target and potentially apply Stunned."""
        for target in targets:
            damage_multiplier = 1.2 if any(effect.type == Stunned.type for effect in target.active_effects) else 1.0
            damage = self.calculate_damage(user, target) * damage_multiplier
            target.take_damage(damage)

            # Chance to apply Stunned effect
            if self.should_apply_stun(target):
                stunned = Stunned()
                stunned_effects: list[AppliedEffect] = stunned.generate_effects(duration=1)  # Duration of 1 turn
                for effect in stunned_effects:
                    target.add_effect(effect)

    def should_apply_stun(self, target) -> bool:
        """Determine whether to apply the Stunned effect based on a random chance."""
        stun_chance = 0.3  # 30% chance to stun
        return random.random() < stun_chance

    def level_up(self) -> None:
        """Level up Crash - increases damage multiplier and stun chance."""
        self.level += 1
        new_damage_multiplier = 1.2 + (self.level - 1) * 0.05  # Increase damage multiplier by 5% per level
        new_stun_chance = 0.3 + (self.level - 1) * 0.05         # Increase stun chance by 5% per level
        description = f"Powerful attack that has a {new_stun_chance:.0%} chance to stun the target for 1 turn. The damage is increased by {new_damage_multiplier:.0%} if the target is already stunned."
        self.description = description