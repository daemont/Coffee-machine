# Write your code here


class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups_remained = 9
        self.money = 550
        self.state = "choosing an action"

    def action(self, uinput):
        if self.state == "choosing a product":
            if uinput == 1:
                if self.water < 250:
                    print("Sorry, not enough water!")
                elif self.beans < 16:
                    print("Sorry, not enough beans!")
                elif self.cups_remained < 1:
                    print("Sorry, not enough cups!")
                else:
                    self.water = self.water - 250
                    self.beans = self.beans - 16
                    self.money = self.money + 4
                    self.cups_remained = self.cups_remained - 1
                    print("I have enough resources, making you a coffee!")
            elif uinput == 2:
                if self.water < 350:
                    print("Sorry, not enough water!")
                elif self.milk < 75:
                    print("Sorry, not enough milk!")
                elif self.beans < 20:
                    print("Sorry, not enough beans!")
                elif self.cups_remained < 1:
                    print("Sorry, not enough cups!")
                else:
                    self.water = self.water - 350
                    self.milk = self.milk - 75
                    self.beans = self.beans - 20
                    self.cups_remained = self.cups_remained - 1
                    self.money = self.money + 7
                    print("I have enough resources, making you a coffee!")
            elif uinput == 3:
                if self.water < 200:
                    print("Sorry, not enough water!")
                elif self.milk < 100:
                    print("Sorry, not enough milk!")
                elif self.beans < 12:
                    print("Sorry, not enough beans!")
                elif self.cups_remained < 1:
                    print("Sorry, not enough cups!")
                else:
                    self.water = self.water - 200
                    self.milk = self.milk - 100
                    self.beans = self.beans - 12
                    self.cups_remained = self.cups_remained - 1
                    self.money = self.money + 6
                    print("I have enough resources, making you a coffee!")
            elif uinput == "back":
                return
            else:
                print("Try again!")
        elif self.state == "fill water":
            self.water = self.water + uinput
        elif self.state == "fill milk":
            self.milk = self.milk + uinput
        elif self.state == "fill beans":
            self.beans = self.beans + uinput
        elif self.state == "fill cups":
            self.cups_remained = self.cups_remained + uinput
        elif self.state == "giving money":
            print("I gave you ${}".format(self.money))
            self.money = 0
        elif self.state == "remaining":
            print()
            print("The coffee machine has:")
            print(self.water, " of water")
            print(self.milk, " of milk")
            print(self.beans, " of coffee beans")
            print(self.cups_remained, " of disposable cups")
            print(self.money, " of money")


coffee_machine = CoffeeMachine()

while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "exit":
        break
    elif action == "buy":
        coffee_machine.state = "choosing a product"
        option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back: ")
        if option == "1":
            coffee_machine.action(1)
        elif option == "2":
            coffee_machine.action(2)
        elif option == "3":
            coffee_machine.action(3)
        elif option == "back":
            coffee_machine.action("back")
        else:
            print("Try again!")
    elif action == "fill":
        coffee_machine.state = "fill water"
        coffee_machine.action(int(input("Write how many ml of water do you want to add:")))
        coffee_machine.state = "fill milk"
        coffee_machine.action(int(input("Write how many ml of milk do you want to add:")))
        coffee_machine.state = "fill beans"
        coffee_machine.action(int(input("Write how many grams of coffee beans do you want to add:")))
        coffee_machine.state = "fill cups"
        coffee_machine.action(int(input("Write how many disposable"
                                        " cups of coffee do you want to add:")))
    elif action == "take":
        coffee_machine.state = "giving money"
        coffee_machine.action(1)
    elif action == "remaining":
        coffee_machine.state = "remaining"
        coffee_machine.action(1)

    else:
        print("No such action!")
