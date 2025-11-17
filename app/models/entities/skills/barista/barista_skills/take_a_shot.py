from sqlmodel import Field

from models.entities.base_entity import BaseEntity
from models.entities.skills.base_skill import BaseSkill
from models.entities.enums.skills.barista_skills import BaristaSkills
from models.entities.enums.skill_types import SkillType

class TakeAShot(BaseSkill):
    name: str = Field(default=BaristaSkills.TAKE_A_SHOT.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default="Self buffing skill that increases user's dodge, accuracy, speed, and physical damage.")

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Take a Shot skill on a target."""
        user.dodge *= 1.5  # Increase dodge by 50%
        user.accuracy *= 1.5  # Increase accuracy by 50%
        user.speed *= 1.5  # Increase speed by 50%
        user.attack *= 1.5  # Increase physical damage by 50%