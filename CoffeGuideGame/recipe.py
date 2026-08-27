import random
def recipe():
    list_coffee = ["Espresso","Americano","Latte","Cappuccino",
                  "Macchiato","Mocha","Flat White","Corretto",
                  "Glace","Frappe","Raf","Irish Coffee","Vienna",
                  "Freddo","Bicerin","Galao"]
    return random.choice(list_coffee)

def cooking(recipe):
    match recipe:
        case "Espresso":
            return ["Espresso"]
        case "Americano":
            return ["Espresso","Water"]
        case "Latte":
            return ["Espresso","Milk","Milk Foam"]
        case "Cappuccino":
            return ["Espresso","Milk","Milk Foam"]
        case "Macchiato":
            return ["Espresso","Milk Foam"]
        case "Mocha":
            return ["Espresso","Chocolate","Milk","Milk Foam"]
        case "Flat White":
            return ["Espresso","Milk"]
        case "Corretto":
            return ["Espresso","Liquor"]
        case "Glace":
            return ["Espresso","Ice Cream","Chocolate"]
        case "Frappe":
            return ["Espresso","Ico","Milk"]
        case "Raf":
            return ["Syrup","Espresso","Milk Foam"]
        case "Irish Coffee" :
            return ["Espresso","Whiskey","Whipped Cream"]
        case "Vienna":
            return ["Espresso","Whipped Cream"]
        case "Freddo":
            return ["Espresso","Caramel","Milk"]
        case "Bicerin":
            return ["Chocolate","Espresso","Milk","Whipped Cream"]
        case "Galao":
            return ["Espresso","Milk Foam"]