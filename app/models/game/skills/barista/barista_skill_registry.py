from enum import Enum
from typing import Any, Callable
from models.game.enums.skills.barista.barista_skills import BaristaSkills

barista_skills = {}

def register_barista_skill(skill: BaristaSkills):
    ''' Registers a difficulty level with its associated configuration. '''
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        barista_skills[skill] = func
        return func
    return decorator

@register_barista_skill(BaristaSkills.TAKE_A_SHOT)
def take_a_shot():
    """Placeholder for take a shot skill implementation."""
    pass