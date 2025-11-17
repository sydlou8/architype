from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, MainEffects, SideEffects
from models.enums.stat_types import StatType

class Focus(BaseEffect):
    name: str = Field(default=MainEffects.FOCUS.value)
    description: str = Field(default="A positive effect that applies concentration and pierce.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Focus effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=SideEffects.CONCENTRATION.value,
            description="Increases accuracy.",
            target=StatType.ACCURACY,
            magnitude=1.5, 
            duration=duration
        ))
        effects.append(AppliedEffect(
            effect_name=SideEffects.PIERCE.value,
            description="Increases critical chance.",
            target=StatType.CRITICAL_CHANCE,
            magnitude=1.5,
            duration=duration
        ))

        return effects