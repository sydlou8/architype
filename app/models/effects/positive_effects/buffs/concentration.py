from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_type import EffectType

class Concentration(BaseEffect):
    name: str = Field(default=EffectType.CONCENTRATION.value)
    description: str = Field(default="A positive effect that increases accuracy.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Concentration effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.CONCENTRATION.value,
            description="Increases accuracy by 50%.",
            target=StatType.ACCURACY,
            magnitude=1.5,  
            duration=duration
        ))

        return effects