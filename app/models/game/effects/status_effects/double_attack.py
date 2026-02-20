# allows targeted entity to attack twice for their next turn for a percentage of their original power.
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import EffectType, StatusEffects
from models.game.enums.stat_types import StatType

class DoubleAttack(BaseEffect):
    name: str = Field(default=StatusEffects.DOUBLE_ATTACK.value)
    description: str = Field(default="Allows the affected entity to attack twice for their next turn for a percentage of their original power.")

    # ----------------------------------- CONSTANTS -----------------------------------
    POWER_MULTIPLIER: float = 0.2  # 20% of original power

    def generate_effects(self, duration: int = 0, power_multiplier: float = None) -> list[AppliedEffect]:
        """Generate the Double Attack effect to the entity."""

        if power_multiplier is not None:
            self.POWER_MULTIPLIER = power_multiplier

        effects = []
        effects.append(AppliedEffect(
            effect_name=StatusEffects.DOUBLE_ATTACK.value,
            description=f"Allows the affected entity to attack twice for their next turn for {int(self.POWER_MULTIPLIER * 100)}% of their original power.",
            target=None,  # This effect doesn't target a specific stat
            stat_magnifier=self.POWER_MULTIPLIER,
            duration=duration
        ))

        return effects