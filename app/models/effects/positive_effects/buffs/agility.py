from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, ModifierEffects
from models.enums.stat_types import StatType

class Agility(BaseEffect):
    name: str = Field(default=ModifierEffects.AGILITY.value)
    description: str = Field(default="A positive effect that increases dodge chance.")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Agility effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.AGILITY.value,
            description="Doubles dodge chance.",
            target=StatType.DODGE,
            stat_magnifier=self.BUFF_MULTIPLIER,
            duration=duration
        ))

        return effects