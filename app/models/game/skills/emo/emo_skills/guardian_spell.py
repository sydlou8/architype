# taunts enemy to attack caster for 3 turns.abs
# applies shiled and hidden to self for 3 turns.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.emo_skills import EmoSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.mixed_effects.taunt import Taunt
from models.game.effects.positive_effects.status_effects.shield import Shield
from models.game.effects.positive_effects.status_effects.hidden import Hidden
from models.game.effects.applied_effect import AppliedEffect

class GuardianSpell(BaseSkill):
    name: str = Field(default=EmoSkills.GUARDIAN_SPELL.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="Taunts enemy to attack caster for 3 turns. Also applies shield and hidden to self for 3 turns.")
    cooldown: int = Field(default=4)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Guardian Spell skill to apply Taunt to the enemy and Shield and Hidden to self."""
        taunt = Taunt()
        taunt_effects: list[AppliedEffect] = taunt.generate_effects(duration=3)  # Duration of 3 turns
        for target in targets:
            for effect in taunt_effects:
                target.add_effect(effect)

        shield = Shield()
        shield_effects: list[AppliedEffect] = shield.generate_effects(duration=3)  # Duration of 3 turns
        for effect in shield_effects:
            user.add_effect(effect)

        hidden = Hidden()
        hidden_effects: list[AppliedEffect] = hidden.generate_effects(duration=3)  # Duration of 3 turns
        for effect in hidden_effects:
            user.add_effect(effect)

    def level_up(self) -> None:
        """Level up Guardian Spell - increases duration of Taunt, Shield, and Hidden effects."""
        self.level += 1
        new_duration = 3 + (self.level - 1)  # Increase duration by 1 turn per level up
        Taunt.DURATION = new_duration
        Shield.DURATION = new_duration
        Hidden.DURATION = new_duration
        description = f"Taunts enemy to attack caster for {new_duration} turns. Also applies shield and hidden to self for {new_duration} turns."
        self.description = description