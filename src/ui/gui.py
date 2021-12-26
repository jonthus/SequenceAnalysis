import tkinter as tk
import tkinter.filedialog
from PIL import Image
from PIL import ImageTk
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services import dotplot_service
from services import gc_service
from services import histogram_service
from services import validation_service
from pathlib import Path
PROJECT_ROOT = Path(__file__).parents[1]


class SequenceApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-zoomed', True)
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

    def dp(self, file):
        global img  # image gets garbage-collected if not global
        dotplot_service.dotplot_run(file)
        self.label1['text'] = "Dotplot on tulostettu tiedostoon 'dotplot.png'"
        img = Image.open(PROJECT_ROOT / "output_files" / "dotplot.png")
        img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.label2 = tk.Label(self, image=img)
        self.label2.pack(side="bottom", fill="both")

    def fdialog(self):
        file = tk.filedialog.askopenfilename()
        if validation_service.file_type(file) is False:
            self.dp_fails()
        if validation_service.is_fasta(file) is False:
            self.dp_fails()
        self.dp(file)

    def dp_fails(self):
        self.label1['text'] = "Vääränlainen tiedosto! Yritä uudestaan." \
                              "Esimerkkitiedostot löytyvät kansiosta src/input_files"


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
        content = gc_service.gc_run(file)
        self.label1['text'] = str(content)

    def fdialog(self):
        file = tk.filedialog.askopenfilename()
        if validation_service.file_type(file) is False:
            self.gc_fails()
        if validation_service.is_fasta(file) is False:
            self.gc_fails()
        self.gc(file)

    def gc_fails(self):
        self.label1['text'] = "Vääränlainen tiedosto! Yritä uudestaan." \
                              "Esimerkkitiedostot löytyvät kansiosta src/input_files"


class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Histogrammi").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Valitse tiedosto", command=self.fdialog).pack()
        self.label1 = tk.Label(self, text="")
        self.label1.pack()
        tk.Button(self, text="Palaa etusivulle",
                  command=lambda: master.switch_frame(StartPage)).pack()

    def histo(self, file):
        global imgtwo  # imgtwo gets garbage-collected if not global
        histogram_service.histogram_run(file)
        self.label1['text'] = "Histogrammi on tulostettu tiedostoon 'histogram.png'"
        imgtwo = Image.open(PROJECT_ROOT / "output_files" / "histogram.png")
        imgtwo.resize((250, 250), Image.ANTIALIAS)
        imgtwo = ImageTk.PhotoImage(imgtwo)
        self.label2 = tk.Label(self, image=imgtwo)
        self.label2.pack(side="bottom", fill="both")

    def fdialog(self):
        file = tk.filedialog.askopenfilename()
        if validation_service.file_type(file) is False:
            self.histo_fails()
        if validation_service.is_fasta(file) is False:
            self.histo_fails()
        self.histo(file)

    def histo_fails(self):
        self.label1['text'] = "Vääränlainen tiedosto! Yritä uudestaan. " \
                              "Esimerkkitiedostot löytyvät kansiosta src/input_files"


if __name__ == "__main__":
    app = SequenceApp()
    app.mainloop()