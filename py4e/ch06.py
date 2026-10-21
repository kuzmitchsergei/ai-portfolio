#Looking inside Strings

fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

#Strings Have Length
fruit = 'banana'
print(len(fruit))

fruit = 'banana'
x = len(fruit)
print(x)


#Looping Through Strings
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)


#Looping and Counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

#Looking deeper into in
for letter in 'banana':
    print(letter)


#Slicing Strings
s = 'Monty Python'
print(s[0:4])

print(s[6:7])

print(s[6:20])

s = 'Monty Python'
print(s[:2])
print(s[8:])
print(s[:])


#String Concatenation
a = 'Hello' 
b = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)


#Using in as a logical Operator
fruit = 'banana'
print('n' in fruit)

print('m' in fruit)

print('nan' in fruit)

if 'a' in fruit:
    print('Found it!')


#String Comparison
word = input('Enter a word: ')
if word == 'banana':
    print('All right, bananas')
if word < 'banana':
    print('Your word,' + word + ', comes before banana')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana')
else:
    print('All right, bananas.')


#String Library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())    


#Making eveyrthing UPPER CASE
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)

www = greet.lower()
print(www)


#Search and Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)

nstr = greet.replace('o','X')
print(nstr)


#Stripping Whitespace
greet = '    Hello Bob   '
print(greet.lstrip())

print(greet.rstrip())

print(greet.strip())


#Prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))

print(line.startswith('p'))


#Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)


#Exercise 6.5
text = 'X-DSPAM-Confidence: 0.8475 '
colonpos = text.find(':')

number = text[colonpos+1 :].strip()


print(number)
print(float(number))
