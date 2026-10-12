#Loops & Iterations

#Repeated Steps
n = 5
while n > 0:
    print(n)
    n= n - 1
print('Blastoff')
print(n)

#Breaking out of a Loop
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')

#Finishing an Iteration with continue
while True:
    line = input ('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')


#Definite Loops
#A simple Definite Loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')

#A Definitive Loop with Strings
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')


#Smart Loops
#Looping through a set
print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')


#Finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)


#Counting in a Loop
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)


#Summing in a Loop
zork = 0
print('Before, zork')
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)


#Finding the average in a Loop
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)


#Filtering in a Loop
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number', value)
print('After')


#Search using Boolean Variable
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)


#how to find the smallest value
smallest_so_far = 100
print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After', smallest_so_far)


smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)


#Exercise 5.1
count = 0
total = 0
while True:
    line = input('>')
    if line == 'done':
        break
    try:
        value = float(line)
    except ValueError:
        print('Invalid Input')
        continue
    count = count + 1
    total = total + value

print(total, count, total / count)
