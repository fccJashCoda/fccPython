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


def create_spend_chart(arr):
    percentage_spent = []
    # get the percentage spent by category rounded down to the nearest ten

    for category in arr:
        amount_spent = abs(sum(x["amount"] if x["amount"] <
                               0 else 0 for x in category.ledger))
        gross_sum = sum(x["amount"] if x["amount"] >
                        0 else 0 for x in category.ledger)

        if gross_sum > 0:
            percentage = (amount_spent / gross_sum) * 100
        else:
            percentage = 0
        percentage_spent.append(int(percentage - (percentage % 10)))
    print(percentage_spent)

    # print out the bar chart
    graph_lines = []
    for row in range(100, -1, -10):
        y_axis = (str(row) + '|').rjust(4, ' ')
        for value in percentage_spent:
            if value >= row:
                if 'o' in y_axis:
                    y_axis += 'o'.rjust(3, ' ')
                else:
                    y_axis += 'o'.rjust(2, ' ')
            else:
                y_axis += ' ' * 3
        y_axis += '  \n'
        graph_lines.append(y_axis)

    # print the separator (should end 2 bars after the last name line)
    separator = '-'.rjust(5, ' ') + '---' * len(arr)
    # print the category names
    for category in arr:
        print(category.name)
    min_length = max([len(item.name) for item in arr])
    # print(min_length)
    multilign_graph = (f"Percentage spent by category\n"
                       f"{str().join(graph_lines)}"
                       f"{separator}")
    print(multilign_graph)

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
vacation = Category('Vacation')
gifts = Category('Gifts')
gifts.deposit(100, 'mouse')
gifts.withdraw(88, 'mouse')

create_spend_chart([food, car, vacation, gifts])
