def lab12task10():
    import _io

    inputFileName = input("Enter name of the input file: ")
    outputFileName = input("Enter name of the output file: ")

    isFileOpened = False

    while not isFileOpened:
        try:
            with open(inputFileName, "r", encoding='utf-8') as inputFile:
                with open(outputFileName, "w", encoding='utf-8') as outputFile:
                    lines = inputFile.readlines()
                    for i in lines:
                        if i.replace(' ', '')[0] != '#':
                            outputFile.write(i)

                    isFileOpened = True

        except FileNotFoundError:
            print('Invalid directory or file name. Try again.')
            inputFileName = input("Enter name of the input file: ")
            outputFileName = input("Enter name of the output file: ")

    inputFile.close()
    outputFile.close()


# demo
if __name__ == "__main__":
    lab12task10()
