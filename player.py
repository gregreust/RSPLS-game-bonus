#has a list of gestures
#has an active gesture
#has a counter for number of wins
from gesture import Gesture
from gesture import Rock
from gesture import Paper
from gesture import Scissors
from gesture import Lizard
from gesture import Spock

class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = [Rock('rock'), Paper('paper'), Scissors('scissors'), Lizard('lizard'), Spock('Spock')]
        self.active_gesture = self.gestures[0]
        self.win_counter = 0
