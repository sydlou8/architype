from app.models.game.party import Party

from app.models.game.character.classes.barista import Barista
from app.models.game.character.classes.biker import Biker
from app.models.game.character.classes.drag_queen import DragQueen
from app.models.game.character.classes.emo import Emo
from app.models.game.character.classes.jock import Jock

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