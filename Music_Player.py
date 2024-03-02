from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()
root.title('Mp3 player')
mixer.init()
songs_list=Listbox(root, bg='black', fg='white', font='arial 15', height=12, width=47, 
selectmode=SINGLE, selectbackground='gray', selectforeground='black')
songs_list.grid(columnspan=6)

def play():
    song=songs_list.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def stop():
    mixer.music.stop()

def add():
    temp_song= filedialog.askopenfilenames(title="Choose a song", filetypes=(('mp3 Files', '*.mp3'),))
    for s in temp_song:
        songs_list.insert(END, s)

playbutton=Button(root,text='Play', font='arial', width=7, command=play)
playbutton.grid(row=1, column=0)

pausebutton=Button(root,text='Pause', font='arial', width=7, command=pause)
pausebutton.grid(row=1, column=1)

resumebutton=Button(root,text='Resume', font='arial', width=7, command=resume)
resumebutton.grid(row=1, column=2)

stopbutton=Button(root,text='Stop', font='arial', width=7, command=stop)
stopbutton.grid(row=1, column=3)

my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label='Select a Folder', menu=add_song_menu)
add_song_menu.add_command(label="Add Songs", command=add)
root.mainloop()