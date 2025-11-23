from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, ModifierEffects
from models.enums.stat_types import StatType

class Defender(BaseEffect):
    name: str = Field(default=ModifierEffects.DEFENDER.value)
    description: str = Field(default="A positive effect that increases physical defense.")

    def generate_effects(self, duration: int = 0) -> list[AppliedEffect]:
        """Generate the Defender effect to the entity."""

        effects = []
        effects.append(AppliedEffect(
            effect_name=ModifierEffects.DEFENDER.value,
            description="Doubles physical defense.",
            target=StatType.PHYSICAL_DEFENSE,
            stat_magnifier=self.BUFF_MULTIPLIER,
            duration=duration
        ))

        return effects