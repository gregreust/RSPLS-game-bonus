class Gesture:
    def __init__(self, name, wins1, wins2, loses1, loses2) -> None:
        self.name = name
        self.wins_against = [wins1, wins2]
        self.loses_to = [loses1, loses2]

    def does_it_win(self, opponent_gesture, player_1, player_2):
        print('')
        if opponent_gesture.name in self.wins_against:
            print(f'{player_1.name} wins')
            player_1.win_counter += 1
        elif opponent_gesture.name in self.loses_to:   
            print(f'{player_2.name} wins')
            player_2.win_counter += 1
        else:
            print('This one was a tie.')

class Rock(Gesture):
    def __init__(self, name):
        super().__init__(name, 'scissors', 'lizard', 'paper', 'Spock')

class Paper(Gesture):
    def __init__(self, name):
        super().__init__(name, 'rock', 'Spock', 'scissors', 'lizard')

class Scissors(Gesture):
    def __init__(self, name):
        super().__init__(name, 'paper', 'lizard', 'rock', 'Spock')

class Lizard(Gesture):
    def __init__(self, name):
        super().__init__(name, 'paper', 'Spock', 'rock', 'scissors')

class Spock(Gesture):
    def __init__(self, name):
        super().__init__(name, 'rock', 'scissors', 'paper', 'lizard')