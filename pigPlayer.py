from DiceQuad import DiceQuad


class PigPlayer:
    
    WINNING_SCORE = 100
    AUTO_WIN_RECOGNITION_ON = True
    numPlayers = 0

    
    
    def __init__(self, owner, name = "Player"):
        
        self.owner = owner
        self.name = name

        self.dice = DiceQuad()
        
        self.score = 0
        self.roundScore = 0

        self.isPlayerTurn = False
        PigPlayer.numPlayers += 1
        self.bad = False
    

    def reset(self):
        '''Resets all player values to their default value at the start of a game'''
        self.score = 0
        self.roundScore = 0
        self.isPlayerTurn = False
        self.bad = False

        
    def getName(self):
        '''Return the name of the player'''
        return self.name

    def getCurrentScore(self):
        '''Return the current score of the player. If it is currently the player's turn,
            include the round score'''
        if self.isPlayerTurn:
            return self.score + self.roundScore
        else:
            return self.score

    def hasWon(self):
        '''Return boolean if the player has won'''
        if self.getCurrentScore() >= self.WINNING_SCORE:
            return True
        else:
            return False

    def __str__(self):
        '''String representation of this class is the current total score, along with the
	 current round score (which could still be lost, in the case the turn is still
	 on), or the last round score, if it's the other player's turn'''
        
        return (self.name + "\'s score: \t" + str(self.getCurrentScore()) + "\t"+
    ("(this round so far: " if self.isPlayerTurn else " (last round's score: ")+ "\t" + str(self.roundScore) + ")")

    def displayNum1s(self):
        '''Prints a message about how many 1s were rolled. Also prints what happens as a consequence.
            EX:
                Player 1 rolled 3 ones
                Player 1 loses all points'''
        num1s = self.dice.num1s()
        
        print(self.name + " rolled " + str(num1s) + " ones")
    
        
        if(num1s == 1):
            print(self.name + "'s round ends and their round score is added to their total score")
            
            
        elif(num1s == 2):
            print(self.name + " loses all points for the round and their turn is over")
            
            
        elif(num1s == 3):
            print(self.name + " loses all their points in the game and their turn is over")
            
        elif(num1s == 4):
            print(self.name + " loses")
            
    
    def displayDice(self):
        print(self.dice)

    def displayDoRoll(self):
        self.owner.displayScores()
        print(self.name + " rolls... ")

    def doRoll(self):
        '''Rolls the dice for the player. Based on the number of 1s left, either asks the player if they want to roll again
            or ends the turn with the proper consequence. If AUTO_WIN_RECOGNITION_ON is True, ends the turn automatically when
            player has won including the most recent roll'''

        if (self.AUTO_WIN_RECOGNITION_ON):
            self.hasWon()
        

        self.displayDoRoll()
        self.dice.roll()
        self.displayDice()

        num1s = self.dice.num1s()

        self.roundScore += self.dice.getDiceTotal()

        if(num1s == 0):
            if (self.AUTO_WIN_RECOGNITION_ON):
                if (self.hasWon()):
                    self.isPlayerTurn = False
            else:
                self.isPlayerTurn = True
                

                
        elif(num1s == 1):
            self.isPlayerTurn = False
    

        elif(num1s == 2):
            self.roundScore = 0
            self.isPlayerTurn = False
            
            
        elif(num1s == 3):
            self.score = 0
            self.roundScore = 0
            self.isPlayerTurn = False
            
        elif(num1s == 4):
            self.score = 0
            self.roundScore = 0
            self.bad = True
            self.isPlayerTurn = False
            
            
    
    def doTurn(self):
        '''Performs a full turn for the player'''

        
        self.roundScore = 0
        self.isPlayerTurn = True

        while (self.isPlayerTurn):
            self.doRoll()
            
            if(self.isPlayerTurn):
                self.isPlayerTurn = not self.wantsHandOver()
                
        
        self.score += self.roundScore
        self.lost()

    def lost(self):
        if (self.bad):
            return True
        else:
            return False
        
        
                













            
