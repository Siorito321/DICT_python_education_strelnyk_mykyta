import random

fellas = {}


num_of_friends = int(input('type number of your friends (including you)\n'))

if num_of_friends <= 0:
    print('No one is joining the party')
else:
    iterator = 1
    print('Call names of your friends (including you)')
    while iterator <= num_of_friends:
        bro_name = input('>')
        fellas[bro_name] = 0
        iterator += 1
    amount_a = int(input('enter total amount: '))
    amount = amount_a / num_of_friends
    for keys in fellas:
        fellas[keys] = round(amount, 2)

    answer_rand = input('Do you want to use "Who is lucky" feature? Type Yes/No')
    if answer_rand == 'Yes':
        lucky_one = random.choice(range(0, len(fellas)))
        iterator = 0
        for key in fellas.keys():
            if iterator == lucky_one:
                lucky_one_name = key
            iterator += 1
        amount_one = int(amount_a) / (num_of_friends - 1)
        for key in fellas:
            fellas[key] = round(amount_one, 2)
        fellas[lucky_one_name] = 0
        print(f'{lucky_one_name} is the lucky one!')

    else:
        print('Nobody is going to be lucky!')

    print(fellas)
