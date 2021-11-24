#!/usr/bin/env python3

def greet(bot_name, birth_year):  # Function to greet user...
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():  # Function to input and output user's name...
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():  # Function to guess age using a special formula...
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105  # The special formula...

    print("Your age is " + str(age) + "; that's a good time to start programming!")

def count():  # Function that loops until the user's input...
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():  # Your test function for the multiple choices...
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    choice = int(input())

    if choice == 2:
        print('Wohoo! You nailed it!!!')
    else:
        print("PLease try again")



def end():  # Concluding message...
    print('Congratulations, have a nice day!')

# Invoke the functions...

greet('Chatty', '2021')
remind_name()
guess_age()
count()
test()  
end()
