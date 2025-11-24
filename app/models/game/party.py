# Party model
# if a party of characters, all character classes should be unique
# if a party of enemies, enemies can be duplicated

from pydantic import BaseModel, Field
from app.models.game.character import Character

class Party(BaseModel):
    members: list[Character] = Field(default_factory=list)

    # ------------------------------- Constants -------------------------------
    MAX_PARTY_SIZE: int = 5

    # -------------------------------- Methods --------------------------------
    # Logic held in service layer, this is just a data model that holds party members
    def add_saved_party(self, default_members: list[Character]) -> None:
        """Add default members to the party."""
        if len(self.members) + len(default_members) > self.MAX_PARTY_SIZE:
            self.clear_party()
        self.members.extend(default_members)
    
    def add_member(self, character: Character) -> None:
        """Add a character to the party. """
        self.members.append(character)

    def edit_member(self, index: int, character: Character) -> None:
        """Edit a character in the party at the specified index."""
        if 0 <= index < len(self.members):
            self.members[index] = character
        else:
            raise IndexError("Member index out of range.")

    def move_member(self, old_index: int, new_index: int) -> None:
        """
        Move a character from old_index to new_index in the party.
        This allows reordering of party members.
        """
        if 0 <= old_index < len(self.members) and 0 <= new_index < len(self.members):
            member = self.members.pop(old_index)
            self.members.insert(new_index, member)
        else:
            raise IndexError("Member index out of range.")
    
    def swap_members(self, index1: int, index2: int) -> None:
        """Swap two characters in the party at the specified indices."""
        if 0 <= index1 < len(self.members) and 0 <= index2 < len(self.members):
            self.members[index1], self.members[index2] = self.members[index2], self.members[index1]
        else:
            raise IndexError("Member index out of range.")
            
    def clear_party(self) -> None:
        """Clear all members from the party."""
        self.members.clear()
        
    def remove_member(self, character: Character) -> None:
        """Remove a character from the party."""
        self.members.remove(character)

    def get_alive_members(self) -> list[Character]:
        """Get a list of alive members in the party."""
        return [member for member in self.members if member.is_alive]