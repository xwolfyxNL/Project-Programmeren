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

# GUI
class NSApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

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

        button1 = tk.Button(self, text="Registeren",
                            command=lambda: controller.show_frame("Registreerpagina"),
                           height=2, width=20)
        button2 = tk.Button(self, text="Inchecken",
                            command=lambda: controller.show_frame("Incheckpagina"),
                           height=2, width=20)
        button3 = tk.Button(self, text="Uitchecken",
                            command=lambda: controller.show_frame("Uitcheckpagina"),
                           height=2, width=20)
        button4 = tk.Button(self, text="Info",
                            command=lambda: controller.show_frame("Infopagina"),
                           height=2, width=20)
        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)
        button4.pack(pady=5)


class Registreerpagina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Registreer je account", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        inputfield = tk.Entry(self)
        inputfield.pack(pady=5)
        inputfield.insert(0, "Naam")
        inputfield2 = tk.Entry(self)
        inputfield2.pack(pady=5)
        inputfield2.insert(0, "Telefoon nummer")
        inputfield3 = tk.Entry(self)
        inputfield3.pack(pady=5)
        inputfield3.insert(0, "Code woord (Koe)")
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