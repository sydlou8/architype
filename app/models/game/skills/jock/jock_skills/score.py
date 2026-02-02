# hits single target enemy for high physical damage.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.jock_skills import JockSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType

class Score(BaseSkill):
    name: str = Field(default=JockSkills.SCORE.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Hits single target enemy for high physical damage.")
    cooldown: int = Field(default=2)
    power: int = Field(default=100)

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Score skill on a target."""
        # Calculate damage
        damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)
        
        # Apply damage to target
        target.take_damage(damage)

    def level_up(self) -> None:
        """Level up Score - increases power."""
        self.level += 1
        self.power += 10