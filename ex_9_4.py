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
        email = words[1]
        if email in counts :
            counts[email] = counts[email] + 1
        else :
            counts[email] = 1
maxcount = -1
for k,v in counts.items() :
    if v > maxcount :
        maxemail = k
        maxcount = v
print(maxemail,maxcount)
