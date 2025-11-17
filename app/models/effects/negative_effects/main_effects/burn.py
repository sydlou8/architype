from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import MainEffects
from models.effects.negative_effects.debuffs.weaken import Weaken
from models.effects.negative_effects.debuffs.frailty import Frailty
from models.effects.over_time_effects.dot import DoT

class Burn(BaseEffect):
    name: str = Field(default=MainEffects.BURN.value)
    description: str = Field(default="A negative effect that causes damage over time and applies weaken and frailty.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Apply the Burn effect to the entity."""
        # Apply burn damage
        effects = []
        dot_effects = DoT().generate_effects(duration=duration, tick_value=tick_value)
        effects.extend(dot_effects)

        # Apply debuffs: weakness and frailty
        # TODO: Adjust for unique effect -- currently stackable --> adjust magnitude after change
        # Apply Weaken
        weaken = Weaken()
        weaken.magnitude = 0.9  
        weaken_effects = weaken.generate_effects(duration=duration)
        effects.extend(weaken_effects)

        # Apply Frailty
        frailty = Frailty()
        frailty.magnitude = 0.9
        frailty_effects = frailty.generate_effects(duration=duration)
        effects.extend(frailty_effects)

        return effects