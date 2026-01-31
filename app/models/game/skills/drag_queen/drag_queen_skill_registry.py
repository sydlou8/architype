"""
Drag Queen Skill Registry - Central registry for all Drag Queen skills.

This registry allows for:
- Dynamic skill loading from database
- Player skill customiztion
- Easy addition of new skills
- Skill unlocking systems
    
"""

from models.game.enums.skills.drag_queen_skills import DragQueenSkills
from models.game.skills.base_skill import BaseSkill
from models.game.skills.base_skill_registry import BaseSkillRegistry
from models.game.skills.drag_queen.drag_queen_skills.applause import Applause
from models.game.skills.drag_queen.drag_queen_skills.boots_down import BootsDown
from models.game.skills.drag_queen.drag_queen_skills.clock_it import ClockIt
from models.game.skills.drag_queen.drag_queen_skills.death_drop import DeathDrop
from models.game.skills.drag_queen.drag_queen_skills.fish import Fish
from models.game.skills.drag_queen.drag_queen_skills.gaggy import Gaggy
from models.game.skills.drag_queen.drag_queen_skills.tip_your_queen import TipYourQueen

class DragQueenSkillRegistry(BaseSkillRegistry[DragQueenSkills]):
    # The registry: maps skill enums to skill classes
    REGISTRY: dict[DragQueenSkills, type[BaseSkill]] = {
        DragQueenSkills.APPLAUSE: Applause,
        DragQueenSkills.BOOTS_DOWN: BootsDown,
        DragQueenSkills.CLOCK_IT: ClockIt,
        DragQueenSkills.DEATH_DROP: DeathDrop,
        DragQueenSkills.FISH: Fish,
        DragQueenSkills.GAGGY: Gaggy,
        DragQueenSkills.TIP_YOUR_QUEEN: TipYourQueen,
    }
