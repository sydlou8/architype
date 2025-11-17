from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, MainEffects, SideEffects
from models.enums.stat_types import StatType

class Burn(BaseEffect):
    name: str = Field(default=MainEffects.BURN.value)
    description: str = Field(default="A negative effect that causes damage over time and reduces physical damage and healing received.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Apply the Burn effect to the entity."""
        # Apply burn damage
        effects = []
        effects.append(AppliedEffect(
            effect_name=MainEffects.BURN.value,
            description="Causes damage over time.",
            target=StatType.HEALTH,
            tick_magnitude=tick_value,
            duration=duration
        ))

        # Apply debuffs: weakness and frailty
        # TODO: Adjust for unique effect -- currently stackable --> adjust magnitude after change
        effects.append(AppliedEffect(
            effect_name=SideEffects.WEAKEN.value,
            description="Reduces physical damage dealt.",
            target=StatType.PHYSICAL_ATTACK,
            # is_unique_effect=True,
            magnitude=0.9,  # Example: reduces physical damage by 10%
            duration=duration
        ))
        effects.append(AppliedEffect(
            effect_name=SideEffects.FRAILTY.value,
            description="Reduces healing received.",
            target=StatType.HEALING_MODIFIER,
            # is_unique_effect=True,
            magnitude=0.9,  # Example: reduces healing received by 10%
            duration=duration
        ))

        return effects