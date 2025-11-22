# Party model
# if a party of characters, all character classes should be unique
# if a party of enemies, enemies can be duplicated


class Party(BaseModel):
    members: list[Character] = Field(default_factory=list)

    def add_member(self, character: Character) -> None:
        """Add a character to the party."""
        self.members.append(character)

    def remove_member(self, character: Character) -> None:
        """Remove a character from the party."""
        self.members.remove(character)

    def get_alive_members(self) -> list[Character]:
        """Get a list of alive members in the party."""
        return [member for member in self.members if member.is_alive]