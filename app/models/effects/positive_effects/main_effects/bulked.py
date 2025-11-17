# applies strengthen and defender for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import MainEffects
from models.positive_effects.buffs.strengthen import Strengthen
from models.positive_effects.buffs.defender import Defender

class Bulked(BaseEffect):
    name: str = Field(default=MainEffects.BULKED.value)
    description: str = Field(default="A positive effect that increases physical damage and defense.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Bulked effect to the entity."""

        effects = []
        # Apply Strengthen effect
        strengthen_effects = Strengthen().generate_effects(duration=duration)
        effects.extend(strengthen_effects)

        # Apply Defender effect
        defender_effects = Defender().generate_effects(duration=duration)
        effects.extend(defender_effects)

        return effects