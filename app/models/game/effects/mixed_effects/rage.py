from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects
from models.game.effects.positive_effects.buffs.strengthen import Strengthen
from models.game.effects.negative_effects.status_effects.confusion import Confusion
from models.game.effects.negative_effects.debuffs.weaken import Weaken
from models.game.effects.negative_effects.debuffs.frailty import Frailty


class Rage(BaseEffect):
    name: str = Field(default=StatusEffects.RAGE.value)
    description: str = Field(default="Applies confusion, weakness, and frailty. Also applies strengthen.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Generate the Rage effect to the entity."""
        
        effects = []
        
        # TODO: Apply confusion 
        # confusion_effects = Confusion().generate_effects(duration=duration)
        # effects.extend(confusion_effects)

        # Apply weakness, and frailty
        weakness_effects = Weaken().generate_effects(duration=duration)
        effects.extend(weakness_effects)

        frailty_effects = Frailty().generate_effects(duration=duration)
        effects.extend(frailty_effects)

        # Apply strengthen
        strengthen_effects = Strengthen().generate_effects(duration=duration)
        effects.extend(strengthen_effects)

        return effects