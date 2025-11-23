# applies poison and daze for duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import StatusEffects
from models.effects.negative_effects.status_effects.poison import Poison
from models.effects.negative_effects.debuffs.daze import Daze

class Intoxication(BaseEffect):
    name: str = Field(default=StatusEffects.INTOXICATION.value)
    description: str = Field(default="A negative effect that applies poison and daze.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Apply the Intoxication effect to the entity."""

        effects = []
        # Apply Poison effect
        poison_effects = Poison().generate_effects(duration=duration, tick_value=tick_value)
        effects.extend(poison_effects)

        # Apply Daze effect
        daze_effects = Daze().generate_effects(duration=duration)
        effects.extend(daze_effects)

        return effects