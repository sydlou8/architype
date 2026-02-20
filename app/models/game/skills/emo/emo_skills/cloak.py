# applies agility and removes negative effects for a duration (HIDDEN status effect) to party for 1 turn.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.emo_skills import EmoSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.status_effects.hidden import Hidden
from models.game.effects.applied_effect import AppliedEffect

class Cloak(BaseSkill):
    name: str = Field(default=EmoSkills.CLOAK.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="Applies agility and removes negative effects for a duration (HIDDEN status effect) to party for 1 turn.")
    cooldown: int = Field(default=3)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Cloak skill to apply Hidden to the entire party."""
        hidden = Hidden()
        hidden_effects: list[AppliedEffect] = hidden.generate_effects(duration=1)  # Duration of 1 turn
        for target in targets:
            for effect in hidden_effects:
                target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Cloak - increases duration of Hidden effect."""
        self.level += 1
        # Increase the duration of the Hidden effect by 1 turn per level up
        new_duration = 1 + (self.level - 1) * 1
        Hidden.DURATION = new_duration
        description = f"Applies agility and removes negative effects for a duration (HIDDEN status effect) to party for {new_duration} turns."
        self.description = description
