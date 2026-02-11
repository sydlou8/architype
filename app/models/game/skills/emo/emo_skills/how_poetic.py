# Turns user into a glass cannon for 3 turns. Increases damage dealt by 50% but also increases damage taken by 50%.
# applies strengthen, wisdom, hidden, susceptible, vulnerable for 3 turns.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.emo_skills import EmoSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.positive_effects.buffs.strengthen import Strengthen
from models.game.effects.positive_effects.buffs.wisdom import Wisdom
from models.game.effects.positive_effects.status_effects.hidden import Hidden
from models.game.effects.negative_effects.debuffs.susceptible import Susceptible
from models.game.effects.negative_effects.debuffs.vulnerable import Vulnerable
from models.game.enums.effect_types import ModifierEffects, StatusEffects
from models.game.effects.applied_effect import AppliedEffect

class HowPoetic(BaseSkill):
    name: str = Field(default=EmoSkills.HOW_POETIC.value)
    skill_type: str = Field(default=SkillType.BUFF.value)
    description: str = Field(default="Turns user into a glass cannon for 3 turns. Increases damage dealt by 50% but also increases damage taken by 50%.")
    cooldown: int = Field(default=5)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use How Poetic to apply buffs and debuffs to the user."""
        # Create effects
        strengthen = Strengthen()
        wisdom = Wisdom()
        hidden = Hidden()
        susceptible = Susceptible()
        vulnerable = Vulnerable()

        # Generate applied effects with duration of 3 turns
        effects_to_apply: list[AppliedEffect] = []
        for effect in [strengthen, wisdom, hidden]:
            effects_to_apply.extend(effect.generate_effects(duration=3))
        for effect in [susceptible, vulnerable]:
            effects_to_apply.extend(effect.generate_effects(duration=3))

        # Apply all effects to the user
        for effect in effects_to_apply:
            user.add_effect(effect)
    
    def level_up(self) -> None:
        """Level up How Poetic - increases damage boost and damage taken."""
        self.level += 1
        # Increase damage boost and damage taken by 10% per level up
        new_boost_multiplier = 0.5 + (self.level - 1) * 0.1
        self.damage_boost_multiplier = new_boost_multiplier
        self.damage_taken_multiplier = new_boost_multiplier
