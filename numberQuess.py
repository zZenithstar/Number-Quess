#number quess game
#2 game style we have.first one is the us quessing and the second one is computer queissing!
import random
from turtle import down
print("---WELCOME TO QUESS GAME---")
name = input("What's Your Name: ")

def menu():
    play = True
    while(play):
        print("-----MENU-----\nWho is Quessing?")
        print(f"1-)COMPUTER\n2-){name}")
        gameMode = input("Your Chose: ")

        if(gameMode == "1"):
            computer()

            again = input("AGAIN?(y/n): ")
            again = again.lower
            if(again == "y" or again == "yes"):
                play = True
            elif(again == "n" or again == "no"):
                play = False
            else:
                print("Invalid Input!")
            
        elif(gameMode == "2"):
            player()

            again = input("AGAIN?:(y/n) ")
            again = again.lower
            if(again == "y" or again == "yes"):
                play = True
            elif(again == "n" or again == "no"):
                play = False
            else:
                print("Invalid Input!")

        else:
            print("Invalid Input!")

        


def computer():
    #bilgisayar tahmin ediyor 7 hakkı var!
    print("!!IF YOU CHOOSE YOUR NUMBER LET'S START")
    playing = True
    quessCount = 0
    upLim = 101
    downLim = 0
    while(playing):
        if(quessCount<=7):
            print(f"--- RIGHT TO QUESS: {7 - quessCount} ---")
            if downLim >= upLim:
                quess = downLim
            else:
                quess = random.randrange(downLim, upLim)

            isTrue = input(f"Your Number Is: {quess}\n1-)CORRECT\n2-)GO UP\n3-)GO DOWN\n")
            if(isTrue == "1"):
                print("!!YOU LOSE!!\n!!COMPUTER WIN!!")
                playing = False
                    
            elif(isTrue == "2"):
                downLim = quess
                quessCount +=1

            elif(isTrue == "3"):
                upLim = quess
                quessCount +=1

            else:
                print("Invalid Input!")
        else:
            print("!!YOU WIN!!")








def player():
    #oyuncu tahmin ediyor 7 tahmin hakkı var!
    randomNum = random.randrange(0,101)
    playing = True
    quessCount = 0
    print("NUMBER BETWEEN OF 1-100\nGood Luck!")
    upLim = 100
    downLim = 0
    while(playing):
        if(quessCount<=7):
            print(f"--- RIGHT TO QUESS: {7 - quessCount} ---")

            try:
                quess = int(input(f"({downLim}-{upLim})QUESS: "))
            except ValueError:
                print("Invalid Input!")
                continue


            if(quess==randomNum):
                print("-----------")
                print("!!YOU WIN!!")
                print("-----------")
                playing = False
            elif(quess>randomNum):
                print("-----------")
                print("!!GO DOWN!!")
                print("-----------")
                upLim = quess
                quessCount += 1

            elif(quess<randomNum):
                print("-----------")
                print("!!GO UP!!")
                print("-----------")
                downLim = quess
                quessCount += 1

            else:
                print("Invalıd Input")
        else:
            print("-----------")
            print("!!YOU LOSE!!")
            print(f"RANDOM NUM IS: {randomNum}")
            print("-----------")
            playing = False
    



if (__name__ == "__main__"):
    menu()
