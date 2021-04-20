abc = 'With;Three;Words'
stuff = abc.split()
print(stuff)
stuff = abc.split(';')
print(stuff)
print(len(stuff))
print(stuff[0])
line = 'A lot          of spaces'
etc = line.split()
print(etc)
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
word = line.split()
email = word[1]
print(email)
pieces = email.split('@')
print(pieces)
