# reduces physical damage by 50% for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, SideEffects
from models.enums.stat_types import StatType

class Weaken(BaseEffect):
    name: str = Field(default=SideEffects.WEAKEN.value)
    description: str = Field(default="A negative effect that reduces physical attack.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Weaken effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=SideEffects.WEAKEN.value,
            description="Halves physical attack.",
            target=StatType.PHYSICAL_ATTACK,
            magnitude=self.DEBUFF_MULTIPLIER,
            duration=duration
        ))

        return effects