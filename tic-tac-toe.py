from tkinter import *
from tkinter import messagebox
from random import randint
def createBoard():
    global fenetre,btnsList,count,B1,B2,B3,B4,B5,B6,B7,B8,B9
    count=0 #to know which person is player 
    fenetre = Tk()
    fenetre.geometry("500x300")
    fenetre.config(bg="black")
    lablel_1 = Label(fenetre, text="Player (X)", bg = "pink", fg = "black",
                width = 15, bd = 5)
    lablel_1.grid(row=0, column=2)
    B1 = Button(fenetre, activeforeground = '#F1948A',
                activebackground = "black", bg = "pink", fg = "black",command=lambda: insert(B1, (0, 0)),
                width = 15, font = 'summer', bd = 5)  
    B2 = Button(fenetre, activeforeground = '#F1948A',
                activebackground = "black", bg = "pink", fg = "black",command=lambda: insert(B2, (0, 1)),
                width = 15, font = 'summer', bd = 5)              
    B3 = Button(fenetre, activeforeground = '#F1948A',command=lambda: insert(B3, (0, 2)),
                activebackground = "black", bg = "pink", fg = "black",
                width = 15, font = 'summer', bd = 5) 
    B1.grid(row=2, column=0)
    B2.grid(row=2, column=1)
    B3.grid(row=2, column=2)
    B4 = Button(fenetre, activeforeground = '#F1948A',
                activebackground = "black", bg = "pink", fg = "black",command=lambda: insert(B4, (1, 0)),
                width = 15, font = 'summer', bd = 5)      
    B5 = Button(fenetre, activeforeground = '#F1948A',
                activebackground = "black", bg = "pink", fg = "black",command=lambda: insert(B5, (1, 1)),
                width = 15, font = 'summer', bd = 5)                      
    B6 = Button(fenetre, activeforeground = '#F1948A',
                activebackground = "black", bg = "pink", fg = "black",command=lambda: insert(B6, (1, 2)),
                width = 15, font = 'summer', bd = 5) 
    B4.grid(row=3, column=0)
    B5.grid(row=3, column=1)
    B6.grid(row=3, column=2)
    B7 = Button(fenetre, activeforeground = '#F1948A',
                activebackground = "black", bg = "pink", fg = "black",command=lambda: insert(B7, (2, 0)),
                width = 15, font = 'summer', bd = 5)                
    B8 = Button(fenetre, activeforeground = '#F1948A',
                activebackground = "black", bg = "pink", fg = "black",command=lambda: insert(B8, (2, 1)),
                width = 15, font = 'summer', bd = 5)  
    B9 = Button(fenetre, activeforeground = '#F1948A',
                activebackground = "black", bg = "pink", fg = "black",command=lambda: insert(B9, (2, 2)),
                width = 15, font = 'summer', bd = 5)  
    B7.grid(row=4, column=0)
    B8.grid(row=4, column=1)
    B9.grid(row=4, column=2)   
    B = Button(fenetre, text = "Quit game", command = Quit, activeforeground = '#F1948A',
                activebackground = "black", bg = "pink", fg = "black",
                width = 15, font = 'summer', bd = 5)           
    B.grid(row=5, column=1, columnspan=1) 
    btnsList = [B1, B2, B3, B4, B5, B6, B7, B8, B9]
#*********************************************************************
def createBoardList():
    global boardList
    boardList = [["", "", ""], ["", "", ""], ["", "", ""]]

# to quit the tkinter 0board window


def Quit():
    global fenetre
    msg = messagebox.askquestion("Confirm", "Are you sure you want to quit?")
    if msg == "yes":
        fenetre.destroy()

# to close the tkinter winning window and tkinter board window


def Destruct():
    global winnerWindow
    winnerWindow.destroy()
    fenetre.destroy()

# to start our game


def start():
    createBoard()
    createBoardList()
    moveAI(True)
    fenetre.mainloop()

# to inserts X or O in the board


def insert(button, position):
    global count, fenetre
    if button["text"] == "":
        if count % 2 != 0:
            button["text"] = "O"
            boardList[position[0]][position[1]] = "O"
            lablel_1 = Label(fenetre, text="Player (X)")
            lablel_1.grid(row=0, column=2)
        count += 1
        if count >= 5:
            checkWinner()
        else:
            moveAI(False)
    else:
        messagebox.showinfo("Error", "This cell is already occupied")

# to check if we got a winner on the board


def checkWinner():
    global count
    if boardList[0][0] == boardList[0][1] == boardList[0][2] != "" or boardList[1][0] == boardList[1][1] == boardList[1][2] != "" or boardList[2][0] == boardList[2][1] == boardList[2][2] != "" or boardList[0][0] == boardList[1][0] == boardList[2][0] != "" or boardList[0][1] == boardList[1][1] == boardList[2][1] != "" or boardList[0][2] == boardList[1][2] == boardList[2][2] != "" or boardList[0][0] == boardList[1][1] == boardList[2][2] != "" or boardList[0][2] == boardList[1][1] == boardList[2][0] != "":
        if count % 2 == 0:
            displayWinner("Player (O)")
        else:
            displayWinner("Player (X)")
    elif count == 9:
        displayWinner("Tie")
    else:
        if count % 2 == 0:
            moveAI(False)


# to display the winning window


def displayWinner(winner):
    global t, winnerWindow
    winnerWindow = Tk()
    winnerWindow.title("Winner")
    winningLabel = Label(winnerWindow, width=32,
                         height=4, text="THE WINNER IS: ")
    winningLabel.pack()
    winningPlayerLabel = Label(winnerWindow, width=32, height=4, text=winner)
    winningPlayerLabel.pack()
    bproceed = Button(winnerWindow, text="Replay",
                      width=16, height=2, command=Reset)
    bproceed.pack()
    bproceed = Button(winnerWindow, text="Proceed",
                      width=16, height=2, command=Destruct)
    bproceed.pack()

# to reset the game again


def Reset():
    global count, boardList
    count = 0
    B1["text"] = ""
    B2["text"] = ""
    B3["text"] = ""
    B4["text"] = ""
    B5["text"] = ""
    B6["text"] = ""
    B7["text"] = ""
    B8["text"] = ""
    B9["text"] = ""
    boardList = [["", "", ""], ["", "", ""], ["", "", ""]]
    winnerWindow.destroy()
    createBoardList()
    moveAI(True)

# get the final best position to choose by the ai


def getBestPosition(boardListCopy):
    global btnsList
    clonedBoardList = boardListCopy
    bestScore = -1000
    bestPosition = (0, 0)
    for i in range(3):
        for j in range(3):
            if clonedBoardList[i][j] == "":
                clonedBoardList[i][j] = "X"
                # apply the minimax algorithm on the cloned board list
                score = minimax(clonedBoardList, 0, False,-1000,1000)
                if score > bestScore:
                    bestScore = score
                    bestPosition = (i, j)
                clonedBoardList[i][j] = ""
    return bestPosition


# minimax algorithm
def minimax2(boardList, depth, isMaximizing):
    if isWinning(boardList) != None:  # if None => no winner yet and still playing
        return isWinning(boardList)  # 0, 1, -1
    if isMaximizing:
        bestScore = -1000
        for i in range(3):
            for j in range(3):
                if boardList[i][j] == "":
                    boardList[i][j] = "X"
                    score = minimax2(boardList, depth + 1, False)
                    bestScore = max(score, bestScore)
                    boardList[i][j] = ""
        return bestScore
    else:
        bestScore = 1000
        for i in range(3):
            for j in range(3):
                if boardList[i][j] == "":
                    boardList[i][j] = "O"
                    score = minimax2(boardList, depth + 1, True)
                    bestScore = min(score, bestScore)
                    boardList[i][j] = ""
        return bestScore
def minimax(boardList, depth, isMaximizing,alpha,beta):
    if isWinning(boardList) != None:  # if None => no winner yet and still playing
        return isWinning(boardList)  # 0, 1, -1
    if isMaximizing:
        bestScore = -1000
        for i in range(3):
            for j in range(3):
                if boardList[i][j] == "":
                    boardList[i][j] = "X"
                    score = minimax(boardList, depth + 1, False,alpha,beta)
                    bestScore = max(score, bestScore)
                    alpha=max(alpha,bestScore)
                    boardList[i][j] = ""
                    if beta<=alpha:
                        break
        return bestScore
    else:
        bestScore = 1000
        for i in range(3):
            for j in range(3):
                if boardList[i][j] == "":
                    boardList[i][j] = "O"
                    score = minimax(boardList, depth + 1, True,alpha,beta)
                    bestScore = min(score, bestScore)
                    beta=min(beta,bestScore)
                    boardList[i][j] = ""
                    if beta<=alpha:
                        break
        return bestScore

# give me the expected board with the player you want => give me if he would won


def isWinning(boardList):
    isTie = True
    for i in range(3):
        # check for X
        if boardList[i][0] == boardList[i][1] == boardList[i][2] == "X" or boardList[0][i] == boardList[1][i] == boardList[2][i] == "X" or boardList[0][0] == boardList[1][1] == boardList[2][2] == "X" or boardList[0][2] == boardList[1][1] == boardList[2][0] == "X":
            return 1
        # check for O
        if boardList[i][0] == boardList[i][1] == boardList[i][2] == "O" or boardList[0][i] == boardList[1][i] == boardList[2][i] == "O" or boardList[0][0] == boardList[1][1] == boardList[2][2] == "O" or boardList[0][2] == boardList[1][1] == boardList[2][0] == "O":
            return -1
        for j in range(3):
            if boardList[i][j] == "":
                isTie = False
    # check for tie
    if isTie:
        return 0
    # still playing without winner yet
    return None

# the computer move


def moveAI(isStart):
    global btnsList, boardList, count, fenetre
    if isStart:
        position = (randint(0, 2), randint(0, 2))
        boardList[position[0]][position[1]] = "X"
        btnsList[getBtnIndex(position)]["text"] = "X"
    else:
        position = getBestPosition(boardList.copy())
        boardList[position[0]][position[1]] = "X"
        btnsList[getBtnIndex(position)]["text"] = "X"
    lablel_1 = Label(fenetre, text="Player (O)", bg = "pink", fg = "black",
                width = 15, bd = 5)
    lablel_1.grid(row=0, column=0, columnspan=1)
    count += 1
    if count >= 5:
        checkWinner()

# input is a button index => output is its position


def getBtnPosition(btnIndex):
    for i in range(3):
        for j in range(3):
            if i*3+j == btnIndex:
                return (i, j)


# from position, get the index of the btn inside the btnsList

def getBtnIndex(position):
    return position[0]*3+position[1]


start()