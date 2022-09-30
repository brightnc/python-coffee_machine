from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
turn_on = True


while turn_on:
    options = menu.get_items()
    user_pick = input(f"What would you like? ({options}):")
    if user_pick == "off":
        turn_on = False
    elif user_pick == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if coffee_maker.is_resource_sufficient(menu.find_drink(user_pick)) and money_machine.make_payment(menu.find_drink(user_pick).cost):
            coffee_maker.make_coffee(menu.find_drink(user_pick))
