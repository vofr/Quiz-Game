import tkinter as tk
import Prover
from PIL import Image, ImageTk

gui = tk.Tk()
gui.geometry("1000x600")
gui.configure(bg='black')

def startPage():
    for widgets in gui.winfo_children():
        widgets.destroy()
    my_text = "Mafioso"

    title = tk.Label(
        text=my_text,
        font=('Helvetica bold', 48),
        fg='#b31905',
        bg="black",
        width=20,
        height=10
    )
    title.place(x=130, y=-120)

    startGameBtn = tk.Button(
        text="Start",
        command=lambda: levelChoose(),
        fg='black',
        bg='#313639',
        width=20,
        height=2
    )
    startGameBtn.place(x=430, y=300)
    gui.mainloop()


def hideWindow(panel, fct):
    panel.pack_forget()
    level1()


def levelChoose():
    for widgets in gui.winfo_children():
        widgets.destroy()
    img = ImageTk.PhotoImage(Image.open("logo.jpg").resize((300, 75), Image.Resampling.LANCZOS))
    panel = tk.Label(gui, image=img)
    panel.pack()
    panel.place(x=350, y=20)
    level1Btn = tk.Button(
        text="Level 1",
        command=lambda: level1(),
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    level1Btn.place(x=135, y=500)
    level1Description = tk.Label(
        text="This puzzle known as 'Malice and Alice'\n was written by George J. Summers \nand published in his book \n'Logical Deduction Puzzles'.\nHere you will find the story\nbehind the death of one\n Alice's members of family.\nYou do have enough informations \nto find the kiler and the victim also\n\n\n\n\n Can you solve the case?\n\n\n",
        font=('Helvetica bold', 10),
        fg='black',
        bg="#2C2E2F",
    )
    level1Description.place(x=80, y=200)

    level2Btn = tk.Button(
        text="Level 2",
        command=lambda: level2(),
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    level2Btn.place(x=465, y=500)
    level2Description = tk.Label(
        text="5 friends have a simple board game\nnight.They play the famous Mafia game\nAfter collecting all the informations\nyou should reveal every player identity\n\n\n\n\n\n\n\n\n\n Can you do it?\n\n\n",
        font=('Helvetica bold', 10),
        fg='black',
        bg="#2C2E2F",
    )
    level2Description.place(x=400, y=200)

    level3Btn = tk.Button(
        text="Level 3",
        command=lambda:level3(),
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    level3Btn.place(x=775, y=500)
    level3Description = tk.Label(
        text="You're name is Mark Lutwiss\nand you are a leader of a big mafia\norganization in which prime work is to\ndistribuit drugs\nin your home town: Boston.\nA group of 5 people finds one\nof your hidding spots for drugs.\nLuckly for you, you find them\nNow you're carrefouly listening\nto everybody's stataments about\nwho took drugs.Take\nyour time and found at least\n2 of them that took drugs\nThey'll have to pay.\nCan you spot the right ones?\n\n",
        font=('Helvetica bold', 10),
        fg='black',
        bg="#2C2E2F",
    )
    level3Description.place(x=715, y=200)

    backBtn = tk.Button(
        text="Back",
        fg='white',
        command=lambda: startPage(),
        bg='#b31905',
        width=15,
        height=2
    )
    backBtn.place(x=10, y=20)
    gui.mainloop()


def entryMenu(buttons, label):
    buttons.place_forget
    label.place_forget
    levelChoose()


def level1():
    for widgets in gui.winfo_children():
        widgets.destroy()
    aux = True
    backBtn = tk.Button(
        text="Back",
        fg='white',
        command=lambda: levelChoose(),
        bg='#b31905',
        width=15,
        height=2
    )
    backBtn.place(x=10, y=20)

    level1Description = tk.Label(
        text="A crime took place in Alice's family, you know the following:'\n Alice, Alice’s husband, their son, their daughter, and Alice’s brother were involved in a murder. \nOne of the five killed one of the other four. The following facts refer to the five people mentioned:\n"
             "\n1) A man and a woman were together in a bar at the time of the murder.\n"
             "2) The victim and the killer were together on a beach at the time of the murder.\n"
             "3) One of Alice’s two children was alone at the time of the murder.\n"
             "4) Alice and her husband were not together at the time of the murder.\n"
             "5) The victim’s twin was not the killer.\n"
             "6) The killer was younger than the victim.\n"
             "\n\nWhich one of the five was the victim?   Take some time to try to work out a solution. \n(press a button that corresponds to your guess of who is the victim)",
        font=('Helvetica bold', 10),
        fg='white',
        bg="black",
    )
    level1Description.place(x=170, y=110)

    hintBtn = tk.Button(
        text="Hint?",
        fg='white',
        command=lambda: showHint(),
        bg='#b31905',
        width=10,
        height=1
    )
    hintBtn.place(x=10, y=550)

    hintDescription = tk.Label(
        text="You should assume that the victim’s twin is one of the five people mentioned.) Summers’ book offers the following hint: \n“First find the locations of two pairs of people at the time of the murder,\nand then determine who the killer and the victim were so that no condition is contradicted.",
        font=('Helvetica bold', 10),
        fg='white',
        bg="black",
    )

    aliceBtn = tk.Button(
        text="Alice",
        command=lambda: [revealAnswer(Prover.puzzle(1,0))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    aliceBtn.place(x=100, y=450)

    aliceHusbandBtn = tk.Button(
        text="Alice's Husband",
        command=lambda: [revealAnswer(Prover.puzzle(1,1))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    aliceHusbandBtn.place(x=250, y=450)

    sonBtn = tk.Button(
        text="Son",
        command=lambda: [revealAnswer(Prover.puzzle(1,2))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    sonBtn.place(x=400, y=450)

    daughterBtn = tk.Button(
        text="Daughter",
        command=lambda: [revealAnswer(Prover.puzzle(1,3))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    daughterBtn.place(x=550, y=450)

    aliceBroBtn = tk.Button(
        text="Alice's Brother",
        command=lambda: [revealAnswer(Prover.puzzle(1,4))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    aliceBroBtn.place(x=700, y=450)

    def showHint():
        hintDescription.place(x=150, y=530)

    gui.mainloop()



def level2():
    for widgets in gui.winfo_children():
        widgets.destroy()
    backBtn = tk.Button(
        text="Back",
        fg='white',
        command=lambda: levelChoose(),
        bg='#b31905',
        width=15,
        height=2
    )
    backBtn.place(x=10, y=20)

    level2Description = tk.Label(
        text="Five people sit around a table playing Mafia.\nAmong them are two innocent people, two Mafiosos, and one detective.\nThe Mafia people know each other; the detective knows who each of them is;\nand the innocent people have no information whatsoever\nabout anyone at the table.\n"
             "\nDuring this particular game, the innocents and the detective always tell the truth, while mafia people always lie.\nThey start by going around the circle making the following statements:\n"
             "A: I know who B is.\nB: I know who the detective is.\nC: I know who B is.\nD: I know who E is."
             "\n\n Can you reveal tha mafia guys?",
        font=('Helvetica bold', 10),
        fg='white',
        bg="black",
    )
    level2Description.place(x=170, y=110)

    hintBtn = tk.Button(
        text="Hint?",
        fg='white',
        command=lambda: showHint(),
        bg='#b31905',
        width=10,
        height=1
    )
    hintBtn.place(x=10, y=550)

    hintDescription = tk.Label(
        text="You should consider that the first 2 persons\n“Cannot be innocent since they already know something",
        font=('Helvetica bold', 10),
        fg='white',
        bg="black",
    )

    def showHint():
        hintDescription.place(x=150, y=530)

    aBtn = tk.Button(
        text="A and C",
        command=lambda:[ revealAnswer(Prover.puzzle(2,0))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    aBtn.place(x=250, y=450)

    bBtn = tk.Button(
        text="B and E",
        command=lambda:[ revealAnswer(Prover.puzzle(2,1))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    bBtn.place(x=450, y=450)

    cBtn = tk.Button(
        text="A and E",
        command=lambda: [revealAnswer(Prover.puzzle(2,2))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    cBtn.place(x=650, y=450)




def level3():
    for widgets in gui.winfo_children():
        widgets.destroy()
    backBtn = tk.Button(
        text="Back",
        fg='white',
        command=lambda: levelChoose(),
        bg='#b31905',
        width=15,
        height=2
    )
    backBtn.place(x=10, y=20)

    level3Description = tk.Label(
        text="Determine who out of the following is guilty of doping.\n The suspects are: Sam, Michael, Bill, Richard, Matt.\n1) Sam said: Michael or Bill took drugs, but not both.\n2) Michael said: Richard or Sam took drugs, but not both\n3) Bill said: Matt or Michael took drugs, but not both.\n4) Richard said: Bill or Matt took drugs, but not both.\n5) Matt said: Bill or Richard took drugs, but not both.\n6) Tom said: If Richard took drugs, then Bill took drugs.\nOnly the 6 statement is 100% true\n in the frist 5 statements 1 is a lie.\n\n\n Can you find who took for sure drugs? ",
        font=('Helvetica bold', 10),
        fg='white',
        bg="black",
    )
    level3Description.place(x=350, y=150)

    hintBtn = tk.Button(
        text="Hint?",
        fg='white',
        command=lambda: showHint(i),
        bg='#b31905',
        width=10,
        height=1
    )
    hintBtn.place(x=10, y=550)

    hintDescription = tk.Label(
        text="\nStatements 1 3 4",
        font=('Helvetica bold', 10),
        fg='white',
        bg="black",
    )

    def showHint(i):
        if i%2 == 0 :
            hintDescription.place(x=150, y=530)
        else :
            hintDescription.place_forget()

    aBtn = tk.Button(
        text="Sam & Bill",
        command=lambda:[ revealAnswer(Prover.puzzle(3,0))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    aBtn.place(x=250, y=450)

    bBtn = tk.Button(
        text="Richard & Matt",
        command=lambda:[ revealAnswer(Prover.puzzle(3,1))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    bBtn.place(x=450, y=450)

    cBtn = tk.Button(
        text="Michael & Matt",
        command=lambda: [revealAnswer(Prover.puzzle(3,2))],
        fg='black',
        bg='#313639',
        width=15,
        height=2
    )
    cBtn.place(x=650, y=450)

def revealAnswer(ans):
    for widgets in gui.winfo_children():
        widgets.destroy()
    backBtn = tk.Button(
        text="Back",
        fg='white',
        command=lambda: levelChoose(),
        bg='#b31905',
        width=15,
        height=2
    )
    backBtn.place(x=10, y=20)

    label1 = tk.Label(
        text="YOUR ANSWER IS",
        font=('Helvetica bold', 20),
        fg='white',
        bg="black",
    )
    label1.place(x=400, y=100)

    label2 = tk.Label(
        text="CORRECT",
        font=('Helvetica bold', 20),
        fg='green',
        bg="black",
    )
    label3 = tk.Label(
        text="WRONG",
        font=('Helvetica bold', 20),
        fg='red',
        bg="black",
    )
    if (ans == True):
        label2.place(x=430, y=160)
    else:
        label3.place(x=430, y=160)
    gui.mainloop()

if __name__ == '__main__':
    startPage()
