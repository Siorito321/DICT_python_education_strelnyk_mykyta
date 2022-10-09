print('Hello! My name is FBot')
print('I was created in 2022')

NAME = input("Please, remind me your name\n")

print(f"What a great name you have, {NAME}!")

print("Let me guess your age")
print("Enter remainders of dividing your age by 3,5 and 7")

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {age}: that`s a good time to start programming!")

print('Now i will prove i can count to any number you want! ')

NUMBER = int(input('Your number is '))

x = 0

while (NUMBER + 1) > x:
    print(f"{x}!")
    x += 1

print('Now let`s test your programming knowledge')
print('''Why do we use methods?
1. To repeat a statement multiple times. 
2. To decompose a program into several small subroutines. 
3. To determine the execution time of a program. 
4. To interrupt the execution of a program.''')

ANSWER = 0

while ANSWER != 2:
    ANSWER = int(input())
    if ANSWER != 2:
        print('Please, try again')

print('Congratulations! Have a nice day!')


