import tkinter
import sequence
import gc_content


def seq():
    sequence.run()


def gc():
    gc_content.run()


def start():
    window = tkinter.Tk()

    def close_window():
        window.destroy()

    window.columnconfigure([0, 1, 2], minsize=200)
    window.rowconfigure([0, 1, 2], minsize=100)

    frame1 = tkinter.Frame(master=window, width=10, height=10)
    frame1.grid(row=0, column=0)
    frame2 = tkinter.Frame(master=window, width=10, height=10)
    frame2.grid(row=0, column=1)
    frame3 = tkinter.Frame(master=window, width=10, height=10)
    frame3.grid(row=0, column=2)

    button = tkinter.Button(master=frame1, text="Sequence", command=seq)
    button2 = tkinter.Button(master=frame2, text="GC-%", command=gc)
    button3 = tkinter.Button(master=frame3, text="Quit", command=close_window)
    button.grid()
    button2.grid()
    button3.grid()
    window.mainloop()


if __name__ == '__main__':
    start()

# EOF
