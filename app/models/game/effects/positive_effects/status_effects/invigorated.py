#  applies haste and removes negative effects
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects
from models.game.positive_effects.buffs.haste import Haste

class Invigorated(BaseEffect):
    """Invigorated status effect that applies Haste and removes negative effects."""

    __tablename__ = "invigorated_effects"

    id: int | None = Field(default=None, primary_key=True)

    def apply(self, target) -> AppliedEffect:
        """Apply the Invigorated effect to the target.

        Args:
            target: The entity to which the effect is applied.

        Returns:
            An instance of AppliedEffect representing the applied effect.
        """
        # Apply Haste effect
        haste_effect = Haste()
        applied_haste = haste_effect.apply(target)

        # Remove negative effects from the target
        negative_effects = [effect for effect in target.active_effects if effect.type in StatusEffects.negative_effects()]
        for effect in negative_effects:
            target.remove_effect(effect)

        return AppliedEffect(
            effect=self,
            target=target,
            details=f"Applied Haste and removed {len(negative_effects)} negative effects."
        )