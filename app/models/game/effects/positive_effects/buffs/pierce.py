from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import EffectType, ModifierEffects
from models.game.enums.stat_types import StatType

class Pierce(BaseEffect):
    name: str = Field(default=ModifierEffects.PIERCE.value)
    description: str = Field(default="A positive effect that increases critical chance.")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Pierce effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.PIERCE.value,
            description="Doubles critical chance.",
            target=StatType.CRITICAL_CHANCE,
            stat_magnifier=self.BUFF_MULTIPLIER,
            duration=duration
        ))

        return effects