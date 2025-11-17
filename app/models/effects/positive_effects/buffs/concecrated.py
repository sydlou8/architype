from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_type import EffectType

class Concecrated(BaseEffect):
    name: str = Field(default=EffectType.CONCECRATED.value)
    description: str = Field(default="A positive effect that increases healing received.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Concecrated effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.CONCECRATED.value,
            description="Doubles healing received.",
            target=StatType.HEALING_RECEIVED,
            magnitude=2,  
            duration=duration
        ))

        return effects