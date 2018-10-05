import os.path
import tkinter as tk
from functions import *
from tkinter.messagebox import showinfo
from tkinter import font as tkfont

# Initial creation
if os.path.exists('database.db') == False:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE data
                 (bikeid INTEGER PRIMARY KEY ,name text, phonenumber text, securitycode text, checkedin INTEGER, time TEXT)''')
    conn.commit()
    conn.close()
else:
    print('Database exists')

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
                               command=lambda:  controller.show_frame(page),
                               height=h, width=w)
            button.pack(pady=pad)

        button("Registreren", "Registreerpagina", 2, 20, 5)
        button("Inchecken", "Incheckpagina", 2, 20, 5)
        button("Uitchecken", "Uitcheckpagina", 2, 20, 5)
        button("Info", "Infopagina", 2, 20, 5)


class Registreerpagina(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def label(name):
            label = tk.Label(self, text=name, font=controller.title_font)
            label.pack(side="top", fill="x", pady=5)
        def labeltext(name):
            label = tk.Label(self, text=name)
            label.pack(side="top", fill="x")
        label("Registreer je account")

        labeltext("Naam")
        naam = tk.Entry(self)
        naam.pack(pady=5)
        labeltext("Telefoonnummer")
        tel = tk.Entry(self)
        tel.pack(pady=5)
        labeltext("Codewoord (Voorbeeld: koe)")
        word = tk.Entry(self)
        word.pack(pady=5)

        def clear_textbox():
            naam.delete(0, 9999)
            tel.delete(0, 9999)
            word.delete(0, 9999)

        def clicked(naam, tel, word):
            if len(naam) == 0 or len(tel) == 0 or len(word) == 0:
                bericht = 'Vul alle velden in!'
                showinfo(title='Warning', message=bericht)
            else:
                bikeid = bikeid_generator()
                labeltext("Het account is aangemaakt. Uw unieke code is " + bikeid)
                register(int(bikeid),naam,tel,word)
                clear_textbox()


        registreer = tk.Button(self, text="Registreren", command=lambda: clicked(naam.get(), tel.get(), word.get()), height=2, width=20)
        registreer.pack(pady=5)
        button = tk.Button(self, text="Ga terug",
                          command=lambda: [controller.show_frame("StartPagina"),clear_textbox()],
                             height=2, width=20)
        button.pack()


class Incheckpagina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def label(name):
            label = tk.Label(self, text=name, font=controller.title_font)
            label.pack(side="top", fill="x", pady=5)
        def labeltext(name):
            label = tk.Label(self, text=name)
            label.pack(side="top", fill="x")
        label("Check je fiets in")

        labeltext("Fiets nummer:")
        bikeid = tk.Entry(self)
        bikeid.pack(pady=5)

        def clear_textbox():
            bikeid.delete(0, 9999)
        def clicked(bikeid):
            if len(bikeid) == 0:
                bericht = 'Vul het veld in!'
                showinfo(title='Warning', message=bericht)
            elif verifybikeid(bikeid) == False:
                bericht = 'Fiets nummer klopt niet!'
                showinfo(title='Warning', message=bericht)
            elif verifyincheck(bikeid) == True:
                bericht = 'Fiets is al ingechecked!'
                showinfo(title='Warning', message=bericht)
            else:
                labeltext("De fiets is ingecheckt")
                fietscheckin(bikeid)
                clear_textbox()
        checkin = tk.Button(self, text="Check je fiets in", command=lambda: clicked(bikeid.get()), height=2, width=20)
        checkin.pack(pady=5)
        button = tk.Button(self, text="Ga terug",
                          command=lambda: [controller.show_frame("StartPagina"),clear_textbox()],
                             height=2, width=20)
        button.pack()

class Uitcheckpagina(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def label(name):
            label = tk.Label(self, text=name, font=controller.title_font)
            label.pack(side="top", fill="x", pady=5)
        def labeltext(name):
            label = tk.Label(self, text=name)
            label.pack(side="top", fill="x")
        label("Check je fiets uit")

        labeltext("Fiets nummer:")
        bikeid = tk.Entry(self)
        bikeid.pack(pady=5)
        labeltext("Security code:")
        code = tk.Entry(self)
        code.pack(pady=5)
        codecounter = 0
        def clear_textbox():
            bikeid.delete(0, 9999)
            code.delete(0, 9999)
        def clicked(bikeid, code):

            if len(bikeid) == 0:
                bericht = 'Vul het veld in!'
                showinfo(title='Warning', message=bericht)
            elif verifybikeid(bikeid) == False:
                bericht = 'Fiets nummer klopt niet!'
                showinfo(title='Warning', message=bericht)
            elif verifyincheck(bikeid) == False:
                bericht = 'Fiets is niet ingecheckt!'
                showinfo(title='Warning', message=bericht)
            elif not securitycode(bikeid, code):
                bericht = 'Dat was niet de goede code!'
                showinfo(title='Warning', message=bericht)
            else:
                labeltext("De fiets is uitgecheckt!")
                fietscheckout(bikeid)
                clear_textbox()

        checkin = tk.Button(self, text="Check je fiets uit", command=lambda: clicked(bikeid.get(), code.get(),
                                                                                     ), height=2, width=20)
        checkin.pack(pady=5)

        button = tk.Button(self, text="Ga terug",
                          command=lambda: [controller.show_frame("StartPagina"),clear_textbox()],
                             height=2, width=20)
        button.pack()

class Infopagina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def label(name):
            label = tk.Label(self, text=name, font=controller.title_font)
            label.pack(side="top", fill="x", pady=5)
        def labeltext(name):
            label = tk.Label(self, text=name)
            label.pack(side="top", fill="x")
        label("Info stalling")
        labeltext("Openingstijden:")
        labeltext("Maandag t/m Vrijdag 06:00 - 22:00")
        labeltext("Zaterdag en Zondag 10:00 - 20:00")
        label("Fiets info")
        labeltext("Fiets nummer:")
        bikeid = tk.Entry(self)
        bikeid.pack(pady=5)

        def clear_textbox():
            bikeid.delete(0, 9999)

        def clicked(bikeid):
            if len(bikeid) == 0:
                bericht = 'Vul het veld in!'
                showinfo(title='Warning', message=bericht)
            elif verifybikeid(bikeid) == False:
                bericht = 'Fiets nummer klopt niet!'
                showinfo(title='Warning', message=bericht)
            else:
                labeltext("Naam: " + fetchpersonalinfo(bikeid)[1])
                labeltext("Telefoon nummer: " + fetchpersonalinfo(bikeid)[2])
                if fetchpersonalinfo(bikeid)[4]:
                    labeltext("Ingecheckt: Ja")
                    labeltext("Datum en tijd incheck: " + fetchpersonalinfo(bikeid)[5])
                else:
                    labeltext("Ingecheckt: Nee")

                clear_textbox()
        checkin = tk.Button(self, text="Check je fiets info", command=lambda: clicked(bikeid.get()), height=2, width=20)
        checkin.pack(pady=5)
        button = tk.Button(self, text="Ga terug",
                          command=lambda: [controller.show_frame("StartPagina"),clear_textbox()],
                             height=2, width=20)
        button.pack()

if __name__ == "__main__":
    app = NSApp()
    app.title("NS App")
    app.geometry("500x400")
    app.mainloop()