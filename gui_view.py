from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

class View(QWidget):
    def __init__(self, model, controller):
        super().__init__()

        self.model = model
        self.controller = controller
        self.maxTry = 6
        self.hangmantext = [

        '''\
           ____
          |    |
          |    o
          |   /|\\
          |    |
          |   / \\
         _|_
        |   |______
        |          |
        |__________|\
        \n****PRESS \"New Game\" BUTTON****
        ''',

        '''\
           ____
          |    |
          |    o
          |   /|\\
          |    |
          |   /
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |   /|\\
          |    |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |   /|
          |    |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |    |
          |    |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |
          |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |
          |
          |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',
        ]

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)


        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

    # when guessButton Clicked
    def guessClicked(self):
        self.character = self.charInput.text()
        self.message.setText(str(self.controller.guess(self.character)))
        self.guessedChars.setText(self.model.getGuessedCharsSort())
        if self.model.getRemainingLives() > 0:
            # if False -> draw hangman
            if self.message.text() == 'False':
                self.hangmanWindow.setPlaceholderText(self.hangmantext[self.maxTry - self.model.getTries()])
            else:
                self.currentWord.setText(self.model.getStatus())

            if self.model.finished():
                self.message.setText("Success!! PRESS \"New Game\" BUTTON")
        else:
            self.message.setText("Failed... [Answer is : " + self.model.getAnswer() + ']')
            self.hangmanWindow.setPlaceholderText(self.hangmantext[self.maxTry - self.model.getTries()])
            self.charInput.setEnabled(False)

        self.charInput.clear()

    # when New Game Button clicked
    def startGame(self):
        self.model.restart()
        self.message.clear()
        self.charInput.clear()
        self.message.clear()
        self.hangmanWindow.setPlaceholderText(self.hangmantext[self.maxTry - self.model.getTries()])
        self.currentWord.setText(self.model.getStatus())
        self.guessedChars.setText(self.model.getGuessedCharsSort())
        self.charInput.setEnabled(True)
