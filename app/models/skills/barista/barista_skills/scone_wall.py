# throws a scone the size of a brick at single target. Stuns for 2 turns.
# single target physical damage skill
from sqlmodel import Field
from models.skills.base_skill import BaseSkill
from models.entities.base_entity import BaseEntity
from models.enums.skills.barista_skills import BaristaSkills
from models.enums.skill_types import SkillType

class SconeWall(BaseSkill):
    name: str = Field(default=BaristaSkills.SCONE_WALL.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Throws a scone the size of a brick at single target. Stuns for 2 turns.")

    power: int = Field(default=80)

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Scone Wall skill on a target."""
        # Calculate damage
        damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)
        
        # Apply damage to target
        target.current_hp -= damage
