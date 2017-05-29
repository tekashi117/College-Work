
import Tkinter
import time
import random
class ButtonMasher():
    def __init__(self):
        #creating the main window for the button masher game
        self.f=('Courier New', 30)
        self.fb=('Courier New', 25,'bold')
        self.win=Tk()
        self.win.geometry("800x250")
        self.win.title("Button Masher")
        self.Objective=Label(self.win, text="Press the button rapidly for 10sec", font=self.fb)
        self.Objective.pack()
        self.MainB=Button(self.win, text="Hit", font=self.f, width=4, height=2, justify='center', anchor='center')
        self.MainB.pack()
        self.PostGame=Frame(self.win)
        self.qb=Button(self.PostGame, text="Quit", font=self.f, command=self.end)
        self.playb=Button(self.PostGame, text='Start', font=self.f, command=self.start)
        self.qb.pack(side='left')
        self.playb.pack(side='left')
        self.PostGame.pack()
        self.win.mainloop()

    #Function to allow user to click button for 10 seconds
    def start(self):
        self.MainB.config(text="Hit", command=self.countUP,state='active')
        self.win.after(10000,self.stop)
        self.c=0
    def countUP(self):
        self.c+=1

    #disable the button, show score
    def stop(self):
        self.MainB.config(text=self.c, state='disabled')
        self.playb.config(text="Play again?")

    #This code is used to open the mode screen
    def end(self):
        self.win.destroy()
        self.new=ButtonMode()


#Hit the button for 10-12 seconds, until button stays stop
class ButtonControl():
    def __init__(self):
        self.f=('Courier New', 30)
        self.fb=('Courier New', 25,'bold')
        self.win=Tk()
        self.win.geometry("800x250")
        self.win.title("Button Control")
        self.Objective=Label(self.win, text="Be careful when Mashing!", font=self.fb)
        self.Objective.pack()
        self.MainB=Button(self.win, text="Hit!", font=self.f, width=4, height=2, justify='center', anchor='center')
        self.MainB.pack()
        self.PostGame=Frame(self.win)
        self.qb=Button(self.PostGame, text="Quit", font=self.f, command=self.end)
        self.playb=Button(self.PostGame, text='Start', font=self.f, command=self.start)
        self.qb.pack(side='left')
        self.playb.pack(side='left')
        self.PostGame.pack()
        self.win.mainloop()
    def start(self):
        self.MainB.config(text="Hit!", command=self.countUP,state='active')
        self.c=0
        self.win.after(random.randint(10000, 12000),self.Lower)
    def countUP(self):
        self.c+=1
    def stop(self):
        self.MainB.config(text=self.c, state='disabled')
        self.playb.config(text="Play again?")
    #Change the button to decrease, and change text
    def Lower(self):
        self.MainB.config(text="Stop", command=self.decrease)
        self.win.after(6000, self.stop)
    def decrease(self):
        self.c-=7
    def end(self):
        self.win.destroy()
        self.new=ButtonMode()

#use a stopwatch function to test user on sense of time
#goal is to hit button exactly after 10 seconds
class ButtonAccuracy():
    def __init__(self):
        self.win=Tk()
        self.f=("Courier New", 30)
        self.fb=("Courier New", 30,"bold")
        self.win.geometry("800x250")
        self.win.title("Button Accuracy")
        self.Objective=Label(self.win, text="Hit the button in exactly 10 secs!", font=self.fb)
        self.MainB=Button(self.win, text="Hit", font=self.f, width=4, height=2, justify='center', anchor='center')
        self.PostGame=Frame(self.win)
        self.Quit=Button(self.PostGame, font=self.f, text="Quit", command=self.end)
        self.Play=Button(self.PostGame, font=self.f, text="Start", command=self.play)
        self.Quit.pack(side="left")
        self.Play.pack(side="left")
        self.Objective.pack()
        self.MainB.pack()
        self.PostGame.pack()
        self.win.mainloop()
    def play(self):
        self.Objective.config(text="Hit the button in exactly 10 secs!")
        self.timerB=time.time()
        self.MainB.config(command=self.stopT, state='active')
    #this idea was taken from the stopwatch at http://code.activestate.com/recipes/124894-stopwatch-in-Tkinter/
    def stopT(self):
        self.timerE=time.time()
        if (int(self.timerE)-int(self.timerB))==10:
            self.Objective.config(text='You hit the button in exactly 10sec, AMAZING!')
        elif (int(self.timerE)-int(self.timerB))==1:
            self.Objective.config(text='You only waited 1 sec, be patient')
        else:
            self.Objective.config(text='You hit the buttoon after '+str(int(self.timerE)-int(self.timerB))+'seconds.')
        self.MainB.config(state='disabled')
    def end(self):
        self.win.destroy()
        self.new=ButtonMode()

#same rules as control, but switch the button to hit between two buttons
class ButtonSwap():
    def __init__(self):
        self.f=('Courier New', 30)
        self.fb=('Courier New', 25,'bold')
        self.win=Tk()
        self.win.geometry("800x250")
        self.win.title("Button Swap")
        self.Objective=Label(self.win, text="Be careful when Mashing!", font=self.fb)
        self.Objective.pack()
        self.Game=Frame(self.win)
        self.MainB1=Button(self.Game, text="Hit!", font=self.f, width=7, height=2, justify='center', anchor='center')
        self.MainB1.pack(side="left")
        self.MainB2=Button(self.Game, text="No Hit", font=self.f, width=7, height=2, justify='center', anchor='center')
        self.MainB2.pack(side="left")
        self.Game.pack()
        self.PostGame=Frame(self.win)
        self.qb=Button(self.PostGame, text="Quit", font=self.f, command=self.end)
        self.playb=Button(self.PostGame, text='Start', font=self.f, command=self.start)
        self.qb.pack(side='left')
        self.playb.pack(side='left')
        self.PostGame.pack()
        self.win.mainloop()
    def start(self):
        self.MainB1.config(text="Hit!", command=self.countUP,state='active')
        self.MainB2.config(text="No Hit", command=self.decrease, state='active')
        self.c=0
        self.win.after(random.randint(10000, 12000),self.swap)
    def countUP(self):
        self.c+=1
    def stop(self):
        self.MainB1.config(text="You Got", state='disabled')
        if self.c>=0:
            self.MainB2.config(text=(self.c,"Hits"), state='disabled')
        else:
            self.MainB2.config(text="0 Hits",state=disabled)
        self.playb.config(text="Play again?")
    def swap(self):
        self.MainB1.config(text='No Hit', command=self.decrease)
        self.MainB2.config(text='Hit!', command=self.countUP)
        self.win.after(6000, self.swap2)
    def swap2(self):
        self.MainB1.config(text='Hit!', command=self.countUP)
        self.MainB2.config(text='No Hit', command=self.decrease)
        self.win.after(6000, self.stop)
    def decrease(self):
        self.c=self.c-2
    def end(self):
        self.win.destroy()
        self.new=ButtonMode()

#rulebook for the player
class Rules():
    def __init__(self):
        self.win=Tk()
        self.win.title('Rulebook')
        self.rules="""
Button Masher: After clicking start,
click the center button rapidly for 10 seconds,
each click is worth 1 point

Button Accuracy: After clicking start,
wait 10 seconds before clicking.

Button Control: After clicking start,
keep clicking until told otherwise.
Each right click is worth 1 point
while each wrong click takes away 7

Button Swap: after clicking start,
press the correct button!
Each right click is worth 1 point
while each wrong one takes away 2"""
        self.f=('New Courier', 16)
        self.explain=Label(self.win, text=self.rules, font=self.f)
        self.explain.pack()
        self.ok=Button(self.win, font=self.f, command=self.end, text='Ok')
        self.ok.pack()
    def end(self):
        self.win.destroy()
        self.new=ButtonMode()

#main screen
class ButtonMode():
    def __init__(self):
        self.f=('Courier New', 30)
        self.fb=('Courier New', 30, 'bold')
        self.win=Tk()
        self.win.title('Button Game')
        self.Modes=Label(self.win,text='Choose the game you want to play!', font=self.fb)
        self.Modes.pack()
        self.mode1=Button(self.win, text='Button Masher',command=self.play1, font=self.f, width=15)
        self.mode2=Button(self.win, text='Button Accuracy',command=self.play2, font=self.f, width=15)
        self.mode3=Button(self.win, text='Button Control',command=self.play3, font=self.f, width=15)
        self.mode4=Button(self.win, text='Button Swap',command=self.play4, font=self.f, width=15)
        self.mode1.pack()
        self.mode2.pack()
        self.mode3.pack()
        self.mode4.pack()
        self.quit=Button(self.win,font=self.f, text='Quit',command=self.win.destroy)
        self.quit.pack()
        self.rules=Button(self.win,font=self.f, text='See Rulebook', command=self.rulebook)
        self.rules.pack()
        self.win.mainloop()
    #the mode select portion is here
    def play1(self):
        self.win.destroy()
        self.play=ButtonMasher()
        
    def play2(self):
        self.win.destroy()
        self.play=ButtonAccuracy()
        
    def play3(self):
        self.win.destroy()
        self.play=ButtonControl()
        
    def play4(self):
        self.win.destroy()
        self.play=ButtonSwap()
        
    def rulebook(self):
        self.win.destroy()
        self.read=Rules()
start=ButtonMode()
