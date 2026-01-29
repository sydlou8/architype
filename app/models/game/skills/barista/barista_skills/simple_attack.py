"""Simple attack skill for testing - no effects, just damage."""
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType

class SimpleAttack(BaseSkill):
    name: str = Field(default="Simple Attack")
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="A basic attack with no special effects.")
    power: int = Field(default=50)  # 50% of attack stat

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use simple attack on a target - just deals damage."""
        damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)
        target.take_damage(damage)
    
    def level_up(self) -> None:
        """Level up Simple Attack - increases power."""
        self.level += 1
        self.power += 10  # +10% damage per level
