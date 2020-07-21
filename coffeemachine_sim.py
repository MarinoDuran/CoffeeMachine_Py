class CoffeeMachine:
    inventory = {"Water": 400, "Milk": 540, "Beans": 120, "Cups": 9, "Money": 550}
    state = "stand_by"
    coffee_type = "none_selected"

    def __init__(self, action):
        self.action = action

    def process_input(self):
        if self.action == "buy":
            CoffeeMachine.state = "buy"
        elif self.action == "take":
            take()
        elif self.action == "fill":
            self.state = "fill"
        elif self.action == "remaining":
            status()
        elif self.action == 'exit':
            exit()
        else:
            print("Invalid entry. Please try again:")
            start_machine()


def reset_state():
    CoffeeMachine.state, CoffeeMachine.coffee_type = "stand_by", "none_selected"


def status():
    current_status = '''
    The coffee machine has: 
    {0} of water.
    {1} of milk.
    {2} of coffee beans.
    {3} of disposable cups
    ${4} of money.
    '''
    print(current_status.format(CoffeeMachine.inventory.get("Water"), CoffeeMachine.inventory.get("Milk"),
                                CoffeeMachine.inventory.get("Beans"), CoffeeMachine.inventory.get("Cups"),
                                CoffeeMachine.inventory.get("Money")))
    reset_state()
    start_machine()


def fill(add_to):
    parts = [int(add_to[0]), int(add_to[1]), int(add_to[2]), int(add_to[3]), 0]
    index = 0
    for item in CoffeeMachine.inventory:
        CoffeeMachine.inventory[item] += parts[index]
        index += 1
    reset_state()


def enough(ingredients):
    enough_item = True
    virtual_machine = CoffeeMachine.inventory.copy()
    index = 0
    for item in virtual_machine:
        virtual_machine[item] += ingredients[index]
        index += 1
    for items in virtual_machine:
        if virtual_machine[items] < 0:
            print(f'Sorry not enough {items}!')
            enough_item = False
    if enough_item:
        print("\nI have enough resources, making you a coffee!")
        reset_state()
    return enough_item


def take():
    print(f"\nI gave you ${CoffeeMachine.inventory.get('Money')}\n")
    CoffeeMachine.inventory["Money"] = 0
    reset_state()
    start_machine()


def make(cafe):
    parts = []
    if cafe == "1":
        parts = [-250, 0, -16, -1, 4]
    elif cafe == "2":
        parts = [-350, -75, -20, -1, 7]
    elif cafe == "3":
        parts = [-200, -100, -12, -1, 6]
    else:
        pass
    if enough(parts):
        index = 0
        for item in CoffeeMachine.inventory:
            CoffeeMachine.inventory[item] += parts[index]
            index += 1


def start_machine():
    prompt = CoffeeMachine(input("\nWrite action (buy, fill, take, remaining, exit): \n"))
    prompt.process_input()
    if prompt.state == "buy":
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        if coffee_type == "back":
            start_machine()
        elif coffee_type == "1" or coffee_type == "2" or coffee_type == "3":
            make(coffee_type)
        else:
            print("Invalid entry. Please try again:")
            start_machine()
    else:
        add = (input("Write how many ml of water do you want to add:"),)
        add += (input("Write how many ml of milk do you want to add:"),)
        add += (input("Write how many grams of coffee beans do you want to add:"),)
        add += (input("Write how many disposable cups of coffee do you want to add:"),)
        try:
            fill(add)
        except:
            print("\nInvalid amount type. Please try again or type back to start from main menu.")
        finally:
            start_machine()
    start_machine()


start_machine()
