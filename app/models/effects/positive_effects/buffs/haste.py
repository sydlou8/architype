from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_type import EffectType

class Haste(BaseEffect):
    name: str = Field(default=EffectType.HASTE.value)
    description: str = Field(default="A positive effect that increases speed.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Haste effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.HASTE.value,
            description="Increases speed by 50%.",
            target=StatType.SPEED,
            magnitude=1.5, 
            duration=duration
        ))

        return effects