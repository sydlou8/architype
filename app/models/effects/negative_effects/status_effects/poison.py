# causes dot and applies weaken and vulnerable for duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import StatusEffects
from models.effects.negative_effects.debuffs.fatigue import Fatigue
from models.effects.negative_effects.debuffs.vulnerable import Vulnerable
from models.effects.over_time_effects.dot import DoT

class Poison(BaseEffect):
    name: str = Field(default=StatusEffects.POISON.value)
    description: str = Field(default="A negative effect that causes damage over time and applies fatigue and vulnerable.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Apply the Poison effect to the entity."""
        # Apply poison damage
        effects = []
        dot_effects = DoT().generate_effects(duration=duration, tick_value=tick_value)
        effects.extend(dot_effects)

        # Apply debuffs: fatigue and vulnerable
        # TODO: Adjust for unique effect -- currently stackable --> adjust stat_magnifier after change
        # Apply Fatigue
        fatigue = Fatigue()
        fatigue.stat_magnifier = 0.9
        fatigue_effects = fatigue.generate_effects(duration=duration)
        effects.extend(fatigue_effects)

        # Apply Vulnerable
        vulnerable = Vulnerable()
        vulnerable.stat_magnifier = 0.9
        vulnerable_effects = vulnerable.generate_effects(duration=duration)
        effects.extend(vulnerable_effects)
        
        return effects