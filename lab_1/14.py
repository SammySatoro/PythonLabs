def lab14():
    import tkinter

    def task1():

        def fahrToCels(fahr):
            return (fahr - 32) * (5 / 9)

        def click():
            resLabel.config(text=fahrToCels(int(entryBox.get())))

        root = tkinter.Tk()
        frame = tkinter.Frame(root).pack()
        root.resizable(width=False, height=False)
        tkinter.Label(text="Temperature in Fahrenheit", padx=5).pack(anchor='n')
        entryBox = tkinter.Entry(frame)
        entryBox.pack(anchor='n')
        resLabel = tkinter.Label(frame)
        resLabel.pack(anchor='n')
        tkinter.Button(frame, text='Print', command=click).pack(pady=5)
        tkinter.Button(frame, text='Quit', command=root.destroy).pack(pady=5)
        root.mainloop()

    def task2():
        import requests
        import re
        import random

        def getRuWord():
            response = requests.get('https://wooordhunt.ru/dic/content/en_ru')
            regex = r'\/dic\/list\/en_ru\/\w{1,2}'
            #print('Content:')
            matches = re.findall(regex, response.text)
            randomPage = 'https://wooordhunt.ru' + random.choice(matches)
            response = requests.get(randomPage)
            ru_regex = r'[А-Яа-я]+'
            #print(response.text)
            ru_matches = re.findall(ru_regex, response.text)
            return random.choice(ru_matches).lower()

        from translate import Translator


        def guess():
            value = int(tries['text'][len(tries['text']) - 1])
            tries['text'] = f'Tries left: {value - 1}'
            if (value == 1):
                tries['text'] = 'You\'ve lost!'
                guessBtn['state'] = tkinter.DISABLED

            translator = Translator(from_lang='ru', to_lang='en')
            ru_text = ru_word['text']
            en_text = translator.translate(ru_text).lower()
            if entryBox.get() == en_text:
                tries['text'] = 'You win!'
                guessBtn['state'] = tkinter.DISABLED
            return en_text

        def reset():
            tries['text'] = 'Tries left: 3'
            ru_word['text'] = getRuWord()
            guessBtn['state'] = tkinter.ACTIVE
            ru_word['state'] = tkinter.ACTIVE

        def hint():
            print(guess())
            ru_word['state'] = tkinter.DISABLED
            entryBox.delete(0, tkinter.END)
            entryBox.insert(0, guess())

        root = tkinter.Tk()
        root.resizable(width=False, height=False)
        root.geometry('210x150')
        root['background']='#856ff8'

        f_top = tkinter.Frame(root)
        f_bot = tkinter.Frame(root)
        f_top['background']='#856ff8'
        f_bot['background']='#856ff8'

        ru_word = tkinter.Button(f_top, command=hint, width=12, height=1, text=getRuWord(), bg='#5B4CA9')
        entryBox = tkinter.Entry(f_top, width=20, bg='#AFB4FF')

        guessBtn = tkinter.Button(f_bot, width=5, height=1, text='Guess', command=guess, bg='#5B4CA9')
        resetBtn = tkinter.Button(f_bot, width=5, height=1, text='Reset', command=reset, bg='#5B4CA9')
        tries = tkinter.Label(f_bot, width=10, height=1, text=f'Tries left: 3', bg='#5B4CA9')

        f_top.pack(pady=20)
        f_bot.pack(pady=10)
        ru_word.pack(padx=10, pady=5)
        entryBox.pack(padx=10, pady=5)
        guessBtn.pack(side=tkinter.LEFT, padx=10)
        resetBtn.pack(side=tkinter.LEFT, padx=10)
        tries.pack(side=tkinter.LEFT, padx=10)

        root.mainloop()

    task2()
# demo
if __name__ == "__main__":
    lab14()
