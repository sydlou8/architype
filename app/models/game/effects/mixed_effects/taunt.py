# forces enemies to target the user for a duration.abs
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import EffectType, StatusEffects
from models.game.enums.stat_types import StatType

class Taunt(BaseEffect):
    name: str = Field(default=StatusEffects.TAUNT.value)
    description: str = Field(default="Forces enemies to target the user for a duration.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Taunt effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=StatusEffects.TAUNT.value,
            description="Forces enemies to target the user for a duration.",
            target=StatType.NONE,
            stat_magnifier=0,
            duration=duration
        ))

        return effects