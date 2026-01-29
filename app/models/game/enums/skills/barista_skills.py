from enum import Enum

class BaristaSkills(Enum):
    TAKE_A_SHOT = "take_a_shot"  # increase self dodge, speed, and physical_damage
    DOUBLE_SHOT = "double_shot"  # ranged attack that hits twice with burn chance
    ESPRESSO_BOMB = "espresso_bomb"  # causes burn for 5 turns, area damage
    GENDER_ESPRESSO_N = "gender_espresso_n"  # causes enemy confusion and rage for 5 turns, increases self dodge
    BATCH_BREW = "batch_brew"  # support skill for party buffs
    SCONE_WALL = "scone_wall"  # defensive skill
    WHATS_TEA = "whats_tea"  # information/debuff skill


