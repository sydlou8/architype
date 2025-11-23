# applies concecrated and wisdom for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import StatusEffects
from models.positive_effects.buffs.consecrated import Consecrated
from models.positive_effects.buffs.wisdom import Wisdom

class Blessed(BaseEffect):
    name: str = Field(default=StatusEffects.BLESSED.value)
    description: str = Field(default="A positive effect that increases magic damage and healing.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Blessed effect to the entity."""

        effects = []
        # Apply Consecrated effect
        consecrated_effects = Consecrated().generate_effects(duration=duration)
        effects.extend(consecrated_effects)

        # Apply Wisdom effect
        wisdom_effects = Wisdom().generate_effects(duration=duration)
        effects.extend(wisdom_effects)

        return effects