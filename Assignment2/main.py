from Assignment2 import data
from SandwichMaker import SandwichMaker
from Assignment2.cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    is_on = True
    # While loop to turn off/on sandwich machine
    while is_on:
        choice = input("Please write one of the options below\nSandwich Sizes:\nsmall\nmedium\nlarge\noff\nreport\n")
        if choice == "off":
            is_on = False
        elif choice == "report":
            sandwich_maker_instance.generate_report()  # Shows current resources
        elif choice in recipes:  # Check if choice is one of recipes dicts
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):  # Check if resources are enough
                coins = cashier_instance.process_coins()  # Get the total coins from process_coins()
                if cashier_instance.transaction_result(coins, sandwich["cost"]):  # Check if coins are enough
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])  # Make the sandwich
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()

