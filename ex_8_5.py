fname = input("Enter file name: ")
fhand = open(fname)
count = 0
for line in fhand :
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0]!='From' :
        continue
    else :
        count = count + 1
        print(words[1])
print("There were", count, "lines in the file with From as the first word")
