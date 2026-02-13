from functools import wraps
from typing import Callable, Any
from models.game.entities.base_entity import BaseEntity
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.effect_types import EffectType, ModifierEffects, StatusEffects, OverTimeEffects

EFFECT_HANDLERS = {}

def register_effect_handler(effect_type: EffectType) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        EFFECT_HANDLERS[effect_type.value] = func
        return wrapper
    return decorator

def get_effect_handler(effect_type: EffectType) -> Callable[..., Any]:
    handler = EFFECT_HANDLERS.get(effect_type.value)
    if handler is None:
        raise ValueError(f"No handler registered for effect type: {effect_type}")
    return handler

# ------------- REGISTER DIFFERENT EFFECTS AND THEIR FUNCTIONALITY --------------
# These are for effects with EXTRA functionality that can't be handled by the base effect system alone
# Example: Double Attack, Shield, etc

# Damage Logic Effects
@register_effect_handler(ModifierEffects.DOUBLE_ATTACK)
def handle_double_attack(entity: BaseEntity, effect: AppliedEffect, context: dict[str, Any]):
    """Handle the Double Attack effect - allows the entity to attack twice for their next turn."""
    # Consume the effect so it only triggers once
    for active in list(entity.active_effects):
        if active.effect_name == effect.effect_name:
            entity.active_effects.remove(active)
            break
    context["extra_attacks"] += 1
    context["extra_attack_multiplier"] = effect.stat_magnifier if effect.stat_magnifier is not None else 1.0  # Set the power multiplier


@register_effect_handler(StatusEffects.SHIELD)
def handle_shield(entity: BaseEntity, effect: AppliedEffect, context: dict[str, Any]):
    """Handle the Shield effect - blocks incoming damage for a certain duration."""
    # Consume the effect so it only triggers once
    for active in list(entity.active_effects):
        if active.effect_name == effect.effect_name:
            entity.active_effects.remove(active)
            break
    context["damage_blocked"] = True

@register_effect_handler(StatusEffects.ENDURE)
def handle_endure(entity: BaseEntity, effect: AppliedEffect, context: dict[str, Any]):
    """Handle the Endure effect - applies defender and fortify and blocks damage over time for a certain duration."""
    # Consume the effect so it only triggers once
    for active in list(entity.active_effects):
        if active.effect_name == effect.effect_name:
            entity.active_effects.remove(active)
            break
    context["block_dot"] = True

# Action Flow Effects
@register_effect_handler(StatusEffects.CONFUSION)
def handle_confusion(entity: BaseEntity, effect: AppliedEffect, context: dict[str, Any]):
    """Handle the Confusion effect - may cause the entity to hurt itself for a certain duration."""
    context["confused"] = True

@register_effect_handler(StatusEffects.STUN)
def handle_stun(entity: BaseEntity, effect: AppliedEffect, context: dict[str, Any]):
    """Handle the Stun effect - prevents the entity from taking any action for a certain duration."""
    context["skip_turn"] = True

@register_effect_handler(StatusEffects.SILENCE)
def handle_silence(entity: BaseEntity, effect: AppliedEffect, context: dict[str, Any]):
    """Handle the Silence effect - prevents the entity from using skills for a certain duration."""
    context["silenced"] = True

@register_effect_handler(StatusEffects.MUTE)
def handle_mute(entity: BaseEntity, effect: AppliedEffect, context: dict[str, Any]):
    """Handle the Mute effect - prevents the entity from using magical skills for a certain duration."""
    context["muted"] = True

@register_effect_handler(StatusEffects.ROOT)
def handle_root(entity: BaseEntity, effect: AppliedEffect, context: dict[str, Any]):
    """Handle the Root effect - prevents the entity from using physical skills for a certain duration."""
    context["rooted"] = True
