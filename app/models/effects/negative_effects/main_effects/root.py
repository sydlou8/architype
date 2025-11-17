# prevents entity from using physical skills for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import MainEffects
class Root(BaseEffect):
    name: str = Field(default=MainEffects.ROOT.value)
    description: str = Field(default="A negative effect that prevents the affected entity from using physical skills for a duration.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Root effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=MainEffects.ROOT.value,
            description="Prevents the use of physical skills.",
            duration=duration
        ))

        return effects