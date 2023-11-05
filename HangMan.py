# Importing Dependancies
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


window = Tk()
window.title('Hangman-GUESS The City')

cities= ['AGRA', 'ITANAGAR', 'DHANBAD', 'INDORE', 'RAIPUR', 'DELHI', 'SURAT', 'VISAKHAPATNAM', 'RAJKOT', 'PRAYAGRAJ', 
            'JAIPUR', 'PATNA', 'SRINAGAR', 'AHMEDABAD', 'RANCHI', 'CHENNAI', 'HYDERABAD', 'BHOPAL', 'GANGTOK', 'KOCHI', 
            'FARIDABAD', 'KOLKATA', 'DISPUR', 'KANPUR', 'LUCKNOW', 'SHILLONG', 'BENGALURU', 'THANE', 'JHANSI', 'MEERUT', 
            'VARANASI', 'PUNE', 'AMRITSAR', 'GHAZIABAD', 'IMPHAL', 'PURI', 'AIZAWL', 'NAGPUR', 'KOHIMA', 'KOTA', 'AGARTALA', 'MUMBAI']

pictures=[PhotoImage(file="images/hangman0.png"), PhotoImage(file="images/hangman1.png"), PhotoImage(file="images/hangman2.png"),
        PhotoImage(file="images/hangman3.png"), PhotoImage(file="images/hangman4.png"), PhotoImage(file="images/hangman5.png"),
        PhotoImage(file="images/hangman6.png"), PhotoImage(file="images/hangman7.png"), PhotoImage(file="images/hangman8.png"),
        PhotoImage(file="images/hangman9.png"), PhotoImage(file="images/hangman10.png"), PhotoImage(file="images/hangman11.png")]

def newGame():  # starts a new game
    global word_with_space
    global Guess_No
    Guess_No = 0
    imgLabel.config(image=pictures[0])
    the_word=random.choice(cities)
    word_with_space = " ".join(the_word)
    lblWord.set(' '.join("_"*len(the_word)))

def guess(letter):
    global Guess_No
    if Guess_No<11:	
        txt = list(word_with_space)
        guessed = list(lblWord.get())
        if word_with_space.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==word_with_space:
                    messagebox.showinfo("Hangman","Great !!! You guessed it!")
                    break
        else:
            Guess_No += 1
            imgLabel.config(image=pictures[Guess_No])
            if Guess_No==11:
                messagebox.showwarning("Hangman","Game Over \n\n\n The City was  "+str(word_with_space))

imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)


lblWord = StringVar()
Label(window, textvariable  =lblWord,font=('consolas 22 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=('Helvetica 19'), width=4).grid(row=1+n//9,column=n%9)
    n+=1

Button(window, text="New\nGame", command=lambda:newGame(), font=("Helvetica 11 bold")).grid(row=3, column=8)

newGame()
window.mainloop()