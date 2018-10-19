import os
import tkinter as tk
from PIL import ImageTk, Image
from functions import *
from Captcha.captcha import captcha

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



    def __init__(self, parent, controller):  #initializes frame
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
    def __init__(self, parent, controller):                 #initializes frame and calls update model once
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def updatemodel(self):                              #update model allows to refresh the frame
            for widget in tk.Frame.winfo_children(self):    #destroys all widgets
                widget.destroy()

            # fucntions for widgets
            def label(name):                                  #creates a label in title letters with 'name' text
                label = tk.Label(self, text=name, font=controller.title_font)
                label.pack(side="top", fill="x", pady=5)
            def labeltext(name):                              #creates a label in small letters with 'name' text
                label = tk.Label(self, text=name)
                label.pack(side="top", fill="x")
            def popup(name):
                bericht = name
                showinfo(title='Message', message=bericht)    #showinfo generates a popup function
                                                              # made for cleanliness


            #create all widgets
            label("Registreer je account")
            labeltext("Naam")
            naam = tk.Entry(self)
            naam.pack(pady=5)
            labeltext("Telefoonnummer")
            tel = tk.Entry(self)
            tel.pack(pady=5)
            labeltext("Code woord (Voorbeeld: koe)")
            word = tk.Entry(self)
            word.pack(pady=5)
            labeltext("Captcha:")
            cptchkey, image = captcha()                             #generates captcha key and value
            img = ImageTk.PhotoImage(Image.open(image))             #creates picture value
            cptchkey = cptchkey
            panel = tk.Label(self, image=img)                       #inserts picture in label
            panel.image = img
            panel.pack()

            key = tk.Entry(self)
            key.pack(pady=5)

            # fucntion to dictate what happens when button is clicked
            def clicked(naam, tel, word, key):
                if len(naam) == 0 or len(tel) == 0 or len(word) == 0 or len(key) == 0:
                    popup("Vul alle velden in!")
                if not tel.isdigit():
                    popup("Het telefoonnummer moet bestaan uit nummers!")
                elif key.lower() != cptchkey:
                    popup("Captcha verkeerd ingevuld!")
                else:
                    bikeid = bikeid_generator()                 #generates a new id
                    popup("Het account is aangemaakt. Uw unieke code is " + bikeid)
                    register(int(bikeid),naam,tel,word)         #registers new person with the new id,
                                                                # codeword and phonenumber

            # command -button does this. lambda: -only when button is clicked.
            # calls both clicked(inserted name, inserted number, inserted codeword) and updatemodel() to
            # reload the page
            registreer = tk.Button(self, text="Registreren", command=lambda: [clicked(naam.get(), tel.get(), word.get(),
                                                                                      key.get()), updatemodel(self)],
                                                                                            height=2, width=20)
            registreer.pack(pady=5)
            button = tk.Button(self, text="Ga terug",
                              command=lambda: [controller.show_frame("StartPagina"),updatemodel(self)],
                                 height=2, width=20)
            button.pack()
        updatemodel(self)


class Incheckpagina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def updatemodel(self):
            for widget in tk.Frame.winfo_children(self):
                widget.destroy()
            def label(name):
                label = tk.Label(self, text=name, font=controller.title_font)
                label.pack(side="top", fill="x", pady=5)

            def labeltext(name):
                label = tk.Label(self, text=name)
                label.pack(side="top", fill="x")

            def popup(name):
                bericht = name
                showinfo(title='Message', message=bericht)

            label("Check je fiets in")
            labeltext("Fiets nummer:")
            bikeid = tk.Entry(self)
            bikeid.pack(pady=5)
            labeltext("Code woord:")
            securitycode = tk.Entry(self)
            securitycode.pack(pady=5)
            labeltext("Captcha:")
            cptchkey = ''

            cptchkey, image = captcha()
            img = ImageTk.PhotoImage(Image.open(image))
            print(cptchkey)

            panel = tk.Label(self, image=img)
            panel.image = img
            panel.pack(pady=5)

            key = tk.Entry(self)
            key.pack(pady=5)



            def clicked(bikeid, securitycode, key):
                if len(bikeid) == 0 or len(securitycode) == 0:
                    popup("Vul alle velden in!")
                elif verifybikeid(bikeid) == False:
                    popup("Fiets nummer klopt niet!")
                elif verifysecuritycode(bikeid, securitycode) == False:
                    popup("Code woord klopt niet!")
                elif verifyincheck(bikeid) == True:
                    popup("Fiets is al ingechecked!")
                elif key.lower() != cptchkey:
                    popup("Captcha verkeerd ingevuld!")
                else:
                    popup("De fiets is ingecheckt")
                    fietscheckin(bikeid)


            checkin = tk.Button(self, text="Check je fiets in",
                                command=lambda: [clicked(bikeid.get(), securitycode.get(), key.get()), updatemodel(self)], height=2,
                                width=20)
            checkin.pack(pady=5)
            button = tk.Button(self, text="Ga terug",
                               command=lambda: [controller.show_frame("StartPagina"), updatemodel(self)],
                               height=2, width=20)

            button.pack()

        updatemodel(self)


class Uitcheckpagina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def updatemodel(self):
            for widget in tk.Frame.winfo_children(self):
                widget.destroy()
            def label(name):
                label = tk.Label(self, text=name, font=controller.title_font)
                label.pack(side="top", fill="x", pady=5)
            def labeltext(name):
                label = tk.Label(self, text=name)
                label.pack(side="top", fill="x")
            def popup(name):
                bericht = name
                showinfo(title='Message', message=bericht)
            label("Check je fiets uit")

            labeltext("Fiets nummer:")
            bikeid = tk.Entry(self)
            bikeid.pack(pady=5)
            labeltext("Code woord:")
            securitycode = tk.Entry(self)
            securitycode.pack(pady=5)

            labeltext("Captcha:")
            cptchkey, image = captcha()
            img = ImageTk.PhotoImage(Image.open(image))
            cptchkey = cptchkey
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.pack()

            key = tk.Entry(self)
            key.pack(pady=5)

            def clicked(bikeid, securitycode, key):
                if len(bikeid) == 0 or len(securitycode) == 0:
                    popup("Vul alle velden in!")
                elif verifybikeid(bikeid) == False:
                    popup("Fiets nummer klopt niet!")
                elif verifysecuritycode(bikeid, securitycode) == False:
                    popup("Code woord klopt niet!")
                elif verifyincheck(bikeid) == False:
                    popup("Fiets is niet ingecheckt!")
                elif key.lower() != cptchkey:
                    popup("Captcha verkeerd ingevuld!")
                else:
                    popup("De fiets is uitgecheckt!")
                    fietscheckout(bikeid)
            checkin = tk.Button(self, text="Check je fiets uit", command=lambda: [clicked(bikeid.get(), securitycode.get(), key.get()), updatemodel(self)], height=2, width=20)
            checkin.pack(pady=5)
            button = tk.Button(self, text="Ga terug",
                              command=lambda: [controller.show_frame("StartPagina"),updatemodel(self)],
                                 height=2, width=20)
            button.pack()
        updatemodel(self)

class Infopagina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def updatemodel(self):
            for widget in tk.Frame.winfo_children(self):
                widget.destroy()
            def label(name):
                label = tk.Label(self, text=name, font=controller.title_font)
                label.pack(side="top", fill="x", pady=5)
            def labeltext(name):
                label = tk.Label(self, text=name)
                label.pack(side="top", fill="x")
            def popup(name):
                bericht = name
                showinfo(title='Message', message=bericht)
            label("Info stalling")
            labeltext("Openingstijden:")
            labeltext("Maandag t/m Vrijdag 06:00 - 22:00")
            labeltext("Zaterdag t/m Zondag 10:00 - 20:00")
            label("Fiets info")
            labeltext("Fiets nummer:")
            bikeid = tk.Entry(self)
            bikeid.pack(pady=5)
            labeltext("Code woord:")
            securitycode = tk.Entry(self)
            securitycode.pack(pady=5)

            labeltext("Captcha:")
            cptchkey, image = captcha()
            img = ImageTk.PhotoImage(Image.open(image))
            cptchkey = cptchkey
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.pack()

            key = tk.Entry(self)
            key.pack(pady=5)


            def clicked(bikeid, securitycode, key):
                if len(bikeid) == 0 or len(securitycode) == 0:
                    popup("Vul alle velden in!")
                elif verifybikeid(bikeid) == False:
                    popup("Fiets nummer klopt niet!")
                elif verifysecuritycode(bikeid, securitycode) == False:
                    popup("Code woord klopt niet!")
                elif key.lower() != cptchkey:
                    popup("Captcha verkeerd ingevuld!")
                    print(key + cptchkey)
                else:
                    if fetchpersonalinfo(bikeid)[4] == 1:
                        popup("Naam: " + fetchpersonalinfo(bikeid)[1] + "\n" + "Telefoon nummer: " + fetchpersonalinfo(bikeid)[2] + "\n" + "Ingecheckt: Ja" + "\n" + "Tijd en datum incheck: " + fetchpersonalinfo(bikeid)[5])
                    else:
                        popup("Naam: " + fetchpersonalinfo(bikeid)[1] + "\n" + "Telefoon nummer: " + fetchpersonalinfo(bikeid)[2] + "\n" + "Ingecheckt: Nee")

            checkin = tk.Button(self, text="Check je fiets info", command=lambda: [clicked(bikeid.get(), securitycode.get(), key.get()), updatemodel(self)], height=2, width=20)
            checkin.pack(pady=5)
            button = tk.Button(self, text="Ga terug",
                              command=lambda: [controller.show_frame("StartPagina"),updatemodel(self)],
                                 height=2, width=20)
            button.pack()
        updatemodel(self)

if __name__ == "__main__":
    app = NSApp()
    app.title("NS App")
    app.geometry("700x500")
    app.mainloop()