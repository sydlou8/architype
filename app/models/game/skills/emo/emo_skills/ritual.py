# Applies curse to all enemies for 3 turns.
# Attacks all enemies for 20% base damage.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.emo_skills import EmoSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.debuffs.status_effects.curse import Curse
from models.game.effects.applied_effect import AppliedEffect

class Ritual(BaseSkill):
    name: str = Field(default=EmoSkills.RITUAL.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Applies curse to all enemies for 3 turns. Attacks all enemies for 20% base damage.")
    cooldown: int = Field(default=4)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Ritual skill to apply Curse to all enemies and deal damage."""
        curse = Curse()
        curse_effects: list[AppliedEffect] = curse.generate_effects(duration=3)  # Duration of 3 turns
        for target in targets:
            # Apply Curse effect to each target
            for effect in curse_effects:
                target.add_effect(effect)
            # Deal damage to each target (20% of user's base damage)
            damage = int(user.base_damage * 0.2)
            target.take_damage(damage)
    
    def level_up(self) -> None:
        """Level up Ritual - increases damage dealt."""
        self.level += 1
        # Increase damage by 5% of base damage per level up
        new_damage_multiplier = 0.2 + (self.level - 1) * 0.05
        self.damage_multiplier = new_damage_multiplier