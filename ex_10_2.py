fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()

for line in fhand :
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != 'From' :
        continue
    else :
        time = words[5]
        timelst = time.split(':')
        timehour = timelst[0]
        if timehour in counts :
            counts[timehour] = counts[timehour] + 1
        else :
            counts[timehour] = 1
for k,v in sorted(counts.items()) :
    print(k,v)
