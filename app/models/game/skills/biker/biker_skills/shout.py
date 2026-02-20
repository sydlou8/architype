# Applies Berserk to target for 3 turns. and damages for 30% of max health.
# Applies Hidden to party for 3 turns.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.biker_skills import BikerSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.modifier_effects.berserk import Berserk
from models.game.effects.status_effects import Hidden
from models.game.effects.applied_effect import AppliedEffect

class Shout(BaseSkill):
    name: str = Field(default=BikerSkills.SHOUT.value)
    skill_type: str = Field(default=SkillType.BUFF.value)
    description: str = Field(default="Applies Berserk to target for 3 turns and damages for 30% of max health. Applies Hidden to party for 3 turns.")
    cooldown: int = Field(default=5)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Shout skill to apply Berserk to the target and Hidden to the party."""
        berserk = Berserk()
        hidden = Hidden()
        berserk_effects: list[AppliedEffect] = berserk.generate_effects(duration=3)  # Duration of 3 turns
        hidden_effects: list[AppliedEffect] = hidden.generate_effects(duration=3)  # Duration of 3 turns
        
        # Apply Berserk to the first target and deal damage
        if targets:
            target = targets[0]
            for effect in berserk_effects:
                target.add_effect(effect)
            damage = target.max_health * 0.3
            target.take_damage(damage)

        # Apply Hidden to the entire party
        for target in targets:
            for effect in hidden_effects:
                target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Shout - increases duration of effects and damage percentage."""
        self.level += 1
        new_duration = 3 + (self.level - 1) * 1
        new_damage_percentage = 0.3 + (self.level - 1) * 0.05
        Berserk.DURATION = new_duration
        Hidden.DURATION = new_duration
        description = f"Applies Berserk to target for {new_duration} turns and damages for {new_damage_percentage:.0%} of max health. Applies Hidden to party for {new_duration} turns."
        self.description = description