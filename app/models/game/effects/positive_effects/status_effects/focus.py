# applies concentration and pierce for a duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects
from models.game.effects.positive_effects.buffs.concentration import Concentration
from models.game.effects.positive_effects.buffs.pierce import Pierce

class Focus(BaseEffect):
    name: str = Field(default=StatusEffects.FOCUS.value)
    description: str = Field(default="A positive effect that applies concentration and pierce.")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Focus effect to the entity."""

        effects = []
        # Apply Concentration effect
        concentration_effects = Concentration().generate_effects(duration=duration)
        effects.extend(concentration_effects)

        # Apply Pierce effect
        pierce_effects = Pierce().generate_effects(duration=duration)
        effects.extend(pierce_effects)

        return effects