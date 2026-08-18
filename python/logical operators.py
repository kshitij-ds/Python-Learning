#logical operators (and , or,not) are used to check conditional statements


temp=int(input("What is the temperature today?:"))
if temp>=0 and temp<=30:
    print("Today's temperature is good")   # "and" logical operator requires both statements to be true
    print("it's a great day for a walk")
elif temp<0 or temp>30:
    print("Temperature is bad today")   # "or" logical operator requires one if the condition to be true
    print("Prefer to stay indoors")

# if not(temp<0 or temp>39)  # if we add "not" operator then the result reverses for example true will become false