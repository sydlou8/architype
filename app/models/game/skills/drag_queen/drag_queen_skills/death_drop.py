# deals massive damage to single target
# has a chance to OHKO  non-boss enemies
# if a boss is targeted, DeathDrop is 20% stronger against them
# damages user for 10% of their max HP
import random
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.drag_queen_skills import DragQueenSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType

class DeathDrop(BaseSkill):
    name: str = Field(default=DragQueenSkills.DEATH_DROP.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Deals massive damage to a single target. Has a chance to OHKO non-boss enemies. Damages user for 10% of their max HP.")
    cooldown: int = Field(default=5)
    power: int = Field(default=150)

    # ----------------------------------- CONSTANTS -----------------------------------
    OHKO_CHANCE: float = 0.15  # 15%
    SELF_DAMAGE_PERCENTAGE: float = 0.1  # 10%
    BOSS_DAMAGE_MULTIPLIER: float = 1.2  # 20% more damage to bosses

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Death Drop skill on a target."""
        # Check for OHKO chance
        if not target.is_boss and random.random() < self.OHKO_CHANCE:
            target.take_damage(target.current_hp)  # OHKO
        if target.is_boss:
            # Calculate damage with boss multiplier
            damage = int(self.calculate_base_damage(user, target, StatType.MAGIC_ATTACK, StatType.MAGIC_DEFENSE) * self.BOSS_DAMAGE_MULTIPLIER)
            target.take_damage(damage)
        else:
            # Calculate damage
            damage = self.calculate_base_damage(user, target, StatType.MAGIC_ATTACK, StatType.MAGIC_DEFENSE)
            target.take_damage(damage)

        # Damage the user for 10% of their max HP
        self_damage = int(user.max_hp * self.SELF_DAMAGE_PERCENTAGE)
        user.take_damage(self_damage)

    def level_up(self) -> None:
        """Level up Death Drop - increases power."""
        self.level += 1
        self.power += 15
