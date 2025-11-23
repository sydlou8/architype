# reduces physical defense by 50% for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, ModifierEffects
from models.enums.stat_types import StatType

class Vulnerable(BaseEffect):
    name: str = Field(default=ModifierEffects.VULNERABLE.value)
    description: str = Field(default="A negative effect that reduces physical defense.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Vulnerable effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.VULNERABLE.value,
            description="Halves physical defense.",
            target=StatType.PHYSICAL_DEFENSE,
            stat_magnifier=self.DEBUFF_MULTIPLIER,
            duration=duration
        ))

        return effects