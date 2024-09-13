### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:
    def __init__(self, machine_resources):
        """Receives resources as input."""
        self.machine_resources = machine_resources  # resources dict

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")

        dollars = float(input("How many dollars? "))
        half_dollars = float(input("How many half-dollars? "))
        quarters = float(input("How many quarters? "))
        nickels = float(input("How many nickels? "))

        customer_coins = (dollars * 1.00) + (half_dollars * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return customer_coins

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that’s not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")

    def generate_report(self):
        print("\n___Report____")
        for resource, amount in self.machine_resources.items():
            if resource == "cheese":
                unit = "pound(s)"
            else:
                unit = "slice(s)"
            print(f"{resource.capitalize()}: {amount} {unit}\n")

def main():
    customer = SandwichMachine(resources)  # instance
    is_on = True
    # While loop to turn off/on sandwich machine
    while is_on:
        choice = input("Please write one of the options below\nSandwich Sizes:\nsmall\nmedium\nlarge\noff\nreport\n")
        if choice == "off":
            is_on = False
        elif choice == "report":
            customer.generate_report()  # Shows current resources
        elif choice in recipes:  # Check if choice is one of recipes dicts
            sandwich = recipes[choice]
            if customer.check_resources(sandwich["ingredients"]):  # Check if resources are enough
                coins = customer.process_coins()  # Get the total coins from process_coins()
                if customer.transaction_result(coins, sandwich["cost"]):  # Check if coins are enough
                    customer.make_sandwich(choice, sandwich["ingredients"])  # Make the sandwich
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
