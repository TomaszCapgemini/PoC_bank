from transaction import Transaction
import logging


class Client:

    def __init__(self, name, balance):

        self.name = name
        self.id = next(Client.generate_id())
        self._balance = balance
        self._transactions = []
        
    def __repr__(self):
        return f"ID{self.id}, {self.name}: {self._balance}"

    def deposit(self, amount):
        if amount <= 0:
            logging.warning("Cannot deposit negative amount")
            raise Exception  # raise exception

        else:
            saldo = self._balance + amount
            self._transactions.append(Transaction(self.id, self.name, "Deposit", amount))
            self._balance = saldo

    @staticmethod
    def generate_id():
        client_id = 1
        while True:
            yield client_id
            client_id += 1

    def withdraw(self, founds):

        if self._balance < founds:
            logging.warning("Not enough founds")
            raise Exception
        elif founds <= 0:
            logging.warning("Withdraw must be positive")
        else:
            saldo = self._balance - founds
            self._balance = saldo
            self._transactions.append(Transaction(self.id, self.name, "Withdraw", founds))

    @property
    def balance(self):
        return {self._balance}

    @property
    def transaction_list(self):
        return self._transactions

    @transaction_list.setter
    def transaction_list(self, list):
        raise PermissionError("This action is forbidden")


# cl1 = Client("Tom", 1000, [])
# cl2 = Client("Kasia", 500, [])
# cl3 = Client("Rob", 1500, [])
# print(cl1,cl2,cl3, sep='\n')


# cl2 = Client("Kasia", 500)
#
# cl1.get_balance()
# cl2.get_balance()
#
# print(cl2)
#
# cl1.withdraw(1000)
# cl2.withdraw(2000)
#
# cl1.deposit(1000)
# cl2.deposit(1000)
