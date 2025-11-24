# applies strengthen and fortify for a duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects
from models.game.positive_effects.buffs.fortify import Fortify
from models.game.positive_effects.buffs.wisdom import Wisdom

class Enchanted(BaseEffect):
    name: str = Field(default=StatusEffects.ENCHANTED.value)
    description: str = Field(default="A positive effect that increases magic damage and defense.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Enchanted effect to the entity."""

        effects = []
        # Apply Fortify effect
        fortify_effects = Fortify().generate_effects(duration=duration)
        effects.extend(fortify_effects)

        # Apply Wisdom effect
        wisdom_effects = Wisdom().generate_effects(duration=duration)
        effects.extend(wisdom_effects)

        return effects