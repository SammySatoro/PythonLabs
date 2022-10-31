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
        import random

        dictionary = {
            'мама': ['mother'],
            'класс':['classroom', 'class', 'grade'],
            'кот': ['cat', 'kitty'],
            'птица': ['bird'],
            'улица': ['street', 'road', 'outside'],
            'дым': ['smoke'],
            'мяч': ['ball'],
            'зуб': ['tooth'],
            'часы': ['clock', 'watch', 'hours'],
            'число': ['number', 'few', 'count', 'amount', 'date'],
            'хотеть': ['want', 'wish', 'be willing'],
            'ручка': ['pen', 'handle', 'hand', 'arm', 'knob'],
            'вообще-то': ['actually', 'in fact', 'really'],
            'смотреть': ['watch', 'look', 'see', 'stare', 'gaze', 'view'],
            'клавиатура': ['keyboard'],
            'мышка': ['mouse'],
            'наушники': ['headphones', 'earphones', 'earbuds', 'headset'],
            'кофе': ['coffee'],
        }

        cur_ru_word = random.choice(list(dictionary.keys()))

        def guess():
            value = int(tries['text'][len(tries['text']) - 1])
            tries['text'] = f'Tries left: {value - 1}'
            if (value == 1):
                tries['text'] = 'You\'ve lost!'
                guessBtn['state'] = tkinter.DISABLED
            print(entryBox.get(), '   ', dictionary[ru_word['text']])
            if entryBox.get() in dictionary[ru_word['text']]:
                tries['text'] = 'You win!'
                guessBtn['state'] = tkinter.DISABLED

        def reset():
            cur_ru_word = random.choice(list(dictionary.keys()))
            tries['text'] = 'Tries left: 3'
            ru_word['text'] = cur_ru_word
            guessBtn['state'] = tkinter.ACTIVE
            ru_word['state'] = tkinter.ACTIVE

        def hint():
            ru_word['state'] = tkinter.DISABLED
            entryBox.delete(0, tkinter.END)
            entryBox.insert(0, random.choice(dictionary[ru_word['text']]))

        root = tkinter.Tk()
        root.resizable(width=False, height=False)
        root.geometry('210x150')
        root['background'] = '#856ff8'

        f_top = tkinter.Frame(root)
        f_bot = tkinter.Frame(root)
        f_top['background'] = '#856ff8'
        f_bot['background'] = '#856ff8'

        ru_word = tkinter.Button(f_top, command=hint, width=12, height=1, text=cur_ru_word, bg='#5B4CA9')
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

    def task5():
        from tkinter import ttk
        from tkinter import filedialog

        def calculate():
            try:
                radius = int(radius_entry.get())
                V = (4 / 3) * math.pi * radius ** 3
                res_entry.delete(0, tkinter.END)
                res_entry.insert(0, V)
            except ValueError:
                res_entry.delete(0, tkinter.END)
                res_entry.insert(0, 'ERROR')

        def save():
            filetypes = (
                ("TXT files", "*.txt"),
                ("HTML files", "*.html;*.htm"),
                ("All files", "*.*")
            )
            saving_format = select_list.current()
            print(saving_format)
            f = filedialog.asksaveasfile(initialdir="/", title="Select file", filetypes=[filetypes[saving_format]])
            if f is None:
                return
            res_to_save = res_entry.get()
            f.write(res_to_save)
            f.close()

        root = tkinter.Tk()
        root.geometry('280x220')
        root.resizable(width=False, height=False)
        root['background'] = '#856ff8'
        root.title('Sphere radius')
        root.resizable()

        f_top = tkinter.Frame(root, bg='#856ff8')
        f_mid = tkinter.Frame(root, bg='#856ff8')
        f_bot = tkinter.Frame(root, bg='#856ff8')

        radius_label = tkinter.Label(f_top, text='Set radius:', bg='#AFB4FF')
        radius_entry = tkinter.Entry(f_top)

        res_label = tkinter.Label(f_mid, text='Calculation result:', bg='#AFB4FF')
        res_entry = tkinter.Entry(f_mid)

        calc_btn = tkinter.Button(text='Calculate', command=calculate, bg='#AFB4FF')

        save_btn = tkinter.Button(f_bot, text='Save', command=save, bg='#AFB4FF', width=8)
        select_list = ttk.Combobox(f_bot, values=['.txt', '.html', '.*'], background='#AFB4FF', width=10)

        f_top.pack(pady=30)
        f_mid.pack(pady=0)
        calc_btn.pack(pady=20)
        f_bot.pack(pady=0)

        radius_label.pack(side=tkinter.LEFT, padx=30)
        radius_entry.pack(side=tkinter.LEFT)
        res_label.pack(side=tkinter.LEFT, padx=10)
        res_entry.pack(side=tkinter.LEFT)
        save_btn.pack(side=tkinter.LEFT, padx=30)
        select_list.pack(side=tkinter.LEFT)

        root.mainloop()


    task5()
