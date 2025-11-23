# applies strengthen, wisdom, defender, fortify and haste for a duration; however, also applies frality and blind for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, StatusEffects, ModifierEffects
from models.enums.stat_types import StatType
from models.effects.positive_effects.buffs.strengthen import Strengthen
from models.effects.positive_effects.buffs.wisdom import Wisdom
from models.effects.positive_effects.buffs.defender import Defender
from models.effects.positive_effects.buffs.fortify import Fortify
from models.effects.positive_effects.buffs.haste import Haste
from models.effects.negative_effects.debuffs.frailty import Frailty
from models.effects.negative_effects.debuffs.blind import Blind

class Hyped(BaseEffect):
    name: str = Field(default=StatusEffects.HYPED.value)
    description: str = Field(default="A mixed effect that applies strengthen, wisdom, defender, fortify and haste, but also applies frailty and blind.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Apply the Rage effect to the entity."""
        effects = []

        # Apply buffs: strengthen, wisdom, defender, fortify, and haste
        strengthen_effects = Strengthen().generate_effects(duration=duration)
        effects.extend(strengthen_effects)

        wisdom_effects = Wisdom().generate_effects(duration=duration)
        effects.extend(wisdom_effects)

        defender_effects = Defender().generate_effects(duration=duration)
        effects.extend(defender_effects)

        fortify_effects = Fortify().generate_effects(duration=duration)
        effects.extend(fortify_effects)

        haste_effects = Haste().generate_effects(duration=duration)
        effects.extend(haste_effects)

       # Apply debuffs: frailty and blind
       frailty_effects = Frailty().generate_effects(duration=duration)
       effects.extend(frailty_effects)

       blind_effects = Blind().generate_effects(duration=duration)
       effects.extend(blind_effects)

        return effects