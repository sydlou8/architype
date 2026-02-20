# applies regeneration to a single target for 3 turns.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.jock_skills import JockSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.effects.modifier_effects.buffs.regeneration import Regeneration
from models.game.effects.applied_effect import AppliedEffect

class Recover(BaseSkill):
    name: str = Field(default=JockSkills.RECOVER.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="Applies regeneration to a single target for 3 turns.")
    cooldown: int = Field(default=3)
    power: int = Field(default=0)  # No direct healing

    # ----------------------------------- CONSTANTS -----------------------------------
    REGEN_DURATION: int = 3
    REGEN_TICK_HEALING: int = 5  # Heals 5 HP per turn

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Recover skill on a target."""
        # Apply regeneration effect
        regen = Regeneration()
        regen_effects: list[AppliedEffect] = regen.generate_effects(
            duration=self.REGEN_DURATION, 
            tick_value=self.REGEN_TICK_HEALING
        )
        
        for effect in regen_effects:
            target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Recover - increases regeneration tick healing."""
        self.level += 1
        self.REGEN_TICK_HEALING += 2  # Each level adds 2 more HP per turn