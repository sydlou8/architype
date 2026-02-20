# grants a single ally entity and self BULKED and EMPOWERED for 3 turns
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.emo_skills import EmoSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.status_effects.bulked import Bulked
from models.game.effects.status_effects.empowered import Empowered
from models.game.effects.applied_effect import AppliedEffect

class DaggerDance(BaseSkill):
    name: str = Field(default=EmoSkills.DAGGER_DANCE.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Grants a single ally entity and self BULKED and EMPOWERED for 3 turns.")
    cooldown: int = Field(default=4)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Dagger Dance skill to apply Bulked and Empowered to a single ally and self."""
        if not targets:
            raise ValueError("Dagger Dance requires at least one target.")
        
        target = targets[0]  # Only the first target is affected
        bulked = Bulked()
        empowered = Empowered()
        
        bulked_effects: list[AppliedEffect] = bulked.generate_effects(duration=3)  # Duration of 3 turns
        empowered_effects: list[AppliedEffect] = empowered.generate_effects(duration=3)  # Duration of 3 turns
        
        for effect in bulked_effects + empowered_effects:
            target.add_effect(effect)
            user.add_effect(effect)  # Apply the same effects to self

    def level_up(self) -> None:
        """Level up Dagger Dance - increases duration of effects."""
        self.level += 1
        # Increase the duration of the effects by 1 turn per level up
        new_duration = 3 + (self.level - 1) * 1
        Bulked.DURATION = new_duration
        Empowered.DURATION = new_duration
        description = f"Grants a single ally entity and self BULKED and EMPOWERED for {new_duration} turns."
        self.description = description