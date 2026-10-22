#Dictionaries

#List (review)

cards = list()
cards.append(12)
cards.append(3)
cards.append(75)
print(cards)

print(cards[1])

cards[1] = cards[1] + 2
print(cards)

#Dictionaries
cabinet = dict()
cabinet['summer'] = 12
cabinet['fall'] = 3
cabinet['spring'] = 75
print(cabinet)

print(cabinet['fall'])

cabinet['fall'] = cabinet['fall'] + 2
print(cabinet)


#Many counters with a Dictionary
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

#When we see a new name
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


#The get method for dictionaries
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


#definite loops and dictionaries
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])


#retrieving lists of keys and values
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))

print(list(jjj.keys()))

print(list(jjj.values()))

print(list(jjj.items()))


#two iterations variables
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)


#Exercise 9
fhand = open('mbox-short.txt')
counts = dict()

for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

    #find the biggest
bigword = None
bigcount = None
for word, count in counts.items():
    if bigcount is None or count > bigcount: 
        bigword = word
        bigcount = count
print(bigword, bigcount)

