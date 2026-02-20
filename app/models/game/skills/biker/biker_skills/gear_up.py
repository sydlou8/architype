# Applies Endure and Invigorated for 2 turns to self.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.biker_skills import BikerSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.status_effects.endure import Endure
from models.game.effects.status_effects.invigorated import Invigorated
from models.game.effects.applied_effect import AppliedEffect

class GearUp(BaseSkill):
    name: str = Field(default=BikerSkills.GEAR_UP.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="Applies Endure and Invigorated for 2 turns to self.")
    cooldown: int = Field(default=5)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Gear Up skill to apply Endure and Invigorated to self."""
        endure = Endure()
        invigorated = Invigorated()

        endure_effects: list[AppliedEffect] = endure.generate_effects(duration=2)  # Duration of 2 turns
        invigorated_effects: list[AppliedEffect] = invigorated.generate_effects(duration=2)  # Duration of 2 turns

        for effect in endure_effects:
            user.add_effect(effect)
        for effect in invigorated_effects:
            user.add_effect(effect)

    def level_up(self) -> None:
        """Level up Gear Up - increases duration of Endure and Invigorated effects."""
        self.level += 1
        # Increase the duration of both effects by 1 turn per level up
        new_duration = 2 + (self.level - 1) * 1
        Endure.DURATION = new_duration
        Invigorated.DURATION = new_duration
        description = f"Applies Endure and Invigorated for {new_duration} turns to self."
        self.description = description