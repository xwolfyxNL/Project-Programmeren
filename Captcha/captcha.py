import string
from random import *

from claptcha import Claptcha

def captcha():
    min_char = 4
    max_char = 7
    allchar = string.ascii_letters + string.digits
    captchaWord = "".join(choice(allchar) for x in range(randint(min_char, max_char))).lower()

    # Initialize Claptcha object with "Text" as text and FreeMono as font
    c = Claptcha(captchaWord, "./Captcha/FreeMono.ttf")

    # Save a PNG file 'test.png'
    text, file = c.write('./cache/captcha.png')

    #print(text)         # 'Text'           thebugs are everywhere!
    #print(file)         # 'test.png'       debugging!

    return text, file

captcha()