from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_type import EffectType

class Pierce(BaseEffect):
    name: str = Field(default=EffectType.PIERCE.value)
    description: str = Field(default="A positive effect that increases critical chance.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Pierce effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.PIERCE.value,
            description="Doubles critical chance.",
            target=StatType.CRITICAL_CHANCE,
            magnitude=2.0,  
            duration=duration
        ))

        return effects