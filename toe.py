from tkinter import *
import random

def vez_de_cada(row, column):
    global player
    if buttons[row][column]['text'] == "" and verif_vencedor() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if verif_vencedor() is False:
                player = players[1]
                label.config(text=("É a vez do " + players[1]))
            elif verif_vencedor() is True:
                label.config(text=(players[0]+ " venceu"))
            elif verif_vencedor() == "Empate":
                label.config(text=("Empate"))
        else:
            buttons[row][column]['text'] = player

            if verif_vencedor() is False:
                player = players[0]
                label.config(text=("É a vez do " + players[0]))
            elif verif_vencedor() is True:
                label.config(text=(players[1]+ " venceu"))
            elif verif_vencedor() == "Empate":
                label.config(text=("Empate"))

def verif_vencedor():
        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                return True
        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                buttons[0][column].config(bg="green")
                buttons[1][column].config(bg="green")
                buttons[2][column].config(bg="green")
                return True
        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True
        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            return True
        elif empty_spaces() is False:
            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="yellow")
            return "Empate"
        else:
            return False

def empty_spaces():
    
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True
def new_game():
    global player

    player = random.choice(players)
    window.config(bg="black")
    label.config(text="É a vez do " + player)
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="black")

window = Tk()
window.title("Jogo da velha")
window.config(bg="black")
players = ["X", "O"]
player = random.choice(players)

buttons=[[0, 0, 0], 
        [0, 0, 0,], 
        [0, 0, 0]]

label = Label(text= "É a vez do " + player, font = ('Verdana', 30, 'bold'), bg ='black', fg = 'white')
label.pack(side ="top")
reset_button = Button(text="Reniciar", font = ('Verdana', 20, 'bold'), command = new_game)
reset_button.pack(side ="bottom")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font = ('consolas', 40), width=7, height=2, command=lambda row=row, column=column: vez_de_cada(row, column), bg="Black", fg="white" )
        buttons[row][column].grid(row=row, column=column)
window.mainloop()