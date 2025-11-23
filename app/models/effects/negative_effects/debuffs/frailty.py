# halves healing received for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, ModifierEffects
from models.enums.stat_types import StatType

class Frailty(BaseEffect):
    name: str = Field(default=ModifierEffects.FRAILITY.value)
    description: str = Field(default="A negative effect that reduces healing received.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Frailty effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.FRAILITY.value,
            description="Halves healing received.",
            target=StatType.HEALING_MODIFIER,
            stat_magnifier=self.DEBUFF_MULTIPLIER,
            duration=duration
        ))

        return effects