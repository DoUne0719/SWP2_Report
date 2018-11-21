
class Controller:
    def __init__(self, model):
        self.model = model

    def guess(self, character):
        # change uppercase to lowercase
        character.lower()

        # User Input Error
        if len(character) == 0:
            return "Input one alphabet!"

        if not character.isalpha():
            return "Input only alphabet!"

        if character in self.model.getGuessedChars():
            return "Already use!"

        # append character to guessedChars
        if character not in self.model.getGuessedChars():
            self.model.guessedChars.append(character)

        # User Wrong
        if character not in self.model.getAnswer():
            self.model.increaseTries()
            self.model.decreaseLife()
            return False
        #User Right
        # Update currentStatus
        else:
            self.model.updateStatus(character)
            return True
