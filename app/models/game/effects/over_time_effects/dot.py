# Damage over time effect
from sqlmodel import Field
from models.game.effects.over_time_effects.base_over_time_effect import BaseOverTimeEffect
from models.game.effects.applied_over_time_effect import AppliedOverTimeEffect
from models.game.enums.effect_types import OverTimeEffects
from models.game.enums.stat_types import StatType

class DoT(BaseOverTimeEffect):
    name: str = Field(default=OverTimeEffects.DAMAGE.value)
    description: str = Field(default="A negative effect that deals damage over time.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedOverTimeEffect]:
        """Generate the Damage over Time effect to the entity."""

        effects = []
        effects.append(AppliedOverTimeEffect(
            effect_name=OverTimeEffects.DAMAGE.value,
            description="Deals damage over time.",
            target=StatType.HEALTH,
            tick_value=-tick_value,
            duration=duration
        ))

        return effects