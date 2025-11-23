# halves dodge for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, ModifierEffects
from models.enums.stat_types import StatType

class Crippled(BaseEffect):
    name: str = Field(default=ModifierEffects.CRIPPLED.value)
    description: str = Field(default="A negative effect that reduces dodge chance.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Crippled effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.CRIPPLED.value,
            description="Halves dodge chance.",
            target=StatType.DODGE,
            stat_magnifier=self.DEBUFF_MULTIPLIER,
            duration=duration
        ))

        return effects