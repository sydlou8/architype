# causes infatuation for 3 turns, heals self for 20% of damage dealt
# single target magic damage skill
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.drag_queen_skills import DragQueenSkills
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType
from models.game.effects.status_effects.infatuation import Infatuation
from models.game.effects.applied_effect import AppliedEffect

class Fish(BaseSkill):
    name: str = Field(default=DragQueenSkills.FISH.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Causes infatuation for 3 turns, heals self for 20% of damage dealt.")
    cooldown: int = Field(default=4)
    power: int = Field(default=90)

    # ----------------------------------- CONSTANTS -----------------------------------
    INFATUATION_DURATION: int = 3
    HEAL_PERCENTAGE: float = 0.2  # 20%

    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the Fish skill on a target."""
        # Calculate damage
        damage = self.calculate_base_damage(user, target, StatType.MAGIC_ATTACK, StatType.MAGIC_DEFENSE)
        
        # Apply damage to target
        target.take_damage(damage)

        # Heal user for 20% of damage dealt
        heal_amount = int(damage * self.HEAL_PERCENTAGE)
        user.heal(heal_amount)

        # Apply infatuation effect to target
        infatuation = Infatuation()
        infatuation_effects: list[AppliedEffect] = infatuation.generate_effects(duration=self.INFATUATION_DURATION)
        for effect in infatuation_effects:
            target.add_effect(effect)

    def level_up(self) -> None:
        """Level up Fish - increases power."""
        self.level += 1
        self.power += 9