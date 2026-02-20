# Powerful attack that sacrifices defense for offense. 
# Attacks for 200% damage.
# Applies Susceptible and Vulnerable to self for 1 turn.
from sqlmodel import Field
from models.game.skills.base_skill import BaseSkill
from models.game.entities.base_entity import BaseEntity
from models.game.enums.skills.biker_skills import BikerSkills
from models.game.enums.skill_types import SkillType
from models.game.effects.status_effects.susceptible import Susceptible
from models.game.effects.status_effects.vulnerable import Vulnerable
from models.game.effects.applied_effect import AppliedEffect

class Wheelie(BaseSkill):
    name: str = Field(default=BikerSkills.WHEELIE.value)
    skill_type: str = Field(default=SkillType.OFFENSIVE.value)
    description: str = Field(default="Powerful attack that sacrifices defense for offense. Attacks for 200% damage. Applies Susceptible and Vulnerable to self for 1 turn.")
    cooldown: int = Field(default=5)

    def use(self, user: BaseEntity, targets: list[BaseEntity]) -> None:
        """Use the Wheelie skill to attack targets and apply Susceptible and Vulnerable to self."""
        # Attack logic for 200% damage would go here (not implemented in this snippet)

        # Apply Susceptible to self
        susceptible = Susceptible()
        susceptible_effects: list[AppliedEffect] = susceptible.generate_effects(duration=1)  # Duration of 1 turn
        for effect in susceptible_effects:
            user.add_effect(effect)

        # Apply Vulnerable to self
        vulnerable = Vulnerable()
        vulnerable_effects: list[AppliedEffect] = vulnerable.generate_effects(duration=1)  # Duration of 1 turn
        for effect in vulnerable_effects:
            user.add_effect(effect)
    
    def level_up(self) -> None:
        """Level up Wheelie - increases damage multiplier."""
        self.level += 1
        new_multiplier = 2.0 + (self.level - 1) * 0.5  # Increase damage multiplier by 0.5 per level up
        description = f"Powerful attack that sacrifices defense for offense. Attacks for {new_multiplier * 100}% damage. Applies Susceptible and Vulnerable to self for 1 turn."
        self.description = description