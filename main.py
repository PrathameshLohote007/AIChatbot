from tkinter import *
from turtle import color
import pyttsx3 as pp
import speech_recognition as s
import chatbot as chat
import threading
import spacy
import tele
spacy.load("en_core_web_sm")

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)

def speak(words):
    engine.say(words)
    engine.runAndWait()

# Tkinter Dimension
main = Tk()
main.attributes('-alpha',0.95)
main.wm_iconbitmap("images\\science.ico")
main.geometry("800x600")

main.title("Welcome to Transport Help System")


img = PhotoImage(file="images\\bus.png")


photoL = Label(main, image=img)

#photoL.pack(pady=5)

photoL.place(x=0, y=0, relwidth=1, relheight=1)
# takey query : This code takes audio as input from user and convert it to string

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    #answer_from_bot = bot.get_response(query)
    answer_from_bot = chat.chatbot(query)
    #answer_from_bot = 'Akash'
    space_var = '                        '
    msgs.insert(END,"    You : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "    Support : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=135, height=10, yscrollcommand=sc.set,
fg='#ffffff',bg='#84ABFA',background='skyblue4')

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=0 , padx=0)

#frame.pack()

frame.place(x=-2, y=30)
# creating text field

textF = Entry(main, font=("Courier", 14))
#textF.pack(fill=None, pady=10)
textF.place(x = 150,y = 450,width=500,height=50)
#textF.config(width=30)

btn = Button(main, text="Ask Chatbot", font=(
    "Courier", 14),bg='red',fg='white', command=ask_from_bot)
#btn.pack()
btn.place(x=340,y=510)

# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()