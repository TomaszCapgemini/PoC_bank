from classes.bank import Bank
from classes.client import Client


def main():
    bank = Bank()

    cl1 = Client("Tom", 1000)
    cl2 = Client("Kasia", 500)

    # cl1.transaction_list = []

    bank.add_customer(cl1)
    bank.add_customer(cl2)

    cl1.deposit(1100)
    cl1.withdraw(12000)
    cl2.withdraw(100)
    cl2.deposit(400)

    print(cl1.transaction_list)
    print(cl2.transaction_list)

    print(cl1.balance)
    print(cl2.balance)

    bank.all_clients_balance()

    for client in bank.clients:
        print(client.name)


if __name__ == '__main__':
    main()
