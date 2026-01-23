# inflicts small physical damage to all enemies.
# applies burn for 4 turns (2 damage per turn)
# multi-target physical damage skill
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.enums.skills.barista_skills import BaristaSkills

