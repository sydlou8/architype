# increases attack and dodge by 40% for self for 3 turns.
# player cannot be targeted by enemy during this turn. (shield)
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.enums.skills.jock_skills import JockSkills
from models.game.effects.modifier_effects.buffs.agility import Agility
from models.game.effects.modifier_effects.buffs.strengthen import Strengthen # physical attack buff
from models.game.effects.status_effects.shield import Shield
from models.game.effects.applied_effect import AppliedEffect

class Warmup(BaseSkill):
    name: str = Field(default=JockSkills.WARMUP.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="Increases attack and dodge by 40% for self for 3 turns. Player cannot be targeted by enemy during this turn (shield).")
    cooldown: int = Field(default=4)
    power: int = Field(default=0)

    # ----------------------------------- CONSTANTS -----------------------------------
    BUFF_DURATION: int = 3
    ATTACK_INCREASE: float = 0.4  # 40%
    DODGE_INCREASE: float = 0.4  # 40%
    SHIELD_DURATION: int = 1  # Shield lasts for 1 turn

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Warmup skill on self."""
        # Apply strengthen buff to user (increases physical attack)
        strengthen = Strengthen(attack_increase=self.ATTACK_INCREASE)
        strengthen_effects: list[AppliedEffect] = strengthen.generate_effects(duration=self.BUFF_DURATION)
        for effect in strengthen_effects:
            user.add_effect(effect)

        # Apply agility buff to user (increases dodge)
        agility = Agility(dodge_increase=self.DODGE_INCREASE)
        agility_effects: list[AppliedEffect] = agility.generate_effects(duration=self.BUFF_DURATION)
        for effect in agility_effects:
            user.add_effect(effect)

        # Apply shield effect to user
        shield = Shield()
        shield_effects: list[AppliedEffect] = shield.generate_effects(duration=self.SHIELD_DURATION)
        for effect in shield_effects:
            user.add_effect(effect)
    
    def level_up(self) -> None:
        """Level up Warmup - increases buff effectiveness."""
        self.level += 1
        self.ATTACK_INCREASE += 0.05  # Increase attack buff by 5%
        self.DODGE_INCREASE += 0.05   # Increase dodge buff by 5%