# removes all negative status effects from the target and applies consecration for 3 turns.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.enums.skills.jock_skills import JockSkills
from models.game.effects.positive_effects.status_effects.consecration import Consecration
from models.game.effects.applied_effect import AppliedEffect

class DetoxAndRefresh(BaseSkill):
    name: str = Field(default=JockSkills.DETOX_AND_REFRESH.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="Removes all negative status effects from the target and applies consecration for 3 turns.")
    cooldown: int = Field(default=5)
    power: int = Field(default=0)  # No direct damage/healing

    # ----------------------------------- CONSTANTS -----------------------------------
    CONSECRATION_DURATION: int = 3

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Detox and Refresh skill on a target."""
        # Remove all negative status effects from the target
        target.remove_negative_status_effects()

        # Apply consecration effect
        consecration = Consecration()
        consecration_effects: list[AppliedEffect] = consecration.generate_effects(
            duration=self.CONSECRATION_DURATION
        )
        
        for effect in consecration_effects:
            target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Detox and Refresh - increases consecration duration."""
        self.level += 1
        self.CONSECRATION_DURATION += 1  # Each level adds 1 more turn of consecration
