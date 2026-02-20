# applies invigorated and bulked to self for 3 turns.abs
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.biker_skills import BikerSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.status_effects import Invigorated, Bulked
from models.game.effects.applied_effect import AppliedEffect

class Charge(BaseSkill):
    name: str = Field(default=BikerSkills.CHARGE.value)
    skill_type: str = Field(default=SkillType.BUFF.value)
    description: str = Field(default="Applies Invigorated and Bulked to self for 3 turns.")
    cooldown: int = Field(default=4)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Charge skill to apply Invigorated and Bulked to self."""
        invigorated = Invigorated()
        bulked = Bulked()
        invigorated_effects: list[AppliedEffect] = invigorated.generate_effects(duration=3)  # Duration of 3 turns
        bulked_effects: list[AppliedEffect] = bulked.generate_effects(duration=3)  # Duration of 3 turns
        for effect in invigorated_effects + bulked_effects:
            user.add_effect(effect)

    def level_up(self) -> None:
        """Level up Charge - increases duration of effects."""
        self.level += 1
        new_duration = 3 + (self.level - 1) * 1
        Invigorated.DURATION = new_duration
        Bulked.DURATION = new_duration
        description = f"Applies Invigorated and Bulked to self for {new_duration} turns."
        self.description = description
