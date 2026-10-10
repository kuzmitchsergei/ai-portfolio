x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')


#Comparison Operators
x = 5
if x == 5 :
    print('Equals 5')
if x > 4 :
    print('Greater than 4')
if x >= 5 :
    print('Greater than or Equals 5')
if x < 6 : print('Less than 6')
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equal 6')


#One-way Decisions
x = 5
print('Before 5')
if x == 5 :
    print('is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6 :
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('Afterwards 6')


#Increase/Maintain after if or for, decrease to indicate end of block
x = 5
if x > 2 :
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5) :
    print(i)
    if i > 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')


#Nested Decisions
x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than 100')
print('All done')


#Two way Decisions with else
x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All done')


#Multi-way
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print ('All done')


#Try Except
astr = 'Hello Bob'
try:
    istr = int(astr)
except: 
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)


#Sample try / except
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print('Nice work')
else:
    print('Not a number')
    

#Exercise 3.1
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate + (hours - 40) * 1.5 * rate
print('Pay:', pay)


#Exercise 3.2
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except ValueError:
    print('Error, please enter numeric input')
    quit()

if hours <= 40:
    pay = hours * rate
else: 
    pay = 40 * rate + (hours - 40) * 1.5 * rate
print('Pay:', pay)
