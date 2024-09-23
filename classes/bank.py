from classes.client import Client


class Bank:

    def __init__(self):

        self._clients = []

    def __repr__(self):
        return f"{self._clients}"

    @property
    def clients(self):
        return self._clients

    def add_customer(self, client):
        if not isinstance(client, Client):
            print("Musisz podać instancję Klienta")
        else:
            self._clients.append(client)

    def all_clients_balance(self):

        for client in self._clients:
            print(f"Balance for {client.name} is {client.balance}") # Bez splita jak poprawię

