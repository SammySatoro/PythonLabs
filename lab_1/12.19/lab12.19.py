import _io

def lab12task19():

    def checkLines(inFile: _io.TextIOWrapper, dict: _io.TextIOWrapper):
        text = inFile.read().split()
        words = dict.read().split()
        for word in text:
            if word not in words:
                return False
        return True

    fileName = input('Enter file name: ')
    isFileOpened = False

    while not isFileOpened:
        try:
            inputFile = open(fileName, 'r')
            dict = open('words.txt', 'r')
            isFileOpened = True
            print('The text is correct.' if checkLines(inputFile, dict) else 'The text is incorrect.')
        except FileNotFoundError:
            print('Invalid directory or file name. Try again.')
            fileName = input('Enter file name: ')


if __name__ == '__main__':
    lab12task19()

