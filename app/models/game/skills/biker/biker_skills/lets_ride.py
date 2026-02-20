# Applies invigorated to party for 3 turns.
# Hits target for 100% damage.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.biker_skills import BikerSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.status_effects import Invigorated
from models.game.effects.applied_effect import AppliedEffect

class LetsRide(BaseSkill):
    name: str = Field(default=BikerSkills.LETS_RIDE.value)
    skill_type: str = Field(default=SkillType.ATTACK.value)
    description: str = Field(default="Applies Invigorated to party for 3 turns and hits target for 100% damage.")
    cooldown: int = Field(default=4)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Let's Ride skill to apply Invigorated to the party and deal damage to the target."""
        invigorated = Invigorated()
        invigorated_effects: list[AppliedEffect] = invigorated.generate_effects(duration=3)  # Duration of 3 turns
        
        # Apply Invigorated to the entire party
        for target in targets:
            for effect in invigorated_effects:
                target.add_effect(effect)

        # Deal damage to the first target
        if targets:
            target = targets[0]
            damage = target.max_health * 1.0  # 100% of max health
            target.take_damage(damage)

    def level_up(self) -> None:
        """Level up Let's Ride - increases duration of effects and damage percentage."""
        self.level += 1
        new_duration = 3 + (self.level - 1) * 1
        new_damage_percentage = 1.0 + (self.level - 1) * 0.2
        Invigorated.DURATION = new_duration
        description = f"Applies Invigorated to party for {new_duration} turns and hits target for {new_damage_percentage:.0%} damage."
        self.description = description