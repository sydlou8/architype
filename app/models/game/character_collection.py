# This represents a collection of characters that a user may own in the game.
from sqlmodel import SqlModel, Field, Relationship
from typing import Any
from uuid import UUID, uuid4
from models.game.entities.character.character import Character

class CharacterCollection(SqlModel, table=True):
    """CharacterCollection model representing a collection of characters owned by a user."""
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id", nullable=False)
    characters: list[Character] = Relationship(back_populates="character_collection")
    
    def view_character_details_by_id(self, character_id: UUID) -> Character | None:
        """View specific character details by their ID."""
        for character in self.characters:
            if character.id == character_id:
                return character
        return None

    def add_character(self, character: Character) -> None:
        """Add a character to the collection."""
        self.characters.append(character)
    
    def edit_character(self, index: int, character: Character) -> None:
        """Edit a character in the collection at the specified index."""
        if 0 <= index < len(self.characters):
            self.characters[index] = character
        else:
            raise IndexError("Character index out of range.")

    def remove_character(self, character: Character) -> None:
        """Remove a character from the collection."""
        self.characters.remove(character)