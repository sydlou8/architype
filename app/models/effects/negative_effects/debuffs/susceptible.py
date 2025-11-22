# halves magical defense for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, SideEffects
from models.enums.stat_types import StatType

class Susceptible(BaseEffect):
    name: str = Field(default=SideEffects.SUSCEPTIBLE.value)
    description: str = Field(default="A negative effect that reduces magical defense.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Susceptible effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=SideEffects.SUSCEPTIBLE.value,
            description="Halves magical defense.",
            target=StatType.MAGICAL_DEFENSE,
            stat_magnifier=self.DEBUFF_MULTIPLIER,
            duration=duration
        ))

        return effects