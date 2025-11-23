# Heal over time effect
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_over_time_effect import AppliedOverTimeEffect
from models.enums.effect_types import OverTimeEffects
from models.enums.stat_types import StatType

class HoT(BaseEffect):
    name: str = Field(default=OverTimeEffects.HEALING.value)
    description: str = Field(default="A positive effect that heals over time.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedOverTimeEffect]:
        """Generate the Heal over Time effect to the entity."""

        effects = []
        effects.append(AppliedOverTimeEffect(
            effect_name=OverTimeEffects.HEALING.value,
            description="Heals over time.",
            target=StatType.HEALTH,
            tick_value=tick_value,
            duration=duration
        ))

        return effects