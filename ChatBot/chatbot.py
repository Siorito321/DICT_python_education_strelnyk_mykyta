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