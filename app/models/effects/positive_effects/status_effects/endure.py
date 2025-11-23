# applies defender and fortify and blocks DOT for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import StatusEffects
from models.positive_effects.buffs.defender import Defender
from models.positive_effects.buffs.fortify import Fortify

class Endure(BaseEffect):
    name: str = Field(default=StatusEffects.ENDURE.value)
    description: str = Field(default="A positive effect that increases physical defense and magic defense, and blocks damage over time effects.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Endure effect to the entity."""

        effects = []
        # Apply Defender effect
        defender_effects = Defender().generate_effects(duration=duration)
        effects.extend(defender_effects)

        # Apply Fortify effect
        fortify_effects = Fortify().generate_effects(duration=duration)
        effects.extend(fortify_effects)

        # TODO: Block Damage Over Time effects

        return effects