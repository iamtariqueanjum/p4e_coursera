d = {'b' : 10, 'a' : 1, 'c' : 22}
print(d.items())
print(sorted(d.items()))
#sorting based on keys
for k,v in sorted(d.items()) :
    print(k,v)
#sorting based on values
tmp = list()
for k,v in d.items() :
    tmp.append((v,k))
tmp = sorted(tmp,reverse = True)
print(tmp)
