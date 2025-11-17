from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, SideEffects
from models.enums.stat_types import StatType

class Concentration(BaseEffect):
    name: str = Field(default=SideEffects.CONCENTRATION.value)
    description: str = Field(default="A positive effect that increases accuracy.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Concentration effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=SideEffects.CONCENTRATION.value,
            description="Doubles accuracy.",
            target=StatType.ACCURACY,
            magnitude=self.BUFF_MULTIPLIER,  
            duration=duration
        ))

        return effects