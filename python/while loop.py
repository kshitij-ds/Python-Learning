#while loop= a statement that will execute it's block of code as long as it's condition is true

name= ""

while len(name)==0:
    name=input("What is your name?:")
print("hello "+name)

#same code 

name=None

while not name:
    name=input("enter name:")
print("hello "+name)