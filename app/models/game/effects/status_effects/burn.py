from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects, ModifierEffects
from models.game.enums.stat_types import StatType
from models.game.effects.over_time_effects.dot import DoT

class Burn(BaseEffect):
    name: str = Field(default=StatusEffects.BURN.value)
    description: str = Field(default="A negative effect that causes damage over time and applies weaken and frailty.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Apply the Burn effect to the entity."""
        # Apply burn damage over time
        effects = []
        dot_effects = DoT().generate_effects(duration=duration, tick_value=tick_value)
        effects.extend(dot_effects)

        # Apply custom debuffs with 0.9 multiplier (10% reduction)
        # Weaken - reduces physical attack to 90%
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.WEAKEN.value,
            description="Reduces physical attack to 90%.",
            target=StatType.PHYSICAL_ATTACK,
            stat_magnifier=0.9,
            is_unique_effect=False,
            duration=duration
        ))

        # Frailty - reduces healing received to 90%
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.FRAILTY.value,
            description="Reduces healing received to 90%.",
            target=StatType.HEALING_MODIFIER,
            stat_magnifier=0.9,
            is_unique_effect=False,
            duration=duration
        ))

        return effects