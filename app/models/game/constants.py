from models.game.party import Party

from models.game.entities.character.barista import Barista
from models.game.entities.character.biker import Biker
from models.game.entities.character.drag_queen import DragQueen
from models.game.entities.character.emo import Emo
from models.game.entities.character.jock import Jock

# Default Party for New Users --> Tutorial Purpose
# Player will start with these 5 characters and they can later customize their party.
# Players will keep these characters even after customizing their party.
TUTORIAL_PARTY = Party(
    members=[
        DragQueen(),
        Jock(),
        Biker(),
        Barista(),
        Emo()
    ]
)