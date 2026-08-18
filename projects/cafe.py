print("-------------------")
print("      Welcome")
print("-------------------") 

print("1. Tea")
print("2. Coffee")
print("3. Beverages")
print("4. Starters")
print(" ")
order=int(input("What you whould like to order?: "))
print(" ")
if order == 1:
    while True:
        print("1. Earl Grey")
        print("2. Matcha")
        print("3. Masala Chai")
        
        choice_1=int(input("Select: "))
        if choice_1==1:
            print("Earlgrey: $5")
            break
        elif choice_1==2:
            print("Matcha: $10")
            break
        elif choice_1==3:
            print("Masala chai: $4")
            break
        else:
            print("Sorry:/")
        
            
elif order == 2:
    print("Espresso")
    print("Cappuccino")
    print("Latte")
    print("Cold Brew")
elif order==3:
    print("Chocolate")
    print("Fruit Smoothie")
    print("Fresh Lemonade")
    print("Kombucha")
elif order==4: 
    print("Avacado Toast")
    print("Bruschetta")
    print("Loaded Nachos")
    print("Mozzarella Sticks")
else:
    print("Sorry we don't have for what  you are looking for.")
