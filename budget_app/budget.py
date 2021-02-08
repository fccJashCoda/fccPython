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
        return self.balance

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
    # get the percentage spent by category rounded down to the nearest ten

    total_spent = 0
    spent_per_category = []
    for category in arr:
        amount_spent = abs(sum(x["amount"] if x["amount"] <
                               0 else 0 for x in category.ledger))
        print(amount_spent)
        total_spent += amount_spent
        spent_per_category.append(amount_spent)

    percentage_spent = []
    for x in spent_per_category:
        percentage_spent.append(
            ((x / total_spent) * 100) - (((x / total_spent) * 100) % 10))

    # if total_spent > 0:
    #     percentage = (amount_spent / total_spent) * 100
    # else:
    #     percentage = 0
    # percentage_spent.append(int(percentage - (percentage % 10)))
    # for category in arr:
    #     amount_spent = abs(sum(x["amount"] if x["amount"] <
    #                            0 else 0 for x in category.ledger))
    #     gross_sum = sum(x["amount"] if x["amount"] >
    #                     0 else 0 for x in category.ledger)

    #     if gross_sum > 0:
    #         percentage = (amount_spent / gross_sum) * 100
    #     else:
    #         percentage = 0
    #     percentage_spent.append(int(percentage - (percentage % 10)))
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
        y_axis += ' \n'
        graph_lines.append(y_axis)

    # print the separator (should end 2 bars after the last name line)
    separator = '-'.rjust(5, ' ') + '---' * len(arr) + '\n'
    # print the category names
    min_length = max([len(item.name) for item in arr])

    name_lines = []
    for n in range(min_length):
        row = str()
        for category in arr:
            if not len(row):
                if n < len(category.name):
                    row += category.name[n].rjust(2, ' ')
                else:
                    row += ' ' * 2
            else:
                if n < len(category.name):
                    row += category.name[n].rjust(3, ' ')
                else:
                    row += ' ' * 3
        row += '\n'
        row = row.rjust(len(row) + 4, ' ')
        name_lines.append(row)

    # print(min_length)
    multilign_graph = (f"Percentage spent by category\n"
                       f"{str().join(graph_lines)}"
                       f"{separator}"
                       f"{str().join(name_lines)}")

    return multilign_graph
