from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_type import EffectType

class Strengthen(BaseEffect):
    name: str = Field(default=EffectType.STRENGTHEN.value)
    description: str = Field(default="A positive effect that increases physical damage.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Strengthen effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.STRENGTHEN.value,
            description="Increases physical damage by 50%.",
            target=StatType.PHYSICAL_DAMAGE,
            magnitude=1.5,  
            duration=duration
        ))

        return effects