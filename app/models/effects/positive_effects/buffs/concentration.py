from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, ModifierEffects
from models.enums.stat_types import StatType

class Concentration(BaseEffect):
    name: str = Field(default=ModifierEffects.CONCENTRATION.value)
    description: str = Field(default="A positive effect that increases accuracy.")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Concentration effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.CONCENTRATION.value,
            description="Doubles accuracy.",
            target=StatType.ACCURACY,
            stat_magnifier=self.BUFF_MULTIPLIER,  
            duration=duration
        ))

        return effects