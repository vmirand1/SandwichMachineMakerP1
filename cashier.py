class Cashier:
    def __init__(self):
        pass

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
