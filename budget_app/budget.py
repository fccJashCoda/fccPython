class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description):
        self.balance += amount
        payload = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(payload)

    def withdraw(self, amount, description):
        pass

    def get_balance(self):
        pass

    def transfer(self, amount, destination):
        pass

    def check_funds(self, amount):
        pass


def create_spend_chart():
    pass
