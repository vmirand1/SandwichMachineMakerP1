class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")

    def generate_report(self):
        """Generates a report of the current resources."""
        print("\n___Report____")
        for resource, amount in self.machine_resources.items():
            if resource == "cheese":
                unit = "ounce(s)"
            else:
                unit = "slice(s)"
            print(f"{resource.capitalize()}: {amount} {unit}\n")