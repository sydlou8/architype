# increases the target's dodge by 40% for 3 turns. And attacks with 20% increased accuracy for 3 turns.
# hits all enemies for small damage.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.enums.skills.jock_skills import JockSkills
from models.game.effects.modifier_effects.buffs.agility import Agility
from models.game.effects.modifier_effects.buffs.accuracy import Accuracy
from models.game.effects.applied_effect import AppliedEffect

class FormationAte(BaseSkill):
    name: str = Field(default=JockSkills.FORMATION_ATE.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="Increases the target's dodge by 40% for 3 turns. And attacks with 20% increased accuracy for 3 turns.")
    cooldown: int = Field(default=4)
    power: int = Field(default=0)  # No direct damage

    # ----------------------------------- CONSTANTS -----------------------------------
    EFFECT_DURATION: int = 3
    DODGE_INCREASE: float = 0.4  # 40%
    ACCURACY_INCREASE: float = 0.2  # 20%

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Formation Ate skill on a target."""
        # Apply agility (dodge) buff to target
        agility = Agility(dodge_increase=self.DODGE_INCREASE)
        agility_effects: list[AppliedEffect] = agility.generate_effects(duration=self.EFFECT_DURATION)
        
        for effect in agility_effects:
            target.add_effect(effect)

        # Apply accuracy buff to target
        accuracy = Accuracy(accuracy_increase=self.ACCURACY_INCREASE)
        accuracy_effects: list[AppliedEffect] = accuracy.generate_effects(duration=self.EFFECT_DURATION)
        
        for effect in accuracy_effects:
            target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Formation Ate - increases effect duration."""
        self.level += 1
        self.EFFECT_DURATION += 1  # Each level adds 1 more turn of buffs