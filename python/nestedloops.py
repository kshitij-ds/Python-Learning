#nested loops = the inner loopos will finish it's interation before finishing pne iteration of the outer loop

#program to create a rectangle using the desired symbol 

rows= int(input('how many rows?:'))
columns= int(input('how many columns?:'))
symbol=input('enter a symbol to use:')


for i in range(rows):   #outer loop
    for j in range(columns): #inner loop
        print(symbol, end="") #end helps to moving cursor on terminal to the next line
    print()