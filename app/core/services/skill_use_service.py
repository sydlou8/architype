class SkillUseService:
    """Service for handling skill usage and related logic."""
    # Context dictionary for Effects
    # This will be passed to the effect handlers to allow them to modify the behavior of the entity based on the effect
    def make_effect_context() -> dict[str, Any]:
        return {
            # Damage Logic
            "skip_turn": False,                 # Used for effects like Stun that skip the entity's turn
            "silenced": False,                  # Used for effects like Silence that prevent the entity from using skills
            "muted": False,                     # Used for effects like Mute that prevent the entity from using magical skills
            "rooted": False,                    # Used for effects like Root that prevent the entity from moving
            "confused": False,                  # Used for effects like Confusion that may cause the entity to hurt itself
            
            # Action Flow
            "damage_blocked": False,            # Used for effects like Shield that block incoming damage
            "block_dot": False,                 # Used for effects like Endure that block damage over time effects

            # Extra Actions
            "extra_attacks": 0,                 # Used for effects like Double Attack that allow the entity to attack multiple times
            "extra_attack_multiplier" : 1.0,    # Used for effects that modify the power of extra attacks (e.g. Double Attack with a stat magnifier)
            
            # Targeting Logic
            "force_target": None,              # Used for effects that force the entity to target a specific enemy (e.g. Taunt)
        }
