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