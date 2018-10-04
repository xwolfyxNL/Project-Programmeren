import os.path
import tkinter as tk
from functions import *
from tkinter import font as tkfont

# Initial creation
if os.path.exists('database.db') == False:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE data
                 (bikeid INTEGER PRIMARY KEY ,name text, phonenumber text, securitycode text, checkedin INTEGER, time TEXT)''')
    c.execute("INSERT INTO data VALUES (83242, 'Henk Piet', '12345678', 'koe', 0, '00:00:00 01-01-1990')")
    c.execute("INSERT INTO data VALUES (43536, 'Rita Henksla', '87654321', 'eok', 0, '00:00:00 01-01-1990')")
    conn.commit()
    conn.close()
else:
    print('Database exists')
def button(name):
    button = tk.Button(self, text=name,
                       command=lambda: controller.show_frame("StartPagina"),
                       height=2, width=20)
# GUI
class NSApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=10, weight="bold", slant="italic")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPagina, Registreerpagina, Incheckpagina, Uitcheckpagina, Infopagina):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPagina")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPagina(tk.Frame):



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="NS fietsen stalling", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        def button(name, page, h, w, pad):
            button = tk.Button(self, text=name,
                               command=lambda: controller.show_frame(page),
                               height=h, width=w)
            button.pack(pady=pad)

        button("Registreren", "Registreerpagina", 2, 20, 5)
        button("Inchecken", "Incheckpagina", 2, 20, 5)
        button("Uitchecken", "Uitcheckpagina", 2, 20, 5)
        button("Info", "Infopagina", 2, 20, 5)


class Registreerpagina(tk.Frame):
    s = StartPagina
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Registreer je account", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        def label(name):
            label = tk.Label(self, text=name, font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)

        datatable = []
        label("Naam")
        naam = tk.Entry(self)
        naam.pack(pady=5)
        label("Telefoonnummer")
        tel = tk.Entry(self)
        tel.pack(pady=5)
        label("Codewoord (Kak)")
        word = tk.Entry(self)
        word.pack(pady=5)

        def clicked(naam, tel, word):
            register(int(bikeid_generator()),naam,tel,word)

        registreer = tk.Button(self, text="Registreren", command=lambda: clicked(naam.get(), tel.get(), word.get()), height=2, width=20)
        registreer.pack()
        button = tk.Button(self, text="Ga terug",
                          command=lambda: controller.show_frame("StartPagina"),
                             height=2, width=20)
        button.pack()


class Incheckpagina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Check je fiets in", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Ga terug",
                           command=lambda: controller.show_frame("StartPagina"),
                           height=2, width=20)
        button.pack()

class Uitcheckpagina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Check je fiets uit", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Ga terug",
                           command=lambda: controller.show_frame("StartPagina"),
                           height=2, width=20)
        button.pack()

class Infopagina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Informatie NS fietsen stalling", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Ga terug",
                           command=lambda: controller.show_frame("StartPagina"),
                           height=2, width=20)
        button.pack()

if __name__ == "__main__":
    app = NSApp()
    app.title("NS App")
    app.geometry("500x400")
    app.mainloop()