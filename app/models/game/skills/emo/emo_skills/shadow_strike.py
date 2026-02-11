# attack single target for high damage, applies vulnerable for 2 turns
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.emo_skills import EmoSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.negative_effects.status_effects.vulnerable import Vulnerable
from models.game.effects.applied_effect import AppliedEffect

class ShadowStrike(BaseSkill):
    name: str = Field(default=EmoSkills.SHADOW_STRIKE.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Attack single target for high damage, applies vulnerable for 2 turns.")
    cooldown: int = Field(default=2)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use Shadow Strike to attack a single target and apply Vulnerable."""
        if not targets:
            return  # No targets to attack
        target = targets[0]  # Attack the first target in the list
        damage = self.calculate_damage(user, target)
        target.take_damage(damage)

        vulnerable = Vulnerable()
        vulnerable_effects: list[AppliedEffect] = vulnerable.generate_effects(duration=2)  # Duration of 2 turns
        for effect in vulnerable_effects:
            target.add_effect(effect)

    def calculate_damage(self, user: BaseEntity, target: BaseEntity) -> int:
        """Calculate the damage dealt by Shadow Strike."""
        base_damage = 50  # Base damage value, can be scaled with user's stats
        return base_damage + user.physical_attack - target.physical_defense

    def level_up(self) -> None:
        """Level up Shadow Strike - increases damage."""
        self.level += 1
        # Increase base damage by 10 per level up
        new_base_damage = 50 + (self.level - 1) * 10
        description = f"Attack single target for high damage ({new_base_damage}), applies vulnerable for 2 turns."
        self.description = description
