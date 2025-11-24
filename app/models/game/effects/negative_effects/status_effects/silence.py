# prevents entity from using all damaging skills including DoT skills for a duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects

class Silence(BaseEffect):
    name: str = Field(default=StatusEffects.SILENCE.value)
    description: str = Field(default="A negative effect that prevents the affected entity from using all skills for a duration.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Silence effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=StatusEffects.SILENCE.value,
            description="Prevents the use of all skills.",
            duration=duration
        ))

        return effects