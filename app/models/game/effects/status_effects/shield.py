# Blocks incoming damage for a certain duration.
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import EffectType, StatusEffects
from models.game.enums.stat_types import StatType

class Shield(BaseEffect):
    name: str = Field(default=StatusEffects.SHIELD.value)
    description: str = Field(default="A positive effect that blocks incoming damage.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Shield effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=StatusEffects.SHIELD.value,
            description="Blocks incoming damage.",
            target=StatType.NONE,
            stat_magnifier=0,
            duration=duration
        ))

        return effects