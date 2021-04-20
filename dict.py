purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)
for key in purse :
    print(key, purse[key])
