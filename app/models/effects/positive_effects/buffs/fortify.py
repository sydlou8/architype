from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_type import EffectType

class Fortify(BaseEffect):
    name: str = Field(default=EffectType.FORTIFY.value)
    description: str = Field(default="A positive effect that increases magic defense.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Fortify effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.FORTIFY.value,
            description="Increases magic defense by 50%.",
            target=StatType.MAGIC_DEFENSE,
            magnitude=1.5,  
            duration=duration
        ))

        return effects