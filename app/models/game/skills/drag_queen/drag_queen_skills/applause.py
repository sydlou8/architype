# Allows entire party to attack twice for their next turn for 20% of their original power.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.drag_queen_skills import DragQueenSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.status_effects.double_attack import DoubleAttack
from models.game.effects.applied_effect import AppliedEffect

class Applause(BaseSkill):
    name: str = Field(default=DragQueenSkills.APPLAUSE.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="Allows the entire party to attack twice for their next turn for 20% of their original power.")
    cooldown: int = Field(default=5)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Applause skill to apply Double Attack to the entire party."""
        double_attack = DoubleAttack()
        double_attack_effects: list[AppliedEffect] = double_attack.generate_effects(duration=1)  # Duration of 1 turn
        for target in targets:
            for effect in double_attack_effects:
                target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Applause - increases power multiplier of Double Attack effect."""
        self.level += 1
        # Increase the power multiplier of the Double Attack effect by 5% per level up
        new_power_multiplier = 0.2 + (self.level - 1) * 0.05
        DoubleAttack.POWER_MULTIPLIER = new_power_multiplier