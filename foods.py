from queue import PriorityQueue

favourite_foods=[]

while True:
    print("Well Come To Our Favourite Foods Service")
    print("0. Exit")
    print("1. Added Your Favourite Foods Name")
    print("2. Remove Your Foods Name")
    print("3. View Your All Chosen List")

    choice = input("Please Select an option: ")

    if choice =="0":
        print("Thank You Using Our Food Service")
        break

    elif choice =="1":
        food=input("Please Enter Your Favourite Items: ")
        favourite_foods.append(food)
        print(f"{food} Added Successfully")

    elif choice =="2":
        food=input("Please Enter Your Food Items Which Went You Remove")
        favourite_foods.remove(food)
        print(f"{food} is Remove Successfully")
"""
    elif choice =="3":
        if favourite_foods:
            print("Your Chosen Foods Items is: ")
       for index, food in enumerate(favourite_foods, start=1):
        print(f"{index}.{food}")
       else:
        print("Food List is empty or didn't added yet! ")
"""
else:
    print("Invalid Choice!")






