"""
Jock Skill Registry - Central registry for all Jock skills.

This registry allows for:
- Dynamic skill loading from database
- Player skill customization
- Easy addition of new skills
- Skill unlocking systems
"""

from models.game.enums.skills.jock_skills import JockSkills
from models.game.skills.base_skill import BaseSkill
from models.game.skills.base_skill_registry import BaseSkillRegistry
from models.game.skills.jock.jock_skills.detox_and_refresh import DetoxAndRefresh
from models.game.skills.jock.jock_skills.formation_ate import FormationAte
from models.game.skills.jock.jock_skills.high_jump_kick import HighJumpKick
from models.game.skills.jock.jock_skills.power_tackle import PowerTackle
from models.game.skills.jock.jock_skills.recover import Recover
from models.game.skills.jock.jock_skills.score import Score
from models.game.skills.jock.jock_skills.spike import Spike
from models.game.skills.jock.jock_skills.warmup import Warmup

class JockSkillRegistry(BaseSkillRegistry[JockSkills]):
    # The registry: maps skill enums to skill classes
    REGISTRY: dict[JockSkills, type[BaseSkill]] = {
        JockSkills.DETOX_AND_REFRESH: DetoxAndRefresh,
        JockSkills.FORMATION_ATE: FormationAte,
        JockSkills.HIGH_JUMP_KICK: HighJumpKick,
        JockSkills.POWER_TACKLE: PowerTackle,
        JockSkills.RECOVER: Recover,
        JockSkills.SCORE: Score,
        JockSkills.SPIKE: Spike,
        JockSkills.WARMUP: Warmup,
    }


def get_jock_skill(skill_enum: JockSkills) -> BaseSkill:
    return JockSkillRegistry.get_skill(skill_enum)
