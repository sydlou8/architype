"""
Barista Skill Registry - Central registry for all Barista skills.

This registry allows for:
- Dynamic skill loading from database
- Player skill customization
- Easy addition of new skills
- Skill unlocking systems
"""

from models.game.enums.skills.barista_skills import BaristaSkills
from models.game.skills.base_skill import BaseSkill
from models.game.skills.base_skill_registry import BaseSkillRegistry
from models.game.skills.barista.barista_skills.take_a_shot import TakeAShot
from models.game.skills.barista.barista_skills.double_shot import DoubleShot
from models.game.skills.barista.barista_skills.espresso_bomb import EspressoBomb
from models.game.skills.barista.barista_skills.gender_espresso_n import GenderEspressoN
from models.game.skills.barista.barista_skills.batch_brew import BatchBrew
from models.game.skills.barista.barista_skills.scone_wall import SconeWall
from models.game.skills.barista.barista_skills.whats_tea import WhatsTea

class BaristaSkillRegistry(BaseSkillRegistry[BaristaSkills]):
    # The registry: maps skill enums to skill classes
    REGISTRY: dict[BaristaSkills, type[BaseSkill]] = {
        BaristaSkills.TAKE_A_SHOT: TakeAShot,
        BaristaSkills.DOUBLE_SHOT: DoubleShot,
        BaristaSkills.ESPRESSO_BOMB: EspressoBomb,
        BaristaSkills.GENDER_ESPRESSO_N: GenderEspressoN,
        BaristaSkills.BATCH_BREW: BatchBrew,
        BaristaSkills.SCONE_WALL: SconeWall,
        BaristaSkills.WHATS_TEA: WhatsTea,
    }