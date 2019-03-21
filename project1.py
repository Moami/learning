# 27.02.2019
print("Hello, world!")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")
character_name = "Lucy"
character_age = "17"
print("There once was a girl named " + character_name + "...")
print("...and she was " + character_age + " years old.")

        # 28.02.2019
# for sentences and words you need " ... " quotation marks
colour = "silver"
print("Some that glitters may be " + colour + ".\n")

# all the white things are now variables
size = "medium"
cut = "well-tailored"
print("This t-shirt is a size " + size + " and looks very " + cut + ".")

# if I change the value of a variable from here onwards, it will appear as the changed value
cut = "badly tailored"
print("This skirt is " + cut + ".")

# what's in " " is called a string, which is plain text
# another type is a NUMBER, for which you don't need " "
character_age = 50
days_of_exercise = 30.5

# a BOOLEAN value is a TRUE or FALSE value, i.e. binary
isMale = True
# important: it has to be Capitalised! True and False, not true and false
isMale = False
isFemale = True

# backslash_n = \n makes a new paragraph
print("Giraffe \nAcademy")
# putting a backslash in front of something makes it literal, i.e. prints an actual quotation mark
print("Silver \"Fountain")
# to print a backslash, you can just put a backslash in front of it!
print("Golden\\Herd")

# you can define a variable and if you print the variable, its value is output
phrase = "Riders of Rohan"
print(phrase)
slang = "whatever dude"
print(slang)

# this is concatenation (Verkettung) - printing a string and another string
print(phrase + slang)
print(slang + " this too shall pass, man")
# don't forget to always use a + !

# you can access functions by adding a dot to the end of a string
print(phrase.lower())
print(slang.upper())
# so lower = .lower() and upper = .upper()

# check if string is upper or lower case ENTIRELY
# .islower() and .isupper()
print(phrase.islower())
print(phrase.isupper())
print(slang.islower())
print(slang.isupper())

# and now you can combine functions! one after the other will be performed
print(slang.lower().isupper())
print(phrase.upper().isupper())

# let's see if I still recall what I learned in python like half a year ago...
# okay I had to google the : at the end but all else I still knew, that's rad
if phrase.isupper() == True:
    print("hell yeah")

        # 01.03.
# if you want to concatenate a string and a number, you have to make the number a string first
print(str(character_age) + phrase + " go yeet")

# you can make python do calculations for you!
# a decimal number is called a float function
print(phrase * 5)
print(5+3)
print(2 ** 4 + 17)
print(23748444923798%8)
print(18//9)
print(17.5-5)
print("Alice" * int(3.434534))
# so when using int(number) with a float, the resulting integer is rounded

# integers and floats can be modified normally
eggs = 56
spinach = 78.5
print(eggs + spinach)

# variable names can't contain special charas, spaces or begin with a number
# they are also case-sensitive: MORDOR is different from mOrdor
# naming variables inThisWay is called camelcase
# the typical python convention is naming variables in_this_way

        # 02.03.

# print("Hello world!")
# print("What is your name?")
# myName = input()
# print("It is very cool to meet you, " + myName)
# print("The length of your name is:")
# print(len(myName))
# print("What is your age?")
# myAge = input()
# print("You will be " + str(int(myAge) + 1) + " in a year.")
# code only progresses after INPUT is given following the input() command!

# if you put a # in front of code temporarily, it is called commenting out code

# blank lines are simply ignored :)

# input() turns whatever you type into a string
# len() gives you the length of a variable

print(int("17"))

        # 03.03.

tea = "boba and also earl grey"
print(len(tea))
print(tea[1])
# the square brackets give you the symbol/letter of the position
# important: you start indexes on a string with 0, not 1!
print(tea[16])
print(tea[0])

# the index function will tell where a specific character is located
print(tea.index("b"))
print(tea.index("r"))
# it will give you the first position that a chara appears in
print(tea.index("bob"))

# this is a replace function: 1st string is what you want to replace, 2nd with what
print(tea.replace("boba", "matcha"))
print(tea.replace("boba", "white tea"))

# now let's do numbers!

print(float(500))
print(str(48934839.4))
print(int("-80"))
print(float(67))

# the % operator is called mod and gives the remainder of a division
print(10 % 3)
some_number = 15
print(some_number % 7)
print(str(some_number) + " is my favourite number")

# to get the absolute value of a number, use abs
number_two = -2
print(abs(number_two))

# pow function can take 1st number to power of 2nd number
print(pow(6, 2))

# max and min return the smaller or bigger number
print(max(26, 15))
print(min(156, 248, 24))

# the round function rounds a number
print(round(45.6))

# for more functions, you can import external code
from math import *

# floor grabs you the lowest integer, i.e. chops off decimals
print(floor(3.7))
print(floor(87.9))

# ceiling rounds your number up
print(ceil(45.1))

print(sqrt(49))
neg_num = -1

# python has a lot more math functions!

        # 04.03.

# now we learn how to get input!
# this input function tells python: hey we will get a prompt from the user now!
# and we define what we want them to enter
# and then store their input in the variable name

# print("Hello, dear user!")
# print("May I ask for your name?")
# name = input()
# print("Hello " + name + "!")
# print(name.isupper())

# input is only for string variables

print(len(tea))

myAge = "25"
print("You will be " + str(int(myAge)+1) + " in a year.")

        # 05.03

eggs = True
print(eggs)

# you can never use True or False as variable names

# == means equal to
# != means not equal to
# < lesser than
# > greater than
# >= greater or equal to
# <= less or equal to

twothree = 2 == 3
print(twothree)

# >= and <= only work with float or int
# str and int/float cannot be used together

# == means equal to, = means assignment

#       06.03

moths = 66 == 89
print(moths)
# only true+true makes true, any other combo = false
# but: if OR is used, then it's true if EITHER of the booleans is true

# not True = False and not False = True

(4 < 5) and (5 < 6)
(1 == 2) or (2 == 2)

# the above ones only work in python

# computer evaluates left first, then right, then calculates the whole expression down to a single boolean value

# evaluation order: any brackets/math; then: not, and, or

#       07.03.

# flow control starts with a CONDITION and is followed by a CLAUSE
# conditions always evaluate down to True or False
# so if a certain condition is true or false, a certain action follows

#       08.03
# a group of python lines is called a Block
# when an indentation appears, a block begins
# blocks can contain other blocks!
# blocks end when the indentation = 0 or is reduced to a lower indentation for sub-blocks

name = "Mary"
password = "Swordfish"
if name == "Mary":
    print("Hello Mary")
    if password == "swordfish":
        print("Access granted.")
    else:
        print("Wrong password.")

# wrong password! why? I capitalised Swordfish but didn't later on!

# flow control can lead to jumping in code, depending on what you program

# most important statement: THE IF STATEMENT
# means: "if this condition is true, execute the following code"
# needs: 1) if keyword, 2) condition, 3) colon, 4) indented code with if clause

name = "Alice"
if name == "Alice":
    print("The name really is Alice!")

# an else statement if executed if the if statement's condition is FALSE
# has NO condition, is simply a command!

name = "Bob"
if name == "Bob":
    print("He's the real Bob!")
else:
    print("No Bob in this town")

# the ELSEIF statement acts when all OTHER conditions come out FALSE

name = "Monkeybrain"
if name == "Mastermind":
    print("No monkeys in da house")
elif name == "Goodguy":
    print(2 + 2)
else:
    print("Nobody's homee!")

# only 1 or none of the elif clauses will be executed
# so you can't have the same clause twice --> redundant!
# an else statement after the last elif guarantees that THAT clause will be executed

#       09.03.

# the order of elif statements matters, as they are tested in ORDER!

# we can also make a WHILE statement - to LOOP orders!
# consists of the while keyword, condition, colon, indentation, you know the drill

spam = 2
while spam < 5:
    print("Moin moin, meine lads und lasses!")
    spam = spam + 1

# why the + 1? well otherwise we're gonna loop it to fucking infinity
# and infinity is not a good thing to have in code, believe me
# so it loops UNTIL THE VALUE IS REACHED
# the condition is always checked again at the start of each loop
# once it becomes FALSE, it stops and ends!

# name = ""
# while name != "your name":
    # print("Please type a name, you buffoon.")
    # name = input()
# print("Thanks dude")

# to make it easier, you can BREAK out of a while statement
# and if you use "while true", that's always true - infinite loop!!
# you HAVE to break those or you break your fucking program

# while True:
  #  print("Please type a name.")
   # name = input()
    #if name == "your name":
     #   break
# print("Thank you!")

#       10.03.

name = "Franz"
age = 450
if name == "Nina" and age < 100:
    print("Hello, Nina!")
elif name == "Dracula":
    print("Not today, evil man!")
elif age > 100 and age < 450:
    print("Maybe you are Franz...")
else:
    print("You surely are Franz!")

while True:
    print("Who are you?")
    name = input()
    if name == "Percy Jackson":
        print("Hello, Percy Jackson. Where is the lightning bolt?")
    else:
        continue

while True:
    location = input()
    if location == "Hades":
        break
    else:
        continue
print("Very well.")


