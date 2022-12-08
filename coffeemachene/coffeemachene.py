
class Coffeemachine:
    def __init__(self, n_water, n_milk, n_beans, n_of_cups, n_of_money, espresso, latte, capuccino):
        self.n_water = n_water
        self.n_milk = n_milk
        self.n_beans = n_beans
        self.n_of_cups = n_of_cups
        self.n_of_money = n_of_money
        self.espresso = espresso
        self.latte = latte
        self.capuccino = capuccino

    def fill_f(self):
        self.n_water += int(input('Write how many ml of water you want to add:\n>'))
        self.n_milk += int(input('Write how many ml of milk you want to add:\n>'))
        self.n_beans += int(input('Write how many g of coffee beans you want to add:\n>'))
        self.n_of_cups += int(input('Write how many empty cups you want to add:\n>'))

    def buy_f(self, coffeet):
        wia = [self.n_water, self.n_milk, self.n_beans, self.n_of_cups]

        def is_enough(x, y, z, b):
            if wia[0] < x:
                print('Sorry, not enough water!')
            elif wia[1] < y:
                print('Sorry, not enough milk!')
            elif wia[2] < z:
                print('Sorry, not enough coffee beans!')
            elif wia[3] < b:
                print('Sorry, not enough cups!')
            else:
                return True

        if coffeet == '1':
            if is_enough(250, 0, 16, 4) is True:
                print('I have enough resources, making you a coffee!')
                self.n_water -= 250
                self.n_beans -= 16
                self.n_of_money -= 4
                self.n_of_cups -= 1
        elif coffeet == '2':
            if is_enough(350, 75, 20, 7) is True:
                print('I have enough resources, making you a coffee!')
                self.n_water -= 350
                self.n_milk -= 75
                self.n_beans -= 20
                self.n_of_money -= 7
                self.n_of_cups -= 1
        else:
            if is_enough(200, 100, 12, 6) is True:
                print('I have enough resources, making you a coffee!')
                self.n_water -= 200
                self.n_milk -= 100
                self.n_beans -= 12
                self.n_of_money -= 6
                self.n_of_cups -= 1

    def take_f(self):
        print(f'i gave you {self.n_of_money} money')
        self.n_of_money = 0

    def what_is_lef(self):
        print(f'''The coffee machine has:
        {self.n_water} ml of water
        {self.n_milk} ml of milk
        {self.n_beans} g of coffee beans
        {self.n_of_cups} of disposable cups
        {self.n_of_money} of money
        ''')


cofee_obj = Coffeemachine(400, 540, 120, 9, 550, [250, 0, 16, 4], [350, 75, 20, 7], [200, 100, 12, 6])
user_answer = 'no'

while user_answer != 'exit':
    user_answer = input('Write action (buy, fill, take, remaining, exit):')
    if user_answer == 'buy':
        number_ans = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - return'
                           'to main menu:')
        if number_ans != 'back':
            cofee_obj.buy_f(number_ans)
        cofee_obj.what_is_lef()
    elif user_answer == 'fill':
        cofee_obj.fill_f()
        cofee_obj.what_is_lef()
    elif user_answer == 'take':
        cofee_obj.take_f()
        cofee_obj.what_is_lef()
    elif user_answer == 'remaining':
        cofee_obj.what_is_lef()
    elif user_answer == 'exit':
        break
    else:
        print('undefined answer')

