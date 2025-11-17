# applies strengthen, haste, and pierce for a duration; however, also applies vulnerable and susceptible for a duration
from sqlmodel import Field
from models.effects.base_effect import BaseEffect
from models.effects.applied_effect import AppliedEffect
from models.enums.effect_types import EffectType, MainEffects, SideEffects
from models.effects.positive_effects.buffs.haste import Haste
from models.effects.positive_effects.buffs.pierce import Pierce
from models.effects.positive_effects.buffs.strengthen import Strengthen
from models.effects.negative_effects.debuffs.susceptible import Susceptible
from models.effects.negative_effects.debuffs.vulnerable import Vulnerable

class Berserk(BaseEffect):
    name: str = Field(default=MainEffects.BERSERK.value)
    description: str = Field(default="A mixed effect that applies strengthen, haste, and pierce for a duration; however, also applies vulnerable and susceptible for a duration.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Berserk effect to the entity."""
        effects = []
        # Apply positive effects
        # Apply Strengthen effect
        strengthen_effects = Strengthen().generate_effects(duration=duration)
        effects.extend(strengthen_effects)

        # Apply Haste effect
        haste_effects = Haste().generate_effects(duration=duration)
        effects.extend(haste_effects)

        # Apply Pierce effect
        pierce_effects = Pierce().generate_effects(duration=duration)
        effects.extend(pierce_effects)

        # Apply negative effects
        # Apply Vulnerable effect
        vulnerable_effects = Vulnerable().generate_effects(duration=duration)
        effects.extend(vulnerable_effects)

        # Apply Susceptible effect
        susceptible_effects = Susceptible().generate_effects(duration=duration)
        effects.extend(susceptible_effects)
        
        return effects