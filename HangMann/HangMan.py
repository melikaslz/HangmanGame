from tkinter import *
from tkinter import messagebox as msg
import random

easy=["apple","hello","act","air","blood"
,"blue","business","data","easy","eat","event","glass","pink","land","home"]
medium=["action","analysis","beautiful","building","camera","daughter","school","experience","history","lawyer","management","operation"]
hard=["agreement","campaign","community","democratic","economic","environmental","idenify","institution","knowledge","language","opportunity"]


alphabet=list('abcdefghijklmnopqrstuvwxyz')

btn=[]

Q=True
chosen=[]

def f(x):
    global btn
    global heart
    global alphabet
    global Q
    global chosen
    if alphabet[x] in answer:
        btn[x].config(bg='green')
        chosen.append(btn[x])
        yourGuess.config(bg="green")
        var3.set("your guess was right")
                
        for i in range(len(answer)):
            if alphabet[x]==answer[i]:                
                label[i]=alphabet[x]
                var.set(label)
                
    else:
        yourGuess.config(bg="red")
        Heart=Label(win,text="You have just       Chance")
        Heart.config(font=('helvetica',25),bg="#FC9A03")
        Heart.place(x=10,y=120)
        var3.set("your guess was wrong")
        btn[x].config(bg='red')
        heart-=1
        var4=StringVar()
        var4.set(heart)
        countHeart=Label(win,textvariable=var4)
        countHeart.config(font=('helvetica',25),bg="#FC9A03")
        countHeart.place(x=230,y=120)

    if answer==label:
        var2.set("you win")
        imgPath = "Win.png"
        photo = PhotoImage(file = imgPath)
        label1 = Label(image = photo)
        label1.image = photo
        label1.place(x=680,y=30)
        warning.config(bg="blue")
        Q=msg.askyesno('Hangman',"Do yo want to play again?")
        win.destroy()
    if heart==0:
        var2.set("you lost")
        var5=StringVar()
        lbl=Label(win,textvariable=var5)
        var5.set(" ".join(answer))
        lbl.config(bg="red",font=('helvetica',25))
        lbl.place(x=800,y=400)
        
        imgPath = "Lose.png"
        photo = PhotoImage(file = imgPath)
        label1 = Label(image = photo)
        label1.image = photo
        label1.place(x=680,y=30)
        warning.config(bg="blue")
        Q=msg.askyesno('Hangman',"Do yo want to play again?")
        win.destroy()
    
        
names=easy

def ChooseLevel(event):
    global n
    n=True
    global names
    cur=listbox.curselection()
    if cur==(0,):
        names=easy
    elif cur==(1,):
        names=medium
    else:
        names=hard
        
    x=random.randrange(0,len(names))
    answer=list(names[x])
    win.destroy()  

def keyboard():
    row=0
    col=0        
    for i in range(len(alphabet)):
        btn.append(alphabet[i])
        func=lambda x=i : f(x)
        btn[i]=Button(F,text=alphabet[i],command=func)
        btn[i].grid(row=row,column=col)
        btn[i].config(font=('helvetica',20))
        col+=1
        if col==9:
            col=0
            row+=1


while Q==True:
       
    win=Tk()
    win.geometry('1000x600')
    win.resizable(False,False)
    win.config(bg="#900C3F")

    levels=Label(win,text="Double click and Choose your level")
    levels.config(font=('helvetica',10))
    levels.place(x=24,y=400)
    listbox=Listbox(win)
    listbox.config(font=('helvetica',15))
    listbox.place(x=10,y=423)
    listbox.insert(0,'Easy')
    listbox.insert(1,'Medium')
    listbox.insert(2,'Hard')
    listbox.config(height=3,borderwidth=4)
    listbox.bind('<Double-Button>',ChooseLevel)

    F=Frame(win)
    F.config(bg='grey')
    F.config(bd=20)
    F.config(relief="groove")
    F.place(x=300 , y=380)

    var=StringVar()
    Input=Label(win,textvariable=var)
    Input.config(bg="gray")
    Input.place(x=300,y=280)
    Input.config(font=('helvetica',30))

    var2=StringVar()
    warning=Label(win,textvariable=var2)
    warning.place(x=10 , y=50)
    warning.config(bg="#900C3F",font=('helvetica',30))        
        
    var3=StringVar()
    yourGuess=Label(win,textvariable=var3)
    yourGuess.place(x=10 , y=200)
    yourGuess.config(font=('helvetica',30),bg='#900C3F')
        
    x=random.randrange(0,len(names))
        
    answer=list(names[x])
    print(answer)

    label=["_"]*len(answer)
    var.set(label)
    heart=len(answer)
    keyboard()

    win.mainloop() 
