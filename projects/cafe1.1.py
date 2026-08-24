while True:
    print(" ")
    print("-------------------")
    print("      Welcome")
    print("-------------------") 
    print(" ")
    print("1. Tea")
    print("2. Coffee")
    print("3. Beverages")
    print("4. Starter")
    print(" ")
    order=int(input("What you would like to order?: "))
    if order==1:
        print(" ")
        print("1.Matcha")
        print("2.Masala chai")
        print("3.Pearl grey")
        print(" ")
        choice_1=int(input("Choose: "))
        print(" ")
        while True:
            if choice_1==1:
                print("Matcha: $5. Thankyou! Please collect your order from the counter")
                break
            elif choice_1==2:
                print("Masala Chai: $2 ")
                break
            elif choice_1==3:
                print("Pearl Gery: $10 ")
                break
            else:
                print("Sorry")
                break
    elif order==2:
        print(" ")
        print("1.Cappuccino")
        print("2.Espresso")
        print("3.Latte")
        print("4.Cold Brew")
        print(" ")
        choice_2=int(input("Choose: "))
        print(" ")
        while True:
            if choice_2==1:
                print("Cappuccino: $8")
                break
            elif choice_2==2:
                print("Espresso: $10")
                break
            elif choice_2==3:
                print("Latte: $5")
                break
            elif choice_2==4:
                print("Cold Brew: $15")
                break
            else:
                print("Sorry")
                break
    elif order==3:
        print(" ")
        print("1.Chocolate")
        print("2.Fruit Smoothie")
        print("3.Fresh lemonade")
        print("4.Kombucha")
        print(" ")
        while True:
            choice_3=int(input("Choose: "))
            print(" ")
            if choice_3==1:
                print("Chocolate: $5")
                break
            elif choice_3==2:
                print("Fruit Smoothie: $10")
                break
            elif choice_3==3:
                print("Fresh Lemonade: $8")
                break
            elif choice_3==4:
                print("Kombucha: $15")
                break
            else:
                print("Sorry")
                break
    elif order==4:
        print(" ")
        print("1.Avacado Toast")
        print("2.Bruschette")
        print("3.Loaded Nachos")
        print("4.Mozzarella Sticks")
        print(" ")
        while True:
            choice_4=int(input("Choose: "))
            print(" ")
            if choice_4==1:
                print("Avacado Toast: $20")
                break
            elif choice_4==2:
                print("bruschette: $18")
                break
            elif choice_4==3:
                print("Loaded Nachos: $20")
                break
            elif choice_4==4:
                print("Mozzarella Sticks: $15")
                break
            else:
                print("Sorry")
                break
    else:
        print("Sorry! Try Again")
                              