# Damage over time effect
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import OverTimeEffect
from models.enums.stat_types import StatType

class DoT(BaseEffect):
    name: str = Field(default=OverTimeEffect.DAMAGE.value)
    description: str = Field(default="A negative effect that deals damage over time.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Damage over Time effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=OverTimeEffect.DAMAGE.value,
            description="Deals damage over time.",
            target=StatType.HEALTH,
            magnitude=-tick_value,
            duration=duration
        ))

        return effects