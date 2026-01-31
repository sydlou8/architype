"""
Emo Skill Registr - Central registry for all Emo skills.

This registry allows for:
- Dynamic skill loading from database
- Player skill customization
- Easy addition of new skills
- Skill unlocking systems
"""

from models.game.enums.skills.emo_skills import EmoSkills
from models.game.skills.base_skill import BaseSkill
from models.game.skills.base_skill_registry import BaseSkillRegistry
from models.game.skills.emo.emo_skills.cloak import Cloak
from models.game.skills.emo.emo_skills.dagger_dance import DaggerDance
from models.game.skills.emo.emo_skills.guardian_spell import GuardianSpell
from models.game.skills.emo.emo_skills.how_poetic import HowPoetic
from models.game.skills.emo.emo_skills.ritual import Ritual
from models.game.skills.emo.emo_skills.shadow_strike import ShadowStrike
from models.game.skills.emo.emo_skills.soul_drain import SoulDrain

class EmoSkillRegistry(BaseSkillRegistry[EmoSkills]):
    # The registry: maps skill enums to skill classes
    REGISTRY: dict[EmoSkills, type[BaseSkill]] = {
        EmoSkills.CLOAK: Cloak,
        EmoSkills.DAGGER_DANCE: DaggerDance,
        EmoSkills.GUARDIAN_SPELL: GuardianSpell,
        EmoSkills.HOW_POETIC: HowPoetic,
        EmoSkills.RITUAL: Ritual,
        EmoSkills.SHADOW_STRIKE: ShadowStrike,
        EmoSkills.SOUL_DRAIN: SoulDrain,
    }