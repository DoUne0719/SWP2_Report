
import random

class Model:
    def __init__(self):
        self.answer = ""

        # read 'words.txt' file
        self.words = []
        f = open('words.txt', 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)

        self.guessedChars = []
        self.remainingLives = 6
        self.numTries = 0
        self.currentStatus = ''

    def randFromDB(self):
        r = random.randrange(self.count)
        self.answer = self.words[r]
        self.currentStatus = '_' * len(self.answer)
        return self.answer

    # reset for button pressed
    def restart(self):
        self.randFromDB()
        self.guessedChars = []
        self.remainingLives = 6
        self.numTries = 0

    # update currentStatus bar
    def updateStatus(self, inputchar):
        index = 0
        currentlist = list(self.currentStatus)

        for i in self.answer:
            if i == inputchar:
                currentlist[index] = inputchar
                index += 1
            else:
                index += 1

        self.currentStatus = ''.join(currentlist)

    # judge finish
    def finished(self):
        if self.currentStatus == self.answer:
            return True
        else:
            return False

    def decreaseLife(self):
        self.remainingLives -= 1

    def increaseTries(self):
        self.numTries += 1

    def getGuessedChars(self):
        return self.guessedChars

    # sort guessedChar & make lowercase
    def getGuessedCharsSort(self):
        self.guessedChars.sort()
        usedword = ', '.join(self.guessedChars)
        usedword.lower()
        return usedword

    def getTries(self):
        return self.numTries

    def getRemainingLives(self):
        return self.remainingLives

    def getAnswer(self):
        return self.answer

    def getStatus(self):
        return self.currentStatus
