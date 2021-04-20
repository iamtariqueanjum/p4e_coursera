fname = input("Enter file name: ")
lst = []
lst2 = open(fname).read().split()
for word in lst2:
    if word in lst :
        continue
    else :
        lst.append(word)
lst.sort()
print(lst)
