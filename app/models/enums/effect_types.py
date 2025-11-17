from enum import Enum
from functools import wraps

effect_registry = {}

class EffectType(Enum):
    pass

class MainEffects(EffectType):
    # Positive Effects
    BULKED = "bulked"  # applies strengthen and defender for a duration
    EMPOWERED = "empowered"  # applies strengthen and wisdom for a duration
    ENCHANTED = "enchanted"  # applies wisdom and fortify for a duration
    INVIGORATE = "invigorate"  # applies haste and removes negative effects
    HIDDEN = "hidden"  # applies agility and removes negative effects
    BLESSED = "blessed"  # applies concecrated and wisdom for a duration
    REGENERATION = "regeneration"  # heals the affected entity over time for a duration
    SHIELD = "shield"  # blocks incoming damage for a duration
    ENDURE = "endure"  # applies defender and fortify and blocks DOT for a duration
    FOCUS = "focus"  # applies concentration and pierce for a duration

    # Mixed Effects
    BERSERK = "berserk"  # applies strengthen, haste, and pierce for a duration; however, also applies weakness and fatigue for a duration
    HYPED = "hyped"  # applies strengthen, wisdom, defender, fortify and haste for a duration; however, also applies frality and blind for a duration
    RAGE = "rage"  # increases physical damage, decreases dodge, decreases accuracy, may cause the affected entity to hurt itself for duration

    # Negative Effects
    BURN = "burn"  # causes damage over time (DOT) and applies weakness and 
    POISON = "poison" # causes DOT and applies fatigue for duration
    INTOXICATION = "intoxication"  # applies poison and daze for duration
    STUN = "stun"  # skips the affected entity's next turn for a duration
    SLEEP = "sleep"  # skips the affected entity's next few turns until woken up (damaged or duration ends)
    DAZE = "daze"  # applies blind and slow to the affected entity for duration
    CONFUSION = "confusion"  # may cause the affected entity to hurt itself for duration
    CURSE = "curse"  # causes DOT and applies weakness and fatigue for duration
    SILENCE = "silence"  # prevents the affected entity from using skills for duration
    MUTE = "mute"  # prevents the use of magical skills for duration
    ROOT = "root"  # prevents the affected entity from using physical skills for duration

class SideEffects(EffectType):
    # Buffs
    STRENGTHEN = "strengthen"  # increases physical attack
    WISDOM = "wisdom"  # increases magical attack
    DEFENDER = "defender"  # increases physical defense
    FORTIFY = "fortify"  # increases magical defense
    HASTE = "haste"  # increases speed
    AGILITY = "agility"  # increases dodge
    PIERCE = "pierce"  # increases critical chance
    CONCENTRATION = "concentration"  # increases accuracy
    CONCECRATED = "concecrated"  # increases healing received 

    # Debuffs
    WEAKNESS = "weakness"  # reduces physical attack
    FATIGUE = "fatigue"  # reduces magical attack
    SLOW = "slow"  # reduces speed
    BLIND = "blind"  # reduces accuracy
    CRIPPLED = "crippled"  # reduces dodge 
    FRAILTY = "frailty"  # reduces healing received
    INTIMIDATED = "intimidated"  # reduces critical chance

def register_effect(effect_type: EffectType):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(self, *args, **kwargs)
        effect_registry[effect_type] = func
        return wrapper
    return decorator
