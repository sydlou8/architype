# halves critical chance for a duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import EffectType, ModifierEffects
from models.game.enums.stat_types import StatType

class Intimidated(BaseEffect):
    name: str = Field(default=ModifierEffects.INTIMIDATED.value)
    description: str = Field(default="A negative effect that reduces critical chance.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Intimidated effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.INTIMIDATED.value,
            description="Halves critical chance.",
            target=StatType.CRITICAL_CHANCE,
            stat_magnifier=self.DEBUFF_MULTIPLIER,
            duration=duration
        ))

        return effects