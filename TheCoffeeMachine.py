coffee_machine_on_off = 'on'

initial_condition = {'water': 1000,
                     'milk': 500,
                     'coffee': 100,
                     'money': 0.0
                     }
coffee_dict = {'espresso': {'water': 20, 'milk': 10, 'coffee': 5, 'money': 2.5},
               'latte': {'water': 40, 'milk': 20, 'coffee': 10, 'money': 3.99},
               'cappucino': {'water': 50, 'milk': 25, 'coffee': 15, 'money': 3.5}}

coin_value_dict = {'quarter': 0.25,
                   'dime': 0.10,
                   'nickel': 0.05,
                   'penny': 0.01}

change = 0


def is_enough_resource_available(initial_condition, type):
    if initial_condition['water'] >= coffee_dict[type]['water']:
        if initial_condition['milk'] >= coffee_dict[type]['milk']:
            if initial_condition['coffee'] >= coffee_dict[type]['coffee']:
                return True
            else:
                print("Sorry there is not enough coffee")
        else:
            print('Sorry there is not enough milk')
    else:
        print('Sorry there is not enough water')
    return False


def money_and_check(type):
    no_of_quarters = int(input("enter no of quarter\t"))
    no_of_dime = int(input("enter no of dime\t"))
    no_of_nickels = int(input("enter no of nickel\t"))
    no_of_penny = int(input("enter no of pennies\t"))
    global change
    amount = no_of_quarters * coin_value_dict['quarter'] + no_of_dime * coin_value_dict['dime'] + no_of_nickels * \
             coin_value_dict['nickel'] + no_of_penny * coin_value_dict['penny']
    if amount >= coffee_dict[type]['money']:
        change = amount - coffee_dict[type]['money']
        return True
    return False


def deduction_of_resource(type):
    initial_condition['water'] -= coffee_dict[type]['water']
    initial_condition['milk'] -= coffee_dict[type]['milk']
    initial_condition['coffee'] -= coffee_dict[type]['coffee']


while coffee_machine_on_off == 'on':
    type = input("What would you like? (espresso/latte/cappuccino)    ")

    change = 0
    if type == 'report':
        print(
            f"Water: {initial_condition['water']}ml\nMilk: {initial_condition['milk']}ml\nCoffee: {initial_condition['coffee']}gm\nMoney: ${initial_condition['money']}")
    else:
        should_make_coffee = is_enough_resource_available(initial_condition, type)
        if should_make_coffee:
            is_enough_money = money_and_check(type)
            if is_enough_money:
                initial_condition['money'] += coffee_dict[type]['money']
                if change > 0.0:
                    print(f"Here is the extra change: ${change}")
                    deduction_of_resource(type)
                    print(f"here is your{type}")
            else:
                print("Sorry not enough money. Money refunded.")
    coffee_machine_on_off = input("on-keep machine on\toff-turn off machine")
