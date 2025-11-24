from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.barista_skills import BaristaSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.effect_types import EffectType
from models.game.effects.positive_effects.status_effects.focus import Focus
from models.game.effects.positive_effects.buffs.strengthen import Strengthen
from models.game.effects.positive_effects.buffs.haste import Haste
from models.game.effects.positive_effects.buffs.agility import Agility

class TakeAShot(BaseSkill):
    name: str = Field(default=BaristaSkills.TAKE_A_SHOT.value)
    skill_type: str = Field(default=SkillType.SUPPORT.value)
    description: str = Field(default=" A buffing skill that applies focus, strengthen, haste, and agility the next turn.")

    EFFECT_DURATION: int = 1
    
    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Take a Shot skill on a target."""
        effects = []
        # Apply buffs to the target
        focus = Focus()
        strengthen = Strengthen()
        haste = Haste()
        agility = Agility()

        effects.extend(focus.generate_effects(duration=self.EFFECT_DURATION))
        effects.extend(strengthen.generate_effects(duration=self.EFFECT_DURATION))
        effects.extend(haste.generate_effects(duration=self.EFFECT_DURATION))
        effects.extend(agility.generate_effects(duration=self.EFFECT_DURATION))

        for effect in effects:
            target.add_effect(effect)