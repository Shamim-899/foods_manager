like_foods = []

while True:
    print("Welcome to Like Foods Manager")
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View All Like Foods")

    option = input("Select an option: ")

    if option == "0":
        print("Thanks for using our like Foods Manager")
        break
    elif option == "1":
        food = input("Enter a like Food name: ")
        like_foods.append(food)
        print(f"{food} added Successfully")

    elif option == "2":
        food = input("Enter a food name which you want to remove: ")
        if food in like_foods:
            like_foods.remove(food)
            print(f"{food} remove Successfully")
        else:
           print("Food not found in the list")


    elif option == "3":
        if like_foods:
            for i, food in enumerate(like_foods,start=1):
                print(f"{i}. {food.upper()}")
        else:
            print("Like Foods is empty, Please added first your like foods")

    else:
        print("Invalid Option!")

