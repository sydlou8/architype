# applies blind and slow for duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects
from models.game.effects.negative_effects.debuffs.blind import Blind
from models.game.effects.negative_effects.debuffs.slow import Slow

class Daze(BaseEffect):
    name: str = Field(default=StatusEffects.DAZE.value)
    description: str = Field(default="A negative effect that applies blind and slow.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Daze effect to the entity."""

        effects = []
        # Apply Blind effect
        blind_effects = Blind().generate_effects(duration=duration)
        effects.extend(blind_effects)

        # Apply Slow effect
        slow_effects = Slow().generate_effects(duration=duration)
        effects.extend(slow_effects)

        return effects
