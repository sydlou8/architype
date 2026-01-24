# skills can be chosen by user, abilities are randomized upon character creation

from abc import ABC, abstractmethod
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class BaseAbility(SQLModel, ABC):
    """Base class for character abilities"""
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    
    @abstractmethod
    def activate(self) -> None:
        """Activate the ability"""
        pass