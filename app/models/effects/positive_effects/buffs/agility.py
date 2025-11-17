from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_type import EffectType

class Agility(BaseEffect):
    name: str = Field(default=EffectType.AGILITY.value)
    description: str = Field(default="A positive effect that increases dodge chance.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Agility effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.AGILITY.value,
            description="Increases dodge chance by 50%.",
            target=StatType.DODGE,
            magnitude=1.5, 
            duration=duration
        ))

        return effects