from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, MainEffects, SideEffects
from models.enums.stat_types import StatType

class Rage(BaseEffect):
    name: str = Field(default=MainEffects.RAGE.value)
    description: str = Field(default="A mixed effect that causes confusion (to be implemented), reduces dodge and accuracy, but increases physical damage.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Apply the Rage effect to the entity."""
        # TODO: Apply confusion damage
        # effects = []
        # effects.append(AppliedEffect(
        #     effect_name=EffectType.CONFUSION.value,
        #     description="Causes damage over time.",
        #     target=StatType.HEALTH,
        #     tick_magnitude=tick_value,
        #     duration=duration
        # ))
        # Apply debuffs: weakness and frailty
        # TODO: Adjust for unique effect -- currently stackable --> adjust magnitude after change
        effects.append(AppliedEffect(
            effect_name=SideEffects.STRENGTHEN.value,
            description="Increase physical damage dealt.",
            target=StatType.PHYSICAL_ATTACK,
            # is_unique_effect=True,
            magnitude=1.5,  # Example: increases physical damage by 50%
            duration=duration
        ))
        effects.append(AppliedEffect(
            effect_name=SideEffects.BLIND.value,
            description="Reduces accuracy.",
            target=StatType.ACCURACY,
            # is_unique_effect=True,
            magnitude=0.5,  # Example: reduces accuracy by 50%
            duration=duration
        ))
        effects.append(AppliedEffect(
            effect_name=SideEffects.CRIPPLED.value,
            description="Reduces dodge.",
            target=StatType.DODGE,
            # is_unique_effect=True,
            magnitude=0.5,  # Example: reduces dodge by 50%
            duration=duration
        ))

        return effects