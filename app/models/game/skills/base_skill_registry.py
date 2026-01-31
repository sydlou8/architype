from abc import ABC
from typing import Generic, TypeVar
from enum import Enum

from models.game.skills.base_skill import BaseSkill

SkillEnum = TypeVar('SkillEnum', bound=Enum)

class BaseSkillRegistry(ABC, Generic[SkillEnum]):
    """
    Abstract base class for skill registries.
    
    This class provides a template for creating skill registries for different
    character classes or skill types. It defines methods for retrieving skills
    and listing all available skills.
    """

    REGISTRY: dict[SkillEnum, type[BaseSkill]] = {}

    @classmethod
    def get_skill(cls, skill_enum: SkillEnum) -> BaseSkill:
        """
        Factory method to create a skill instance from the registry.
        
        Args:
            skill_enum: The skill enum value
            
        Returns:
            An instance of the requested skill
            
        Raises:
            ValueError: If the skill is not found in the registry
        """
        skill_class = cls.REGISTRY.get(skill_enum)
        if skill_class is None:
            raise ValueError(f"Unknown skill: {skill_enum}")
    
        return skill_class()

    @classmethod
    def get_all_skills(cls) -> list[SkillEnum]:
        """
        Get a list of all available skills in the registry.
        
        Returns:
            List of all skill enum values in the registry
        """
        return list(cls._registry.keys())

    @classmethod
    def is_valid_skill(cls, skill_enum: SkillEnum) -> bool:
        """
        Check if a skill enum is valid (exists in the registry).
        
        Args:
            skill_enum: The skill enum value to check

        Returns:
            True if the skill is registered, False otherwise
        """
        return skill_enum in cls.REGISTRY