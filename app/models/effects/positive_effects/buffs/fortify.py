from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, SideEffects
from models.enums.stat_types import StatType

class Fortify(BaseEffect):
    name: str = Field(default=SideEffects.FORTIFY.value)
    description: str = Field(default="A positive effect that increases magic defense.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Fortify effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=SideEffects.FORTIFY.value,
            description="Increases magic defense by 50%.",
            target=StatType.MAGICAL_DEFENSE,
            magnitude=1.5,  
            duration=duration
        ))

        return effects