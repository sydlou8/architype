# high single target enemy for physical damage, applies stun for 1 turn, causes bleed for 2 turns.
# reduces user's dodge and attack by 20% for 2 turns after use.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.jock_skills import JockSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.effects.negative_effects.status_effects.stun import Stun
from models.game.effects.negative_effects.status_effects.bleed import Bleed
from models.game.effects.negative_effects.debuffs.blind import Blind
from models.game.effects.negative_effects.debuffs.weaken import Weaken # physical attack debuff
from models.game.effects.applied_effect import AppliedEffect

class HighJumpKick(BaseSkill):
    name: str = Field(default=JockSkills.HIGH_JUMP_KICK.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="High single target enemy for physical damage, applies stun for 1 turn, causes bleed for 2 turns. Reduces user's dodge and attack by 20% for 2 turns after use.")
    cooldown: int = Field(default=5)
    power: int = Field(default=90)

    # ----------------------------------- CONSTANTS -----------------------------------
    STUN_DURATION: int = 1
    BLEED_DURATION: int = 2
    BLEED_TICK_DAMAGE: int = 5
    DEBUFF_DURATION: int = 2
    DODGE_DECREASE: float = 0.2  # 20%
    ATTACK_DECREASE: float = 0.2  # 20%

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the High Jump Kick skill on a target."""
        # Calculate damage
        damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)
        
        # Apply damage to target
        target.take_damage(damage)

        # Apply stun effect
        stun = Stun()
        stun_effects: list[AppliedEffect] = stun.generate_effects(duration=self.STUN_DURATION)
        for effect in stun_effects:
            target.add_effect(effect)

        # Apply bleed effect
        bleed = Bleed()
        bleed_effects: list[AppliedEffect] = bleed.generate_effects(
            duration=self.BLEED_DURATION,
            tick_value=self.BLEED_TICK_DAMAGE
        )
        for effect in bleed_effects:
            target.add_effect(effect)

        # Apply agility debuff to user (reduces dodge)
        blind = Blind(dodge_decrease=self.DODGE_DECREASE)
        blind_effects: list[AppliedEffect] = blind.generate_effects(duration=self.DEBUFF_DURATION)
        for effect in blind_effects:
            user.add_effect(effect)

        # Apply weaken debuff to user (reduces physical attack)
        weaken = Weaken(attack_decrease=self.ATTACK_DECREASE)
        weaken_effects: list[AppliedEffect] = weaken.generate_effects(duration=self.DEBUFF_DURATION)
        for effect in weaken_effects:
            user.add_effect(effect)
    
    def level_up(self) -> None:
        """Level up High Jump Kick - increases power."""
        self.level += 1
        self.power += 8