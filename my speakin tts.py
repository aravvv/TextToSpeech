from tkinter import *
from gtts import gTTS
#import tkinter.messagebox

def save_info():
    speaking_info = go_text.get()

    file = open("amazing.txt", "w")
    file.write(speaking_info)
    file.close()

def speak():
    
    text=""
    with open("amazing.txt", "r") as file:
        for line in file:
            text=text+line
        
    speech=gTTS(text,'en')

    speech.save("JUST CHILL.mp3")


window=Tk()
window.title("TEXT TO SPEECH CONVERTER BY ARAV")
window.configure(background='cyan')
#creating the labels

l0=Label(window, text="Whatever you want to convert into an audio file, Enter it in the box and then click on \n 1.'convert as a text file' \n 2. 'convert as an audio file' \n \n Once you have clicked on both, you will have your required audio in your folder !! \n ",bg="cyan",fg="red",height="7",font="33")
l0.grid(row=0,column=0)

l1=Label(window, text="Enter the text you want me to speak :", bg="cyan", fg="purple",width="30", height="1",font="40")
l1.grid(row=1,column=0)

l2=Label(window, text="", bg="cyan")
l2.grid(row=2,column=0)

l3=Label(window, text="", bg="cyan")
l3.grid(row=3,column=0)

l4=Label(window, text="", bg="cyan")
l4.grid(row=4,column=0)

l5=Label(window, text="", bg="cyan")
l5.grid(row=5,column=0)

l6=Label(window, text="", bg="cyan")
l6.grid(row=6,column=0)

l7=Label(window, text="Click on both the buttons below !! \n \n \n", bg="cyan", fg="purple",width="30", height="4",font="30")
l7.grid(row=7,column=1)

l8=Label(window, text="\n", bg="cyan")
l8.grid(row=9,column=0)

l9=Label(window, text="\n", bg="cyan")
l9.grid(row=11,column=0)

#creating entry boxes

go_text=StringVar()
e=Entry(window,textvariable=go_text, width="100")
e.grid(row=1,column=1)

#creating buttons

b1 = Button(window, text="convert as a text file", width="30", command=save_info,bg="pink",fg="black",height="4",font="30").grid(row=8,column=1)
b2 = Button(window, text="convert as an audio file", width="30", command=speak,bg="green",fg="black",height="4",font="30").grid(row=10,column=1)

window.mainloop()
