from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, SideEffects
from models.enums.stat_types import StatType

class Strengthen(BaseEffect):
    name: str = Field(default=SideEffects.STRENGTHEN.value)
    description: str = Field(default="A positive effect that increases physical damage.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Strengthen effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=SideEffects.STRENGTHEN.value,
            description="Increases physical damage by 50%.",
            target=StatType.PHYSICAL_ATTACK,
            magnitude=1.5,  
            duration=duration
        ))

        return effects