# hits all enemies causing stun for 1 turn.
# multi-target physical damage skill
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.jock_skills import JockSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.effects.negative_effects.status_effects.stun import Stun
from models.game.effects.applied_effect import AppliedEffect

class PowerTackle(BaseSkill):
    name: str = Field(default=JockSkills.POWER_TACKLE.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Hits all enemies causing stun for 1 turn.")
    cooldown: int = Field(default=4)
    power: int = Field(default=70)

    is_multi_target: bool = Field(default=True)  # Affects multiple targets

    # ----------------------------------- CONSTANTS -----------------------------------
    STUN_DURATION: int = 1

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Power Tackle skill on a target."""
        # Calculate damage
        damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)
        
        # Apply damage to target
        target.take_damage(damage)

        # Apply stun effect
        stun = Stun()
        stun_effects: list[AppliedEffect] = stun.generate_effects(duration=self.STUN_DURATION)
        for effect in stun_effects:
            target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Power Tackle - increases power."""
        self.level += 1
        self.power += 7