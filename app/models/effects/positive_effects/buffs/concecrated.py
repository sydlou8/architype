from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, SideEffects
from models.enums.stat_types import StatType

class Concecrated(BaseEffect):
    name: str = Field(default=SideEffects.CONCECRATED.value)
    description: str = Field(default="A positive effect that increases healing received.")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Concecrated effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=SideEffects.CONCECRATED.value,
            description="Doubles healing received.",
            target=StatType.HEALING_MODIFIER,
            stat_magnifier=self.BUFF_MULTIPLIER,
            duration=duration
        ))

        return effects