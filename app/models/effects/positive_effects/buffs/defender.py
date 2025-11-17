from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_type import EffectType

class Defender(BaseEffect):
    name: str = Field(default=EffectType.DEFENDER.value)
    description: str = Field(default="A positive effect that increases physical defense.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Defender effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.DEFENDER.value,
            description="Increases physical defense by 50%.",
            target=StatType.PHYSICAL_DEFENSE,
            magnitude=1.5, 
            duration=duration
        ))

        return effects