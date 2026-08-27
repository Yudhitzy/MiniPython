import random,recipe,reveals,cooking
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
        if opsi.upper() == "X":
            Give = True
        else:
            ingredient = cooking.cooking(opsi)
            if ingredient is not None:
                ur_cup.append(ingredient)

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
