# reduces magical damage by 50% for a duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import EffectType, ModifierEffects
from models.game.enums.stat_types import StatType

class Fatigue(BaseEffect):
    name: str = Field(default=ModifierEffects.FATIGUE.value)
    description: str = Field(default="A negative effect that reduces magical damage.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Fatigue effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.FATIGUE.value,
            description="Halves magical attack.",
            target=StatType.MAGICAL_ATTACK,
            stat_magnifier=self.DEBUFF_MULTIPLIER,
            duration=duration
        ))

        return effects