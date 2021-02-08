class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):

        transactions = [x["description"][:23].ljust(23, ' ') +
                        f'{x["amount"]:.2f}'.rjust(7, ' ') + '\n' for x in self.ledger]
        multilign_string = (f"{self.name.center(30, '*')}\n"
                            f"{''.join(transactions)}"
                            f"Total: {self.balance:.2f}")

        return multilign_string

    def deposit(self, amount, description=str()):
        self.balance += amount
        transaction = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(transaction)

    def withdraw(self, amount, description=str()):
        if self.check_funds(amount):
            self.balance -= amount
            transaction = {
                "amount": -amount,
                "description": description
            }
            self.ledger.append(transaction)
            return True
        else:
            return False

    def get_balance(self):
        return f"{self.balance:.2f}"

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            withdraw_desc = f"Transfer to {destination.name}"
            deposit_desc = f"Transfer from {self.name}"
            self.withdraw(amount, withdraw_desc)
            destination.deposit(amount, deposit_desc)
            return True
        return False

    def check_funds(self, amount):
        if self.balance - amount >= 0:
            return True
        return False


def create_spend_chart():
    multilign_graph = (f"Percentage spent by category")
    return multilign_graph


food = Category('Food')
print(food.get_balance())
print(food.ledger)
food.deposit(1000, 'bitcoin')
print(food.get_balance())
print(food.ledger)
food.withdraw(155, 'bitcoin')
car = Category('Car')
print(food.get_balance())
food.transfer(100, car)
print(food.get_balance())
print(food.ledger)
print(car.get_balance())
print(car.ledger)
print(food)
