# applies concecrated and wisdom for a duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects
from models.game.positive_effects.buffs.consecrated import Consecrated
from models.game.positive_effects.buffs.wisdom import Wisdom

class Hidden(BaseEffect):
    name: str = Field(default=StatusEffects.HIDDEN.value)
    description: str = Field(default="A positive effect that increases agility immensely")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Blessed effect to the entity."""

        effects = []
        # Apply Agility
        agility = Agility()
        agility.stat_magnifier = 5.0
        agility_effects = agility.generate_effects(duration)
        effects.extend(agility_effects)

        return effects