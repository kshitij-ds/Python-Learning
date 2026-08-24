# tupke = collection which is ordered and unchangable
#          used to group together related data

student=("Kshitij",18,"male")

print(student.count("Kshitij"))  #This gives  the how many times the given element is used in a tuple

print(student.index("male"))  #This is used to give the index number or the position of the element in a tuple

for x in student:
    print(x)
if "Kshitij" in student:
    print("Kshitij us here!")