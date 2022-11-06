dictionary = {}

while (True):
    choice = input("Add or look up a word? (a/1)? ")
    if (choice == "a"):
        newWord = input("Type the word: ")
        newDef = input("Type the definition: ")
        dictionary[newWord] = newDef
        print ("Word added!")
    elif (choice == "1"):
        word = input("Type the word: ")
        if (word in dictionary): print (dictionary[word])
        else: print ("That word isn't in the dictionary yet.")
    elif (choice == "Q"):
        break
print ("Dictionary by Alexander Li")
