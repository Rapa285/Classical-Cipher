class base:
    def __init__(self):
        self.mode = 1
        self.inputFile = ""
        self.inputText = ""
        self.algorithm = ""

    def changeMode(self):
        if self.mode == 1:
            self.mode = 0
        else:
            self.mode = 1

    def setmode(self, mode):
        self.mode = mode

    def setInputFile(self, inputFile):
        self.inputFile = inputFile

    def setInputText(self, inputText):
        self.inputText = inputText

    def encrypt(self):
        pass

    def decrypt(self):
        pass