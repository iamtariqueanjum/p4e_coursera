#fname = input("Enter file name: ")
fhand = open('words.txt')
for line in fhand :
    text = line.rstrip()
    print(text.upper())
