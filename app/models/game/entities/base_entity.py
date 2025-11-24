from abc import ABC, abstractmethod
from typing import Any, Callable
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from functools import wraps

from models.game.skills.base_skill import BaseSkill
from models.game.effects.base_effect import Effect
from models.game.effects.applied_effect import AppliedEffect
from models.game.abilities.base_ability import BaseAbility
from models.game.enums.stat_types import StatType, register_stat, stats_registry 

class BaseEntity(SQLModel, ABC):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)

    # ----------------------- BASE STATS -----------------------
    # Basic attributes
    max_health: int = Field(default=100)
    current_health: int | None = None
    level: int = Field(default=1)
    is_alive: bool | None = None
    active_effects: list[AppliedEffect] = Field(default_factory=list)
    ability: BaseAbility | None = None

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

    # Constant multipliers Not a field
    NORMAL_MULTIPLIER: float = 1.0  # 100% damage
    CRITICAL_MULTIPLIER: float = 1.5  # 150% damage

    # ----------------------- DUNDER METHODS -----------------------
    def __init__(self, *args, **kwargs: Any):
        super().__init__(*args, **kwargs)
        if self.current_health is None:
            self.current_health = self.max_health
        self.is_alive = self.check_alive()

    # ----------------------- CURRENT STAT METHODS -----------------------
    
    @property
    @register_stat(StatType.HEALTH)
    def current_health(self) -> int:
        return self.max_health 

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
    @register_stat(StatType.HEALING_MODIFIER)
    def current_healing_modifier(self) -> float:
        base = self.healing_modifier
        # TODO: Add healing modifier logic and apply any modifiers or effects that affect healing
        multiplier = 1
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
    def attack(self, skill: BaseSkill, target: BaseEntity) -> None:
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
        import random
        if random.random() < self.current_critical_chance:
            return self.CRITICAL_MULTIPLIER
        return self.NORMAL_MULTIPLIER
    
    def get_final_damage_multiplier(self, base_stat: StatType) -> float:
        """Calculate the final damage multiplier based on critical hits and effects."""
        multiplier = self.current_final_damage_modifier()
        return self.calculate_effect_multiplier(self, base_stat, multiplier)
    
    def get_final_healing_multiplier(self) -> float:
        """Calculate the final healing multiplier based on effects."""
        multiplier = self.current_healing_modifier
        return self.calculate_effect_multiplier(self, base_stat, multiplier)

    def calculate_effect_multiplier(self, base_stat: StatType, multiplier: float) -> float:
        unique_effect_detected = False
        for applied_effect in self.active_effects:
            if applied_effect.stat_target == base_stat:
                if applied_effect.is_unique_effect and not unique_effect_detected:
                    multiplier *= applied_effect.get_damage_multiplier()
                    unique_effect_detected = True
        return multiplier

    # ----------------------- EFFECT METHODS -----------------------
    def add_effect(self, effect: AppliedEffect) -> None:
        """Add a status effect to the entity."""
        self.active_effects.append(effect)
    
    def apply_effects(self, effect: BaseEffect, duration: int) -> None:
        """Apply effects to the entity."""
        # Implementation for applying effects can be added here
        effects = effect.generate_effects(self)

    # Get total tick damage from active effects
    def get_total_tick_damage(self) -> int:
        total_tick_damage = 0
        for effect in self.active_effects:
            if effect.tick_magnitude:
                total_tick_damage += effect.tick_magnitude
        return total_tick_damage

    def apply_tick_damage(self) -> None:
        """Apply tick damage from active effects to the entity."""
        total_tick_damage = self.get_total_tick_damage()
        if total_tick_damage > 0:
            self.take_damage(total_tick_damage)
    
    def resolve_effects(self) -> None:
        """Resolve all active effects on the entity."""
        for effect in list(self.active_effects.values()):
            effect.resolve()
            if effect.duration <= 0:
                self.active_effects.remove(effect)

    