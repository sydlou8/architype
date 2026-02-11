# Applies root to all targets for 3 turns. If the target is already rooted, applies stun instead for 1 turn.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.biker_skills import BikerSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.negative_effects.status_effects.root import Root
from models.game.effects.negative_effects.status_effects.stun import Stun
from models.game.effects.applied_effect import AppliedEffect

class WheelSpikes(BaseSkill):
    name: str = Field(default=BikerSkills.WHEEL_SPIKES.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Applies root to all targets for 3 turns. If the target is already rooted, applies stun instead for 1 turn.")
    cooldown: int = Field(default=4)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Wheel Spikes skill to apply Root or Stun to targets."""
        for target in targets:
            if any(effect.effect_name == Root.name for effect in target.active_effects):
                # Target is already rooted, apply Stun instead
                stun = Stun()
                stun_effects: list[AppliedEffect] = stun.generate_effects(duration=1)  # Duration of 1 turn
                for effect in stun_effects:
                    target.add_effect(effect)
            else:
                # Target is not rooted, apply Root
                root = Root()
                root_effects: list[AppliedEffect] = root.generate_effects(duration=3)  # Duration of 3 turns
                for effect in root_effects:
                    target.add_effect(effect)
    
    def level_up(self) -> None:
        """Level up Wheel Spikes - increases duration of Root effect."""
        self.level += 1
        # Increase the duration of the Root effect by 1 turn per level up
        new_root_duration = 3 + (self.level - 1) * 1
        Root.DURATION = new_root_duration
        description = f"Applies root to all targets for {new_root_duration} turns. If the target is already rooted, applies stun instead for 1 turn."
        self.description = description