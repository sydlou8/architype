from sqlmodel import Field

from models.entities.base_entity import BaseEntity
from models.entities.effects.base_effect import BaseEffect
from models.entities.enums.effect_type import EffectType
from models.entities.effects.applied_effect import AppliedEffect

class Burn(BaseEffect):
    name: str = Field(default=EffectType.BURN.value)
    description: str = Field(default="A negative effect that causes damage over time and reduces physical damage and healing received.")

    def apply(self, entity: BaseEntity, duration: int = 0, tick_value: int = 0) -> None:
        """Apply the Burn effect to the entity."""
        # Apply burn damage
        effects = []
        effects.append(AppliedEffect(
            effect_name=EffectType.BURN.value,
            description="Causes damage over time.",
            target=StatType.HEALTH,
            tick_magnitude=tick_value,
            duration=duration
        ))

        # Apply debuffs: weakness and frailty
        # TODO: Adjust for unique effect -- currently stackable --> adjust magnitude after change
        effects.append(AppliedEffect(
            effect_name=EffectType.WEAKNESS.value,
            description="Reduces physical damage dealt.",
            target=StatType.PHYSICAL_DAMAGE,
            # is_unique_effect=True,
            magnitude=0.1,  # Example: reduces physical damage by 10%
            duration=duration
        ))
        effects.append(AppliedEffect(
            effect_name=EffectType.FRAILTY.value,
            description="Reduces healing received.",
            target=StatType.HEALING_RECEIVED,
            # is_unique_effect=True,
            magnitude=0.1,  # Example: reduces healing received by 10%
            duration=duration
        ))

        return effects