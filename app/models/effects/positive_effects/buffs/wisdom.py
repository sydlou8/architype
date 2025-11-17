from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_type import EffectType

class Wisdom(BaseEffect):
    name: str = Field(default=EffectType.WISDOM.value)
    description: str = Field(default="A positive effect that increases magic damage.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Wisdom effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.WISDOM.value,
            description="Increases magic damage by 50%.",
            target=StatType.MAGIC_DAMAGE,
            magnitude=1.5, 
            duration=duration
        ))

        return effects