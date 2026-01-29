# throws a scone the size of a brick at single target. Stuns for 2 turns.
# single target physical damage skill
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.barista_skills import BaristaSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.effects.negative_effects.status_effects.stun import Stun
from models.game.effects.applied_effect import AppliedEffect

class SconeWall(BaseSkill):
    name: str = Field(default=BaristaSkills.SCONE_WALL.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Throws a scone the size of a brick at single target. Stuns for 2 turns.")
    cooldown: int = Field(default=3)
    power: int = Field(default=80)

    # ----------------------------------- CONSTANTS -----------------------------------
    STUN_DURATION: int = 2

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Scone Wall skill on a target."""
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
        """Level up Scone Wall - increases power."""
        self.level += 1
        self.power += 5
