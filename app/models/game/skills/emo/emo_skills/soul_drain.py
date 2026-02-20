# Inflicts target with high damage. Heal user for 50% of the damage dealt. Applies curse to target for 2 turns.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.emo_skills import EmoSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.status_effects.curse import Curse
from models.game.effects.applied_effect import AppliedEffect

class SoulDrain(BaseSkill):
    name: str = Field(default=EmoSkills.SOUL_DRAIN.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Inflicts target with high damage. Heal user for 50% of the damage dealt. Applies curse to target for 2 turns.")
    cooldown: int = Field(default=5)
    power: int = Field(default=120)

    # ----------------------------------- CONSTANTS -----------------------------------
    HEALING_PERCENTAGE: float = 0.5  # Heal for 50%
    CURSE_DURATION: int = 2

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Soul Drain skill on a target."""
        # Calculate damage
        damage = self.calculate_base_damage(user, target, StatType.MAGIC_ATTACK, StatType.MAGIC_DEFENSE)
        
        # Apply damage to target
        target.take_damage(damage)

        # Heal user for 50% of damage dealt
        heal_amount = int(damage * self.HEALING_PERCENTAGE)
        user.heal(heal_amount)

        # Apply curse effect to target
        curse = Curse()
        curse_effects: list[AppliedEffect] = curse.generate_effects(duration=self.CURSE_DURATION)
        for effect in curse_effects:
            target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Soul Drain - increases power."""
        self.level += 1
        self.power += 12