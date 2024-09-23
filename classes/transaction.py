from datetime import datetime, date, timezone


class Transaction:

    def __init__(self, nr_klienta, name, transaction_type, amount):
        self.id = nr_klienta
        self.name = name
        self.type = transaction_type
        self.amount = amount
        self.transaction_date = f" \
                                {str(date.today())}\
                                {str(datetime.now(timezone.utc).strftime('%H:%M:%S'))}\
                                "

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.type}, {self.amount}"

    def __str__(self):
        return f"{self.name} made {self.type} on {self.transaction_date} on a amount of {self.amount}"

    def return_transaction(self):
        return [self.id, self.name, self.type, self.amount, self.transaction_date]

# t = Transaction(1, "TOM", "Deposit", 100)
#
# print(t)
