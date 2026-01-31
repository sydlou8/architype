"""
Biker Skill Registry - Central registry for all Biker skills.

This registry allows for:
- Dynamic skill loading from database
- Player skill customization
- Easy addition of new skills
- Skill unlocking systems
"""

from models.game.enums.skills.biker_skills import BikerSkills
from models.game.skills.base_skill import BaseSkill
from models.game.skills.base_skill_registry import BaseSkillRegistry
from models.game.skills.biker.biker_skills.charge import Charge
from models.game.skills.biker.biker_skills.crash import Crash
from models.game.skills.biker.biker_skills.gang_gang import GangGang
from models.game.skills.biker.biker_skills.gear_up import GearUp
from models.game.skills.biker.biker_skills.lets_ride import LetsRide
from models.game.skills.biker.biker_skills.shout import Shout
from models.game.skills.biker.biker_skills.wheel_spikes import WheelSpikes
from models.game.skills.biker.biker_skills.wheelie import Wheelie

class BikerSkillRegistry(BaseSkillRegistry[BikerSkills]):
    # The registry: maps skill enums to skill classes
    REGISTRY: dict[BikerSkills, type[BaseSkill]] = {
        BikerSkills.CHARGE: Charge,
        BikerSkills.CRASH: Crash,
        BikerSkills.GANG_GANG: GangGang,
        BikerSkills.GEAR_UP: GearUp,
        BikerSkills.LETS_RIDE: LetsRide,
        BikerSkills.SHOUT: Shout,
        BikerSkills.WHEEL_SPIKES: WheelSpikes,
        BikerSkills.WHEELIE: Wheelie,
    }