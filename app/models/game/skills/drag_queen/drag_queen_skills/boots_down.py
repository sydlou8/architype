# 50% chance to stun all targets for 2 turns.
# deals multi-target physical and magic damage
import random
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.drag_queen_skills import DragQueenSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.negative_effects.status_effects.stun import Stun
from models.game.effects.applied_effect import AppliedEffect

class BootsDown(BaseSkill):
    name: str = Field(default=DragQueenSkills.BOOTS_DOWN.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="50% chance to stun all targets for 2 turns. Deals multi-target physical and magic damage.")
    cooldown: int = Field(default=4)
    power: int = Field(default=60)

    # ----------------------------------- CONSTANTS -----------------------------------
    STUN_CHANCE: float = 0.5  # 50%
    STUN_DURATION: int = 2

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Boots Down skill on multiple targets."""
        for target in targets:
            # Calculate damage
            damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE) + \
                     self.calculate_base_damage(user, target, StatType.MAGICAL_ATTACK, StatType.MAGICAL_DEFENSE)   
           
            # Apply damage to target
            target.take_damage(damage)

            # Determine if stun is applied
            if random.random() < self.STUN_CHANCE:
                stun = Stun()
                stun_effects: list[AppliedEffect] = stun.generate_effects(duration=self.STUN_DURATION)
                for effect in stun_effects:
                    target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Boots Down - increases power."""
        self.level += 1
        self.power += 8
