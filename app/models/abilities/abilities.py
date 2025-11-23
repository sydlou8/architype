from enum import Enum

class Abilities(Enum):
    # Abilities every class can have
    PASSIVE_HEALING = "Passive Healing"
    CRITICAL_STRIKE = "Critical Strike"
    EVASION = "Evasion"

class AllyAbilities(Abilities):
    # Ally specific abilities
    SUPPORTIVE_AURA = "Supportive Aura"         # Increases allies' healing received by 20%
    PROTECTOR = "Protector"                     # Doubles base hp, 

class BaristaAblities(Abilities):
    # Barista specific abilities
    MORNING_RUSH = "Morning Rush"               # Increases speed by 50% at the start of battle, 
    CAFFEINATED = "Caffeinated"                 # Player cannot be stunned or slept
    HOTTIE_HOTTIE = " Hottie Hottie"            # Can inflict burn for 5 turns when hit with physical attacks

class DragQueenAbilities(Abilities):
    # Drag Queen specific abilities
    SHOWTIME = "Showtime"                       # All status effect resistances are doubled for the first 3 turns
    GAGGY = "Gaggy"                             # All attacks have an extra 30% to stun the target
    COSTUME_CHANGE = "Costume Change"           # Once per battle, can fully heal self when health drops below 30%