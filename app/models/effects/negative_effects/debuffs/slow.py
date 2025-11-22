# Halves speed for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, SideEffects
from models.enums.stat_types import StatType

class Slow(BaseEffect):
    name: str = Field(default=SideEffects.SLOW.value)
    description: str = Field(default="A negative effect that reduces speed.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Slow effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=SideEffects.SLOW.value,
            description="Halves speed.",
            target=StatType.SPEED,
            stat_magnifier=self.DEBUFF_MULTIPLIER,
            duration=duration
        ))

        return effects