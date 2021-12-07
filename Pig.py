#************************************************************
# *  Name  : Joshua Meharg
# * Pledge : I pledge my honor i have abided by the Stevens Honor System
#************************************************************

'''
4-Dice Pig, this time with classes!

Adapted from Java to Python by David Treder, 12/2020

---

For your final project, we are going to revisit the Pig game we programmed
for a previous lab. If you need a refresher for the rules for pig, just check
back on the previous lab. All the rules are the same for this assignment.

Also, this time the AI is not optional. Don’t worry though, we have provided
enough of a skeleton to lead you to the right solutions.

You may need to add additional functions to help get your code working. Feel
free to do that, just try to avoid renaming existing functions. That can
mess up our testing.

On a similar note, do not change the names of the files provided to you.
We may be testing individual classes which requires the name to be predictable.

Good luck!
'''

import HumanPlayer as hp
import ComputerPlayer as cp


class Pig:
    def __init__(self, isPlayer1Human = True, name1 = "Human 1", isPlayer2Human = False, name2 = "Computer 2"):
        if (isPlayer1Human):
            self.player1 = hp.HumanPlayer(self, name1)
        else:
            self.player1 = cp.ComputerPlayer(self, name1)

        if (isPlayer2Human):
            self.player2 = hp.HumanPlayer(self, name2)
        else:
            self.player2 = cp.ComputerPlayer(self, name2)

        self.currentPlayer = self.player1

        self.run()

    ################################## Make sure to put that back in
    
    def wantsPlayAgain(self):
        '''Once the game is over, asks the user if they want to play again'''
        ans = input("Want to play again? (yes or no): ")
        if ans == 'yes':
            return self.run()
        if ans == 'no':
            print('bye bye, ;)')
        else:
            print('Invalid input')
            return self.wantsPlayAgain()
            

    def displayHeader(self, player):
        print("----------")
        print(player.getName() + "\'s turn.")
        print("----------")
            
    def gameOver(self):
        '''return a boolean if the game is over'''
        if self.currentPlayer == self.player1:
            if (self.currentPlayer.lost()) or (self.currentPlayer.hasWon()):
                return True
            else:
                return False
        if self.currentPlayer == self.player2:
            if (self.currentPlayer.lost()) or (self.currentPlayer.hasWon()):
                return True
            else:
                return False

    def swapTurn(self):
        '''Once a player's turn is over, switches to the other players turn'''
        if self.currentPlayer == self.player1:
            if (not self.currentPlayer.isPlayerTurn):
                self.currentPlayer = self.player2
                self.currentPlayer.isPlayerTurn = True
        if self.currentPlayer == self.player2:
            if (not self.currentPlayer.isPlayerTurn):
                self.currentPlayer = self.player1
                self.currentPlayer.isPlayerTurn = True
               
            
            
        

    def playOnce(self):
        '''Plays one full game of Pig. Should also reset any required variables'''
        self.currentPlayer = self.player1
        self.currentPlayer.reset()
        self.currentPlayer = self.player2
        self.currentPlayer.reset()
    
        while (not self.gameOver()):
            if (not self.currentPlayer.isPlayerTurn):
                self.swapTurn()
            self.currentPlayer.doTurn()
        self.displayWinner()
        

    def run(self):
        self.playOnce()
        while(self.wantsPlayAgain()):
            self.playOnce()


    def __str__(self):
        '''The current score, or the name of the winner if game is over.'''

        if (self.gameOver()):
            if self.player2.lost():
                winner = self.player1.getName()
                return winner + " won!"
            if self.player1.lost():
                winner = self.player2.getName()
                return winner + " won!"
            if self.player1.hasWon():
                winner = self.player1.getName()
                return winner + " won!"
            if self.player2.hasWon():
                winner = self.player2.getName()
                return winner + " won!"
            #winner = self.player1.getName() if self.player2.lost() if self.player2.getName(
            #winner = self.player1.getName() if self.player1.hasWon() else self.player2.getName()
            #return winner + " won!"
        else:
            return "Game status: " + "\n\t" + str(self.player1) + "\n\t" + str(self.player2)


    

    def displayScores(self):
        print(self)

    def displayWinner(self):
        print("====================")
        self.displayScores()
        print("====================")

    

if __name__ == "__main__":
    '''Welcomes the user to the game, get the user's names and
        if each user is a human or not.
        Then creates a Pig object.'''
    
    p1h = input("Is player 1 human? (yes or no) ")
    if p1h == 'yes':
        p1Human = True
        p1Name = input("What is player 1's name? ")
    else:
        p1Human = False
        p1Name = 'Computer1'
    
    p2h = input("Is player 2 human? (yes or no) ")
    if p2h == 'yes':
        p2Human = True
        p2Name = input("What is player 2's name? " )
    else:
        p2Human = False
        p2Name = 'Computer2'
        


    Pig(p1Human, p1Name, p2Human, p2Name)
















        
