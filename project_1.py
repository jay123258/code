import random
user = input("enter your choice: ")


dics = {
    "s": 1, "w" : -1, "g" : 0
}

you  = dics[user]
com =  random.choice([1,0,-1])
if(com == you):
    print("with draw")

else:
    if(com == 0 and you == 1):
        print("winer")
    elif(com == 1 and you == 0):
        print("loser")
    if(com == -1 and you == 0):
        print("winer")
    elif(com == 1 and you == 1):
        print("with draw")
    if(com == 1 and you == 1):
        print("with draw")
    elif(com == -1 and you == 1):
        print("winer")
    if(com == 1 and you == -1):
        print("loser")





print(f"user choice is {you}\ncomputer choice is {com}")


