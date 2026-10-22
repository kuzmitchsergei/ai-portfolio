#Lists

#Collection

#print inside Lists

friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])


#Lists are Mutable, strings are immutable
fruit = 'Banana'

x = fruit.lower()
print(x)

lotto = [2, 14, 26, 41, 63]
print(lotto)

lotto[2] = 28
print(lotto)


#How long is a list
greet = 'Hello Bob'
print(len(greet))
#9
x = [1, 2, 'joe', 99]
print(len(x))
#4


#Using the range function


friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
#3
print(list(range(len(friends))))
#[0, 1, 2]


#A tale of two loops
friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
    print('Happy New Year:', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)


#Concatenating lists using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


#List slicing (hint:up to but not including)
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])

print(t[:])

#List Methods
x = list()
print(type(x))

print(dir(x))


#Creating a new empty list & assign values
stuff = list()
stuff.append('book')
stuff.append('99')
stuff.append('cookie')
print(stuff)

#Is smth in a List
some = [1, 9, 21, 10, 16]
print(9 in some)

print(15 in some)

print(20 not in some)


#Lists are in Order
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[1])



#Built-in Functions and Lists
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))

print(max(nums))

print(min(nums))

print(sum(nums))

print(sum(nums)/len(nums))


numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)


#Strings and Lists...SPLIT
abc = 'With three words'
stuff = abc.split()
print(stuff)

print(len(stuff))

print(stuff[0])


#Split
line = 'A lot          of spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)

thing = line.split(';')
print(thing)
print(len(thing))

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])

fhand = open('mbox-short.txt')
for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    print(email)
    pieces = email.split('@')
    print(pieces[1])


#Exercise 8.1
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])