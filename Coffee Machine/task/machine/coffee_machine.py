class CoffeeMachine():
    money = 550
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9

    def display(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.coffee_beans))
        print("{} of disposable cups".format(self.disposable_cups))
        print("{} of money".format(self.money))

    def buy(self):
        user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if user_input == "1":
            if self.water >= 250 and self.coffee_beans >= 16 and self.disposable_cups >= 1:
                self.water -= 250
                self.coffee_beans -= 16
                self.disposable_cups -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!")
            elif self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")
        elif user_input == "2":
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.disposable_cups >= 1:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.disposable_cups -= 1
                self.money += 7
                print("I have enough resources, making you a coffee!")
            elif self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")
        elif user_input == "3":
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.disposable_cups >= 1:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.disposable_cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")
            elif self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")
        elif user_input == "back":
            return

    def refill(self):
        self.water += int(input("Write how many ml of water you want to add:"))
        self.milk += int(input("Write how many ml of milk you want to add:"))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:"))
        self.disposable_cups += int(input("Write how many disposable coffee cups you want to add:"))
        
    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0
    
    def start(self):
        while True:
            user_input = input("Write action (buy, fill, take, remaining, exit):")
            if user_input == "buy":
                self.buy()
            elif user_input == "fill":
                self.refill()
            elif user_input == "take":
                self.take()
            elif user_input == "remaining":
                self.display()
            elif user_input == "exit":
                break

cm = CoffeeMachine()
cm.start()