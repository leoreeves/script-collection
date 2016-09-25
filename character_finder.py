# finds a character in a word

word = input("Word: ")
print("Please enter required character below:")

while True:
    count = int(input("character: ")) - 1
    if count > len(word):
        print("Invalid character")
    else:
        print ((str(int(count) + 1)+ " = " + password[count]))