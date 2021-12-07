from pigPlayer import PigPlayer


class HumanPlayer(PigPlayer):
    
    def wantsHandOver(self):
        '''Asks a human player if they want to play again'''
        print("\tYour current score: " + str(self.getCurrentScore()))
        print("\tRoll again? (yes or no)")
        ans = input()
        if ans == 'yes':
            return False
        if ans == 'no':
            return True
        
