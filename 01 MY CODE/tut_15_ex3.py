n =18
chansuu = 9
print("Welcome to the game \n you have 9 choices to guess the number \n after that game over")
while chansuu >0:
    lelo = int(input("Enter your number here "))
    if lelo == n :
        print("Hai sekai desu ")
        break
    elif lelo >n :
        print("The number you have enterd is bigger then the number ")
        chansuu -= 1
        print("You have", chansuu, "chances left.\n")

    else :

        print("The number you have entered is smaller than the number")
        chansuu -= 1
        print("You have", chansuu, "chances left.\n")

    if chansuu == 0:
        print("Game over! The correct number was", n)
    print("Thanks for playing the game !")