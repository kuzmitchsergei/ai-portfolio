#Tuples are immutable not like lists
#Tuples & Assignment
(x,y) = (4, 'fred')
print(y)


#Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)


#Sorting Lists of Tuples
d = {'a':10, 'c':22, 'b':1}
print(d.items())

print(sorted(d.items()))

t = sorted(d.items())
print(t)

for k, v in sorted(d.items()):
    print(k, v) 


#Sort by values instead of key
d = {'a':10, 'c':22, 'b':1}
tmp = list()
for k, v in d.items():
    tmp.append((v, k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

#Shorter version
d = {'a':10, 'c':22, 'b':1}
print(sorted([(v,k) for k,v in d.items()]))


#Exercise10
fhand = open('mbox-short.txt')
counts = dict()

for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5]
    hour = time.split(':')[0]
    counts[hour] = counts.get(hour, 0) + 1
    print(counts)

for hour, count in sorted(counts.items()):
        print(hour, count)

