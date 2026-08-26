# Dictionary is a changeable unordered  collection of unique key:value   pairs
#           Fast because they use hashing , allow us to acess a value quickly

capitals={'USA':'Wahington DC',
          'India':'New Delhi',
          'China':"Beijing",
          "Russia":"Moscow"}

capitals.update({"Germany":"Berlin"})  # Used to update the dictionary and add new value

capitals.update({"USA":"Las Vegas"}) # We can also edit any key or value using This Method

capitals.pop("China")  # Used to remove a Key:Value pair

capitals.clear()  #Used to clear the entire dictionary

#print(capitals["Russia"])
#print(capitals.get("Germany"))  # It is used to check whether the name is in the dictionary or not
#print(capitals.keys()) #Used to print only the keys
#print(capitals.values()) # Uses to print only the values
#print(capitals.items())  # this prints the entire dictionary
# to print the entire Dictionary Formaly we use:

for key,value in capitals.items():
    print(key ,value)