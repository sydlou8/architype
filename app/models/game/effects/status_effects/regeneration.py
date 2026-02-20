# heals the affected entity over time for a duration
# TODO: implement stacking behavior for regeneration effects
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_over_time_effect import AppliedOverTimeEffect
from models.game.enums.effect_types import StatusEffects
from models.game.enums.stat_types import StatType


class Regeneration(BaseEffect):
    name: str = Field(default=StatusEffects.REGENERATION.value)
    description: str = Field(default="Heals the affected entity over time.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedOverTimeEffect]:
        """Generate the Regeneration effect to the entity."""

        effects = []
        effects.append(AppliedOverTimeEffect(
            effect_name=StatusEffects.REGENERATION.value,
            description="Heals over time.",
            target=StatType.HEALTH,
            tick_value=tick_value,
            duration=duration
        ))

        return effects
