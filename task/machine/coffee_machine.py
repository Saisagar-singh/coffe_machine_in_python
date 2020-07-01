"""
water = 400
milk = 540
beans = 120
dis_cups = 9
money = 550


def account():
    print(
        "The coffee machine has:\n" + str(water) + " of water\n" + str(milk) + " of milk\n" + str(
            beans) + " of coffee "
                     "beans\n"
        + str(dis_cups) + " of disposable cups\n" + str(money) + " of money")


def buy():
    cmd_buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")
    global water, beans, dis_cups, money, milk
    if cmd_buy == "1":
        if water < 250:
            print("Sorry, not enough water!")
        elif beans < 16:
            print("Sorry, not enough coffee beans!")
        elif dis_cups < 1:
            print("Sorry, not enough water!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 250
            beans -= 16
            dis_cups -= 1
            money += 4
    elif cmd_buy == "2":
        if water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        elif beans < 20:
            print("Sorry, not enough coffee beans!")
        elif dis_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            beans -= 20
            dis_cups -= 1
            money += 7
    elif cmd_buy == "3":
        if water < 200:
            print("Sorry, not enough water!")
        elif milk < 100:
            print("Sorry, not enough milk!")
        elif beans < 12:
            print("Sorry, not enough coffee beans!")
        elif dis_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            beans -= 12
            dis_cups -= 1
            money += 6


def fill():
    global water, milk, beans, dis_cups, money
    water += int(input("Write how many ml of water do you want to add:"))
    milk += int(input("Write how many ml of milk do you want to add:"))
    beans += int(input("Write how many grams of coffee beans do you want to add:"))
    dis_cups += int(input("Write how many disposable cups of coffee do you want to add:"))


def take():
    global money
    print("I gave you $" + str(money))
    money -= money


# account()
while True:
    action = input("Write action(buy, fill, take, remaining, exit):\n> ")
    if action == "exit":
        break
    elif action == "buy":
        buy()

    elif action == "fill":
        fill()

    elif action == "take":
        take()

    elif action == "remaining":
        account()"""


# new code using class
class CoffeeMachine:
    resources = {'water': 400, 'milk': 540, 'coffee beans': 120, 'disposable cups': 9, 'money': 550}
    espresso = {'water': 250, 'milk': 0, 'beans': 16, 'price': 4}
    latte = {'water': 350, 'milk': 75, 'beans': 20, 'price': 7}
    cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'price': 6}
    state = 'choosing an action'

    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining()
            elif action == 'exit':
                break

    def remaining(self):
        print("The coffee machine has:")
        for res, val in self.resources.items():
            print(f"{'$' if res == 'money' else ''}{val} of {res}")

    def take(self):
        print("I gave you $" + str(self.resources['money']))
        self.resources['money'] = 0

    def buy(self):
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee == '1':
            self.coffee_preparing(self.espresso)
        elif coffee == '2':
            self.coffee_preparing(self.latte)
        elif coffee == '3':
            self.coffee_preparing(self.cappuccino)
        elif coffee == 'back':
            return

    def coffee_preparing(self, coffee):
        if coffee['water'] <= self.resources['water'] \
                and coffee['milk'] <= self.resources['milk'] \
                and coffee['beans'] <= self.resources['coffee beans'] \
                and self.resources['disposable cups'] >= 1:
            self.resources['water'] -= coffee['water']
            self.resources['milk'] -= coffee['milk']
            self.resources['coffee beans'] -= coffee['beans']
            self.resources['disposable cups'] -= 1
            self.resources['money'] += coffee['price']
            print('I have enough resources, making you a coffee!')
        else:
            if self.resources['water'] < coffee['water']:
                print('Sorry, not enough water!')
            if self.resources['milk'] < coffee['milk']:
                print('Sorry, not enough milk!')
            if self.resources['coffee beans'] < coffee['beans']:
                print('Sorry, not enough beans!')
            if self.resources['disposable cups'] < 1:
                print('Sorry, not enough cups!')

    def fill(self):
        water_add = int(input("Write how many ml of water do you want to add:"))
        milk_add = int(input("Write how many ml of milk do you want to add:"))
        beans_add = int(input("Write how many grams of coffee beans do you want to add:"))
        cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.resources['water'] += water_add
        self.resources['milk'] += milk_add
        self.resources['coffee beans'] += beans_add
        self.resources['disposable cups'] += cups_add


coffee_machine = CoffeeMachine()
coffee_machine.start()
