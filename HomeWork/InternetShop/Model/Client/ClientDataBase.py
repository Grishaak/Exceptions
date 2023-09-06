from seminars_exeptions.HomeWork.InternetShop.Model.Client.Client import Client
from seminars_exeptions.HomeWork.InternetShop.Model.Exceptions.ClientErrors.NotClientFoundError import \
    NotClientFoundError


class ClientDateBase:
    def __init__(self):
        self.date_base = list()

    def get_client(self, client_name):
        for client in self.date_base:
            if client.name == client_name:
                return client
        raise NotClientFoundError("NotClientFoundError", "Клиент не найдет.")

    def add_client(self, client_name):
        client = Client(client_name)
        self.date_base.append(client)
