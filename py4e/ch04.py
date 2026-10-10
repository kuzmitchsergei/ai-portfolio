
#Stored and reused steps
def thing() :
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()

#Type conversions
print (float(99) / 100)

i = 42
print(type(i))

f = float(i)
print(f)

type(f)

print(1 + 2 * float(3) / 4 - 5)


#String conversion
sval = '123'
print(type(sval))

ival = int(sval)
print(type(ival))
print(ival + 1)


#Invoking the function
x = 5
print('Hello')

def print_lyrics() :
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()
x = x + 2
print(x)


#Parameters
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('es')
greet('fr')
greet('en')


#return Values
def greet():
    return "Hello"
print(greet(), "Glenn")
print(greet(), "Sally")

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')
print(greet('en'), 'Glenn')


#Multiple Parameters
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)


#Exercise 4.6
def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else: 
        pay = 40 * rate + (hours - 40) * 1.5 * rate
    return pay
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except ValueError:
    print('Error, please enter numeric input')
    quit()
pay = computepay(hours, rate)
print('Pay', pay)