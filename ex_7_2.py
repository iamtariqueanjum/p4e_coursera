fname = input("Enter file name: ")
fhand = open(fname)
count=0
s = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    pos = line.find(':')
    str = line[pos+1: ]
    value = float(str)
    s = s + value
    count = count + 1
print('Average spam confidence:',s/count)
