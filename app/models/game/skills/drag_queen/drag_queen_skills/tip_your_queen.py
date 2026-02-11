# heals 50% of damage dealt to target
# single target mixed physical and magic damage skill
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.drag_queen_skills import DragQueenSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.effects.applied_effect import AppliedEffect

class TipYourQueen(BaseSkill):
    name: str = Field(default=DragQueenSkills.TIP_YOUR_QUEEN.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Heals 50% of damage dealt to target.")
    cooldown: int = Field(default=4)
    power: int = Field(default=60)

    # ----------------------------------- CONSTANTS -----------------------------------
    HEALING_PERCENTAGE: float = 0.5  # Heal for 50

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Tip Your Queen skill on a target."""
        # Calculate damage (mixed physical and magic)
        physical_damage = self.calculate_base_damage(user, target, StatType.PHYSICAL_ATTACK, StatType.PHYSICAL_DEFENSE)
        magic_damage = self.calculate_base_damage(user, target, StatType.MAGICAL_ATTACK, StatType.MAGICAL_DEFENSE)
        total_damage = physical_damage + magic_damage
        
        # Apply damage to target
        target.take_damage(total_damage)

        # Calculate healing amount
        healing_amount = int(total_damage * self.HEALING_PERCENTAGE)

        # Apply healing to user
        user.heal(healing_amount)
        
    def level_up(self) -> None:
        """Level up Tip Your Queen - increases power."""
        self.level += 1
        self.power += 6