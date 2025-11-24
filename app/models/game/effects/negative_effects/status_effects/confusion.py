# 50% chance to cause the affected entity to hurt itself for duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects

class Confusion(BaseEffect):
    name: str = Field(default=StatusEffects.CONFUSION.value)
    description: str = Field(default="A negative effect that has a 50% chance to cause the affected entity to hurt itself for duration.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Confusion effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=StatusEffects.CONFUSION.value,
            description="50% chance to hurt itself each turn.",
            tick_value=tick_value, # this is 10% of target's physical attack stat
            duration=duration
        ))

        return effects