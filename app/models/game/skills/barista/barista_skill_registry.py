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
from models.game.skills.barista.barista_skills.take_a_shot import TakeAShot
from models.game.skills.barista.barista_skills.double_shot import DoubleShot
from models.game.skills.barista.barista_skills.espresso_bomb import EspressoBomb
from models.game.skills.barista.barista_skills.gender_espresso_n import GenderEspressoN
from models.game.skills.barista.barista_skills.batch_brew import BatchBrew
from models.game.skills.barista.barista_skills.scone_wall import SconeWall
from models.game.skills.barista.barista_skills.whats_tea import WhatsTea


# The registry: maps skill enums to skill classes
BARISTA_SKILLS_REGISTRY: dict[BaristaSkills, type[BaseSkill]] = {
    BaristaSkills.TAKE_A_SHOT: TakeAShot,
    BaristaSkills.DOUBLE_SHOT: DoubleShot,
    BaristaSkills.ESPRESSO_BOMB: EspressoBomb,
    BaristaSkills.GENDER_ESPRESSO_N: GenderEspressoN,
    BaristaSkills.BATCH_BREW: BatchBrew,
    BaristaSkills.SCONE_WALL: SconeWall,
    BaristaSkills.WHATS_TEA: WhatsTea,
}


def get_barista_skill(skill_enum: BaristaSkills) -> BaseSkill:
    """
    Factory function to create a Barista skill instance from the registry.
    
    Args:
        skill_enum: The BaristaSkills enum value
        
    Returns:
        An instance of the requested skill
        
    Raises:
        ValueError: If the skill is not found in the registry
        
    Example:
        >>> skill = get_barista_skill(BaristaSkills.DOUBLE_SHOT)
        >>> skill.use(attacker, defender)
    """
    skill_class = BARISTA_SKILLS_REGISTRY.get(skill_enum)
    
    if skill_class is None:
        raise ValueError(f"Unknown Barista skill: {skill_enum}")
    
    return skill_class()


def get_all_barista_skills() -> list[BaristaSkills]:
    """
    Get a list of all available Barista skills.
    
    Returns:
        List of all BaristaSkills enum values in the registry
    """
    return list(BARISTA_SKILLS_REGISTRY.keys())


def is_valid_barista_skill(skill_enum: BaristaSkills) -> bool:
    """
    Check if a skill is registered in the Barista registry.
    
    Args:
        skill_enum: The BaristaSkills enum value to check
        
    Returns:
        True if the skill is registered, False otherwise
    """
    return skill_enum in BARISTA_SKILLS_REGISTRY