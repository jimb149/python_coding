print("Hello world")
vary23_revised = 1
print(vary23_revised)
# lambda = 1  certain words like this cannot be written as a commond or var name
# how to name our variables in python --> comment
a = 3
print(type(a))
#bc no deciminal points the output calls this 'int' instead of 'float'
b = 1.2
print(type(b))   
c = 'a'
d = 'abc'
# double and single quotes are identical for defining string text
print(d)

# in interactive window can write float(a) then str(a) and you now made a a string variable

#int(b) to round, then float(int(bb)) to make it a deciminal again 
#cannot turn a string variable into a number
#doing these commands in the interactive window does not save or override the interactive code but let's us experiment

#Fundamental tuypes of variables
#integers, float, boolean, complex numbers

i = True
j = False 
# these are the boolean variables. it is the same as factor variabnels in stata (1 is true, 0 is false)

# we can do algebra in the interactive window and permanently with the code in boolean

# floor division, divides then rounds to nearest whole integer 3.0 // 2.0
# 2**3 is 2 to the power of 3, do not use the ^ command 
#single division sign always gives float regardless of result
# command --> not False outputs True because of Boolean variable 
print(i+j)
print(i*j)

# Operators for comparison 

x = 2
y = 2
y = 3
z = 3

x > y 
# now it has outputs was to weahtehr it is true or false
b == c
# checks if b is the same as c and provides an answer 

y is z 

# strings
s = 'Hello Dumbledore'

# print(s) shows the text and len(s) shows the number of characters

print(s.replace('Dumbledore', 'Snape'))

#s[0:5] shows the characters 0 to 5, with 0 being the first text character and it not including the final cut off paramenter
#s[-6:] prints the final six characters of the text 

# s[::2] print every second character

s2 = 'Hello Albus Severus'
s2.split(' ')
# this split it into three parts with the space as the separator but anything could be a separator

print('Hello \n World')

# \n means start a new line
#print('Hello \\n World') --> this ignores the next command line 

# 'Monty' + 'Python'
# ' '.join(['Monty','Pyton']) --> joins these two together 

print("The outcome of interest is", a)
# print("The outcome of interest is %.2f", a) --> code is currently wrong but the professor will update us on it 


