#def choose_gesture
#user chooses from 5 options and updates active_gesture
from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        print('')
        print(f'{self.name}, select your move: ')
        for x in range(len(self.gestures)):
            print(f'{x} for {self.gestures[x].name}')
      
        try:                                                #preventing value error if user doesn't enter int
            choice = int(input())
            if choice < 0 or choice > 4:                    #prevent index error 
                print('')
                print('Please enter a number from 0 to 4')
                self.choose_gesture()
        except:
            print('')
            print('Error. Please enter a number from 0 to 4')
            self.choose_gesture()                           #try again
        
        self.active_gesture = self.gestures[choice]