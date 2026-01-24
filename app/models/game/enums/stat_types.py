from typing import Any, Callable
from enum import Enum, auto
from functools import wraps

stats_registry = {}

class StatType(Enum):
    HEALTH = auto()
    PHYSICAL_ATTACK = auto()
    MAGICAL_ATTACK = auto()
    PHYSICAL_DEFENSE = auto()
    MAGICAL_DEFENSE = auto()
    SPEED = auto()
    DODGE = auto()
    ACCURACY = auto()
    CRITICAL_CHANCE = auto()
    HEALING_MODIFIER = auto()
    FINAL_DAMAGE_MODIFIER = auto()

def register_stat(stat_type: StatType) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> int | float:
            return func(*args, **kwargs)
        stats_registry[stat_type] = wrapper
        return wrapper
    return decorator