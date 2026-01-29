from abc import ABC, abstractmethod
from typing import Any, Callable, TYPE_CHECKING
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from functools import wraps
import random

from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.stat_types import StatType, register_stat, stats_registry
from models.game.effects.applied_over_time_effect import AppliedOverTimeEffect

if TYPE_CHECKING:
    from models.game.skills.base_skill import BaseSkill
    from models.game.effects.base_effect import Effect
    from models.game.abilities.base_ability import BaseAbility

class BaseEntity(SQLModel, ABC):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)

    # ----------------------- BASE STATS -----------------------
    # Basic attributes
    max_health: int = Field(default=100)
    current_health: int | None = None
    level: int = Field(default=1)
    is_alive: bool | None = None
    active_effects: list[AppliedEffect] = Field(default_factory=list)
    # ability: "BaseAbility | None" = None  # Disabled for now to avoid circular import

    # Combat stats
    physical_attack: int = Field(default=10)
    magical_attack: int = Field(default=10)
    physical_defense: int = Field(default=10)
    magical_defense: int = Field(default=10)
    speed: int = Field(default=10)

    # Combat modifiers
    dodge: float = Field(default=0.05)  # 5% dodge chance
    accuracy: float = Field(default=1)  # 100% accuracy
    critical_chance: float = Field(default=0.1)  # 10% critical hit chance
    healing_modifier: float = Field(default=1)  # Normal healing
    final_damage_modifier: float = Field(default=1)  # Overall damage modifier

    # Effect resist modifiers
    burn_resist: float = Field(default=0.2)
    poison_resist: float = Field(default=0.2)
    stun_resist: float = Field(default=0.2)
    curse_resist: float = Field(default=0.2)

    # Critical scaling constants
    BASE_CRITICAL_MULTIPLIER: float = 1.5  # Starting at level 1
    CRITICAL_MULTIPLIER_SCALING: float = 0.05  # Increase per level
    
    # Constant multipliers Not a field
    NORMAL_MULTIPLIER: float = 1.0  # 100% damage

    # ----------------------- DUNDER METHODS -----------------------
    def __init__(self, *args, **kwargs: Any):
        super().__init__(*args, **kwargs)
        if self.current_health is None:
            self.current_health = self.max_health
        self.is_alive = self.check_alive()

    # ----------------------- CURRENT STAT METHODS -----------------------
    # Note: current_health is a regular field, not a property, as it needs to be mutable
    
    @property
    @register_stat(StatType.PHYSICAL_ATTACK)
    def current_physical_attack(self) -> int:
        base = self.physical_attack
        multiplier = self.get_final_damage_multiplier(StatType.PHYSICAL_ATTACK)
        return int(base * multiplier)

    @property
    @register_stat(StatType.MAGICAL_ATTACK)
    def current_magical_attack(self) -> int:
        base = self.magical_attack
        multiplier = self.get_final_damage_multiplier(StatType.MAGICAL_ATTACK)
        return int(base * multiplier)

    @property
    @register_stat(StatType.PHYSICAL_DEFENSE)
    def current_physical_defense(self) -> int:
        base = self.physical_defense
        multiplier = self.get_final_damage_multiplier(StatType.PHYSICAL_DEFENSE)
        return int(base * multiplier)

    @property
    @register_stat(StatType.MAGICAL_DEFENSE)
    def current_magical_defense(self) -> int:
        base = self.magical_defense
        multiplier = self.get_final_damage_multiplier(StatType.MAGICAL_DEFENSE)
        return int(base * multiplier)

    @property
    @register_stat(StatType.SPEED)
    def current_speed(self) -> int:
        base = self.speed
        multiplier = self.get_final_damage_multiplier(StatType.SPEED)
        return int(base * multiplier)

    @property
    @register_stat(StatType.DODGE)
    def current_dodge(self) -> float:
        base = self.dodge
        multiplier = self.get_final_damage_multiplier(StatType.DODGE)
        return base * multiplier

    @property
    @register_stat(StatType.ACCURACY)
    def current_accuracy(self) -> float:
        base = self.accuracy
        multiplier = self.get_final_damage_multiplier(StatType.ACCURACY)
        return base * multiplier

    @property
    @register_stat(StatType.CRITICAL_CHANCE)
    def current_critical_chance(self) -> float:
        base = self.critical_chance
        multiplier = self.get_final_damage_multiplier(StatType.CRITICAL_CHANCE)
        return base * multiplier

    @property
    def current_critical_multiplier(self) -> float:
        """Calculate critical hit multiplier based on level.
        Scales from 1.5x at level 1 to 2.45x at level 20.
        Formula: 1.5 + (0.05 × (level - 1))
        """
        return self.BASE_CRITICAL_MULTIPLIER + (self.CRITICAL_MULTIPLIER_SCALING * (self.level - 1))

    @property
    @register_stat(StatType.HEALING_MODIFIER)
    def current_healing_modifier(self) -> float:
        base = self.healing_modifier
        multiplier = self.calculate_effect_multiplier(StatType.HEALING_MODIFIER, 1.0)
        return base * multiplier

    @property
    @register_stat(StatType.FINAL_DAMAGE_MODIFIER)
    def current_final_damage_modifier(self) -> float:
        base = self.final_damage_modifier
        # TODO: Add final damage modifier logic and apply any modifiers or effects that affect final damage
        multiplier = 1
        return base * multiplier

    # ----------------------- ABSTRACT METHODS -----------------------
    
    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        """Convert the entity to a dictionary representation."""
        pass

    @abstractmethod
    def from_dict(self, data: dict[str, Any]) -> 'BaseEntity':
        """Create an entity instance from a dictionary representation."""
        pass

    @abstractmethod
    def attack(self, skill: "BaseSkill", target: "BaseEntity") -> None:
        """Perform an attack on another entity."""
        # Implementation will vary based on entity type
        pass

    @abstractmethod
    def defend(self) -> None:
        """Defend against an incoming attack."""
        pass

    @abstractmethod
    def take_damage(self, amount: int) -> None:
        """Apply damage to the entity."""
        pass

    @abstractmethod
    def heal(self, amount: int) -> None:
        """Heal the entity."""
        pass

    # ----------------------- METHODS -----------------------
    def check_alive(self) -> bool:
        """Check if the entity is alive based on current health."""
        return self.current_health > 0

    # ----------------------- MULTIPLIERS -----------------------
    def get_critical_hit_multiplier(self) -> float:
        """Calculate the critical hit multiplier."""
        if random.random() < self.current_critical_chance:
            return self.CRITICAL_MULTIPLIER
        return self.NORMAL_MULTIPLIER
    
    def get_final_damage_multiplier(self, base_stat: StatType) -> float:
        """Calculate the final damage multiplier based on critical hits and effects."""
        multiplier = self.current_final_damage_modifier  # Property, not a function
        return self.calculate_effect_multiplier(base_stat, multiplier)
    
    def get_final_healing_multiplier(self) -> float:
        """Calculate the final healing multiplier based on effects."""
        multiplier = self.current_healing_modifier  # Property, not a function
        return self.calculate_effect_multiplier(StatType.HEALING_MODIFIER, multiplier)

    def calculate_effect_multiplier(self, base_stat: StatType, multiplier: float) -> float:
        """Calculate the effect multiplier for a specific stat, applying all matching effects."""
        for applied_effect in self.active_effects:
            if applied_effect.target == base_stat:
                # Apply the effect's stat magnifier
                multiplier *= applied_effect.stat_magnifier
        return multiplier

    # ----------------------- EFFECT METHODS -----------------------
    def add_effect(self, effect: AppliedEffect) -> None:
        """Add a status effect to the entity."""
        self.active_effects.append(effect)
    
    def apply_effects(self, effect: "Effect", duration: int) -> None:
        """Apply effects to the entity."""
        # Implementation for applying effects can be added here
        effects = effect.generate_effects(self)

    # Get total tick damage from active effects
    def get_total_tick_damage(self) -> int:
        """Calculate total damage/healing from over-time effects."""
        total_tick_damage = 0
        for effect in self.active_effects:
            # Check if it's an over-time effect with tick_value
            if isinstance(effect, AppliedOverTimeEffect) and effect.tick_value:
                total_tick_damage += effect.tick_value
        return total_tick_damage

    def apply_tick_damage(self) -> None:
        """Apply tick damage from active effects to the entity."""
        total_tick_damage = self.get_total_tick_damage()
        if total_tick_damage > 0:
            self.take_damage(total_tick_damage)
    
    def resolve_effects(self) -> None:
        """Resolve all active effects on the entity by decrementing duration and applying DoT/HoT."""
        # First, apply tick damage/healing from over-time effects
        self.apply_tick_damage()
        
        # Then decrement duration and remove expired effects
        for effect in list(self.active_effects):
            # Decrement duration
            if effect.duration and effect.duration > 0:
                effect.duration -= 1
            # Remove expired effects
            if effect.duration is not None and effect.duration <= 0:
                self.active_effects.remove(effect)

    