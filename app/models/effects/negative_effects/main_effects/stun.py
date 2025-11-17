# skips the affected entity's next turn for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import MainEffects

class Stun(BaseEffect):
    name: str = Field(default=MainEffects.STUN.value)
    description: str = Field(default="A negative effect that skips the affected entity's next turn for a duration.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Stun effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=MainEffects.STUN.value,
            description="Skips the next turn.",
            duration=duration
        ))

        return effects