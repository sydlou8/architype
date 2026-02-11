# stuns single target for 2 turns and applies fatigue debuff for 25% for 3 turns
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.drag_queen_skills import DragQueenSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.effects.negative_effects.debuffs.fatigue import Fatigue
from models.game.effects.negative_effects.status_effects.stun import Stun
from models.game.effects.applied_effect import AppliedEffect

class Gaggy(BaseSkill):
    name: str = Field(default=DragQueenSkills.GAGGY.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Stuns single target for 2 turns and applies fatigue debuff for 25% for 3 turns.")
    cooldown: int = Field(default=4)

    # ----------------------------------- CONSTANTS -----------------------------------
    STUN_DURATION: int = 2
    FATIGUE_DECREASE: float = 0.25  # 25%
    FATIGUE_DURATION: int = 3

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Gaggy skill on a target."""
        # Apply stun effect to target
        stun = Stun()
        stun_effects: list[AppliedEffect] = stun.generate_effects(duration=self.STUN_DURATION)
        for effect in stun_effects:
            target.add_effect(effect)

        # Apply fatigue debuff to target
        fatigue = Fatigue(fatigue_decrease=self.FATIGUE_DECREASE)
        fatigue_effects: list[AppliedEffect] = fatigue.generate_effects(duration=self.FATIGUE_DURATION)
        for effect in fatigue_effects:
            target.add_effect(effect)
            
    def level_up(self) -> None:
        """Level up Gaggy - currently no stat increases."""
        self.level += 1