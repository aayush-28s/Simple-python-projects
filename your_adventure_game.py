name = input("What is your name?: ")

print("Welcome to the adventure game ", name, "lets start")

q1 = input("You are in a empty dark road there is two way left or right choose your own way by thinking about it? (left/right) ").lower()
if q1 == "left":
    q2 = input("You choose the left direction and there is a beautiful house so you want to enter in the house? (yes/no)")
    if q2 == "yes":
        print("You choose to enter the house and there is a lion who killed you. You lost the game")
    elif q2 == "no":
        q3 = input("you don't enter the house so later you saw an old man. You want to (talk/kill) the old man? ")
        if q3 == "talk":
            print("You loose the game as he hides the secret with him of the tressure")
        elif q3 == "kill":
            q4 = input("You killed the old man and you got a map of tressure from the pants choose you want to follow the map or leave? (follow/leave) ")
            if q4 == "follow":
                q5 = input("you have two caves one is dark and big other is bright and small? choose (big/small)")
                if q5 == "big":
                    print("You choose the wrong cave there is a lion you died")
                elif q5 == "small":
                    print("You have choose a small cave and there is a tons of gold and diamonds.You won")
                else:
                    print("You choose an invalid option. You lost the game")
            elif q4 == "leave":
                print("you lost the game as you left the map")
            else:
                print("You choose an invalid option. You lost the game")
        else:
            print("You choose an invalid option. You lost the game")
    else:
        print("You choose an invalid option. You lost the game")
elif q1 == "right":
    print("you choose the wrong path you die")
else:
    print("You choose an invalid option. You lost the game")