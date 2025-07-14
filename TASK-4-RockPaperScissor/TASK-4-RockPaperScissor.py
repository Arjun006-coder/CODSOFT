import random
compmoves=["snake","water","gun"]
scores=[["d","w","l"],["l","d","w"],["w","l","d"]]
def move(x):
    while True:
        if x=="snake":
            return 0
        elif (x=="water"):
            return 1
        elif x=="gun" :
            return 2
        else:
            print("Enter Valid Move!!!")
            continue
def game(n):
    cpoints=0
    ppoints=0
    i=0
    while i<n:
        print(f"FOR {i+1}th round".center(100))
        y=random.choice(compmoves)
        k=compmoves.index(y)
        j=input("Enter move: ").lower()
        u=move(j)
        condition=scores[u][k]
        if condition=="l":
            print(f"Your Move :{j}\t\tComputer Move :{y}")
            print("Conputer won this round")
            cpoints+=1
            i+=1
        elif condition=="w":
            print(f"Your Move :{j}\t\tComputer Move :{y}")
            print("You won this round")
            ppoints+=1
            i+=1
        else :
            print(f"Your Move :{j}\t\tComputer Move :{y}")
            print("This round was draw play this round again-")
    if(cpoints>ppoints):
        print("\nComputer won the match :**( ")
    else:
        print("\nYou won the match :>")
print("-"*50,"SNAKE-WATER-GUN","-"*50)
while True:
    print('''Choose Game type:
      1. Best of three
      2. Best of five
      3. Best of seven
      4. Quit''')
    gametype=input(" : ")
    if gametype=="1":
        game(3)
        print("-"*150)
    elif(gametype=="2"):
        game(5)
        print("-"*150)
    elif(gametype=="3"):
        game(7)
        print("-"*150)
    elif(gametype=="quit"):
        break
    else:
        print("Enter Valid choice")
        continue