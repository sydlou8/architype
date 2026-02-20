# prevents entity from using physical skills for a duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects
class Root(BaseEffect):
    name: str = Field(default=StatusEffects.ROOT.value)
    description: str = Field(default="A negative effect that prevents the affected entity from using physical skills for a duration.")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Root effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=StatusEffects.ROOT.value,
            description="Prevents the use of physical skills.",
            duration=duration
        ))

        return effects