from enum import Enum

class BaristaSkills(Enum):
    TAKE_A_SHOT = "take_a_shot", # increase self dodge, speed, and physical_damage
    ESPRESSO_BOMB = "espresso_bomb", # causes burn for 5 turns, area damage
    GENDER_EXPRESSION = "gender_expression", # causes enemy confusion and rage for 5 turns, increases self dodge


