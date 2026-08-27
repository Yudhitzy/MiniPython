import random,recipe,reveals
from unittest import case
import os
import time

def newCoffee():
    global Give,coffee,need_cup,ur_cup,correct
    Give = False
    coffee = recipe.recipe()
    need_cup = recipe.cooking(coffee)
    ur_cup.clear()
    correct = False

def run_game():
    global Give,coffee,need_cup,correct,ur_cup
    Give = False
    coffee = recipe.recipe()
    need_cup = recipe.cooking(coffee)
    correct = False
    ur_cup = []

    while correct == False:
        os.system("cls")
        print(f"""      Recipe
        [1] Espresso
        [2] Water
        [3] Chocolate
        [4] Milk
        [5] Milk Foam
        [6] Liquor
        [7] Ico
        [8] Syrup
        [9] Whipped Cream
        [10] Whiskey
        [11] Caramel
        [12] Ice Cream
        [X] Give it
        I Want {coffee}

        """)
        
        if len(ur_cup) == 0:
            print("Your Cup Is Empty")
        else :
            print ("Top")
            print ("-------------------------")
            for ing in reversed(ur_cup):
                print(ing)
            print ("-------------------------")
            print ("Bottom")
        
        opsi = input("Put Ingridients : ")
        match opsi:
            case "1" :
                ur_cup.append("Espresso")
            case "2" :
                ur_cup.append("Water")
            case "3" :
                ur_cup.append("Chocolate")
            case "4" :
                ur_cup.append("Milk")
            case "5" :
                ur_cup.append("Milk Foam")
            case "6" :
                ur_cup.append("Liquor")
            case "7" :
                ur_cup.append("Ico")
            case "8" :
                ur_cup.append("Syrup")
            case "9" :
                ur_cup.append("Whipped Cream")
            case "10" :
                ur_cup.append("Whiskey")
            case "11" :
                ur_cup.append("Caramel")
            case "12" :
                ur_cup.append("Ice Cream")
            case "X" :
                Give = True

        if Give:
            if need_cup is None or len(ur_cup) != len(need_cup):
                reveals.reveals_lose(ur_cup,need_cup)
                break

            for i in range(0,len(need_cup)):
                if ur_cup[i] != need_cup[i]:
                    reveals.reveals_lose(ur_cup,need_cup)
                    correct = True
                    break

            if correct == True:
                break
            else :
                reveals.reveals(ur_cup,need_cup)
                time.sleep(1)
                newCoffee()


if __name__ == '__main__':
    while True:
        run_game()
        ans = input("Restart? (Y/N): ")
        if not ans or ans[0].lower() != 'y':
            print("Goodbye!")
            break
