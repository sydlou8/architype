# prevents entity from using magical skills for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import MainEffects

class Mute(BaseEffect):
    name: str = Field(default=MainEffects.MUTE.value)
    description: str = Field(default="A negative effect that prevents the affected entity from using magical skills for a duration.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Mute effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=MainEffects.MUTE.value,
            description="Prevents the use of magical skills.",
            duration=duration
        ))

        return effects