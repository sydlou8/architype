from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import EffectType, ModifierEffects
from models.game.enums.stat_types import StatType

class Fortify(BaseEffect):
    name: str = Field(default=ModifierEffects.FORTIFY.value)
    description: str = Field(default="A positive effect that increases magic defense.")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Fortify effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.FORTIFY.value,
            description="Doubles magical defense.",
            target=StatType.MAGICAL_DEFENSE,
            stat_magnifier=self.BUFF_MULTIPLIER,
            duration=duration
        ))

        return effects