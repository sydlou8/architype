# ranged attack that spikes a ball at the target, dealing physical damage, reducing the target's accuracy by 20% for 3 turns, and causes bleed for 3 turns.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.jock_skills import JockSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.effects.negative_effects.debuffs.accuracy_debuff import AccuracyDeb
from models.game.effects.negative_effects.status_effects.bleed import Bleed
from models.game.effects.applied_effect import AppliedEffect

class Spike(BaseSkill):
    name: str = Field(default=JockSkills.SPIKE.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Ranged attack that spikes a ball at the target, dealing physical damage, reducing the target's accuracy by 20% for 3 turns, and causes bleed for 3 turns.")
    cooldown: int = Field(default=3)
    power: int = Field(default=75)

    # ----------------------------------- CONSTANTS -----------------------------------
    ACCURACY_DECREASE: float = 0.2  # 20%
    DEBUFF_DURATION: int = 3
    BLEED_DURATION: int = 3
    BLEED_TICK_DAMAGE: int = 6

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Spike skill on a target."""
        # Calculate damage
        damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)
        
        # Apply damage to target
        target.take_damage(damage)

        # Apply accuracy debuff to target
        accuracy_debuff = AccuracyDeb(accuracy_decrease=self.ACCURACY_DECREASE)
        accuracy_debuff_effects: list[AppliedEffect] = accuracy_debuff.generate_effects(duration=self.DEBUFF_DURATION)
        for effect in accuracy_debuff_effects:
            target.add_effect(effect)

        # Apply bleed effect
        bleed = Bleed()
        bleed_effects: list[AppliedEffect] = bleed.generate_effects(
            duration=self.BLEED_DURATION,
            tick_value=self.BLEED_TICK_DAMAGE
        )
        for effect in bleed_effects:
            target.add_effect(effect)
            
    def level_up(self) -> None:
        """Level up Spike - increases power."""
        self.level += 1
        self.power += 6