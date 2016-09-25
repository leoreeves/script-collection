# finds a character in a word

word = input("Word: ")

while True:
    count = int(input("Character: ")) - 1
    if count > len(word):
        print("Invalid character")
    else:
        print ((str(int(count) + 1)+ " = " + word[count]))