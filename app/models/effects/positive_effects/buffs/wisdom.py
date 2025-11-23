from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, ModifierEffects
from models.enums.stat_types import StatType

class Wisdom(BaseEffect):
    name: str = Field(default=ModifierEffects.WISDOM.value)
    description: str = Field(default="A positive effect that increases magic damage.")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Wisdom effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.WISDOM.value,
            description="Doubles magical attack.",
            target=StatType.MAGICAL_ATTACK,
            stat_magnifier=self.BUFF_MULTIPLIER,
            duration=duration
        ))

        return effects