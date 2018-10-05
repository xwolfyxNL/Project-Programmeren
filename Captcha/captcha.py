from tkinter import *
from PIL import ImageTk, Image
import os
import string
from random import *
from claptcha import Claptcha


min_char = 4
max_char = 7
allchar = string.ascii_letters + string.digits
captchaWord = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

# Initialize Claptcha object with "Text" as text and FreeMono as font
c = Claptcha(captchaWord, "FreeMono.ttf")

# Get PIL Image object
text, image = c.image

print(text)         # 'Text'
print(type(image))  # <class 'PIL.Image.Image'>

# Get BytesIO object (note that it will represent a different image, just
# with the same text)
text, bytes = c.bytes

print(text)         # 'Text'
print(type(bytes))  # <class '_io.BytesIO'>

# Save a PNG file 'test.png'
text, file = c.write('test.png')

print(text)         # 'Text'
print(file)         # 'test.png'



root = Tk()
img = ImageTk.PhotoImage(Image.open("test.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
