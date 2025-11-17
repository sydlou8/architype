from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_type import EffectType

class Focus(BaseEffect):
    name: str = Field(default=EffectType.FOCUS.value)
    description: str = Field(default="A positive effect that applies concentration and pierce.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Focus effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.CONCENTRATION.value,
            description="Increases concentration and pierce.",
            target=StatType.FOCUS,
            magnitude=1.5, 
            duration=duration
        ))
        effects.append(AppliedEffect(
            effect_name=EffectType.PIERCE.value,
            description="Increases pierce.",
            target=StatType.PIERCE,
            magnitude=1.5,
            duration=duration
        ))

        return effects