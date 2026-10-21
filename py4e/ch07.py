#Reading Files

#The newline Character
stuff = 'Hello\nWorld!'
print(stuff)

stuff= 'X\nY'
print(stuff)

len(stuff)


#Exercise 7.1
fh = open('mbox-short.txt')

for line in fh:
    ly = line.rstrip()
    print(ly.upper())