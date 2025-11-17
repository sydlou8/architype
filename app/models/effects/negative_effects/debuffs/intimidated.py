# halves critical chance for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, SideEffects
from models.enums.stat_types import StatType

class Intimidated(BaseEffect):
    name: str = Field(default=SideEffects.INTIMIDATED.value)
    description: str = Field(default="A negative effect that reduces critical chance.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Intimidated effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=SideEffects.INTIMIDATED.value,
            description="Halves critical chance.",
            target=StatType.CRITICAL_CHANCE,
            magnitude=self.DEBUFF_MULTIPLIER,
            duration=duration
        ))

        return effects