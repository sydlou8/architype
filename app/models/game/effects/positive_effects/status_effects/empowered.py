# applies strengthen and wisdom for a duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects
from models.game.buffs.strengthen import Strengthen
from models.game.buffs.wisdom import Wisdom

class Empowered(BaseEffect):
    name: str = Field(default=StatusEffects.EMPOWERED.value)
    description: str = Field(default="A positive effect that increases physical and magic damage.")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Empowered effect to the entity."""

        effects = []
        # Apply Strengthen effect
        strengthen_effects = Strengthen().generate_effects(duration=duration)
        effects.extend(strengthen_effects)

        # Apply Wisdom effect
        wisdom_effects = Wisdom().generate_effects(duration=duration)
        effects.extend(wisdom_effects)

        return effects

