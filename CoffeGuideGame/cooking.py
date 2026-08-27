def cooking(code):
    ingredients = {
        "1": "Espresso",
        "2": "Water",
        "3": "Chocolate",
        "4": "Milk",
        "5": "Milk Foam",
        "6": "Liquor",
        "7": "Ico",
        "8": "Syrup",
        "9": "Whipped Cream",
        "10": "Whiskey",
        "11": "Caramel",
        "12": "Ice Cream",
    }
    return ingredients.get(code)
