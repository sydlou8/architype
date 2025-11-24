# cause DOT and applies weaken and fatigue for a duration
from sqlmodel import Field
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import StatusEffects
from models.game.effects.negative_effects.debuffs.weaken import Weaken
from models.game.effects.negative_effects.debuffs.fatigue import Fatigue
from models.game.effects.over_time_effects.dot import DoT

class Curse(BaseEffect):
    name: str = Field(default=StatusEffects.CURSE.value)
    description: str = Field(default="A negative effect that causes damage over time and applies weaken and fatigue.")

    def generate_effects(self, duration: int = 0, tick_value: int = 0) -> list[AppliedEffect]:
        """Apply the Curse effect to the entity."""
        # Apply curse damage
        effects = []
        dot_effects = DoT().generate_effects(duration=duration, tick_value=tick_value)
        effects.extend(dot_effects)

        # Apply debuffs: weaken and fatigue
        weaken = Weaken()
        weaken.stat_magnifier = 0.9
        weaken_effects = weaken.generate_effects(duration=duration)
        effects.extend(weaken_effects)

        fatigue = Fatigue()
        fatigue.stat_magnifier = 0.9
        fatigue_effects = fatigue.generate_effects(duration=duration)
        effects.extend(fatigue_effects)

        return effects