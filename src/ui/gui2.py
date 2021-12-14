import tkinter as tk
import tkinter.filedialog
from PIL import Image
from PIL import ImageTk
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sovellus import sequence
from sovellus import gc_content


class SequenceApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Valitse haluamasi toiminto").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Kahden sekvenssin vertailu",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Sekvenssin GC-%",
                  command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text="Sekvenssien pituuksien vertailu",
                  command=lambda: master.switch_frame(PageThree)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Kahden sekvenssin vertailu").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Valitse tiedosto", command=self.fdialog).pack()
        self.label1 = tk.Label(self, text="")
        self.label1.pack()
        tk.Button(self, text="Palaa etusivulle",
                  command=lambda: master.switch_frame(StartPage)).pack()

    def seq(self, file):
        global img # image gets garbage-collected if not global
        sequence.run(file)
        self.label1['text'] = "Dotplot on tulostettu tiedostoon 'sequence.png'"
        img = Image.open("sequence.png")
        img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.label2 = tk.Label(self, image=img)
        self.label2.pack(side="bottom", fill="both", expand="yes")

    def fdialog(self):
        file = tk.filedialog.askopenfilename()
        self.seq(file)


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="GC-% laskuri").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Valitse tiedosto", command=self.fdialog).pack()
        self.label1 = tk.Label(self, text="")
        self.label1.pack()
        tk.Button(self, text="Palaa etusivulle",
                  command=lambda: master.switch_frame(StartPage)).pack()

    def gc(self, file):
        content = gc_content.run(file)
        self.label1['text'] = str(content), str(" %")

    def fdialog(self):
        file = tk.filedialog.askopenfilename()
        self.label1['text'] = str(file)
        self.gc(file)


# TODO
class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Histogrammi").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Palaa etusivulle",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SequenceApp()
    app.mainloop()