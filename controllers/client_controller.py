# /controllers/client_controller.py

from models.client import Client

class ClientController:

    @staticmethod
    def add_client(name, email, phone, address):
        """
        Add a new client to the database

        :param name: str
        :param email: str
        :param phone: str
        :param address: str
        
        :returns: Client
        """
        try:
            client = Client(name, email, phone, address)
            client_id = client.save()
            return client_id
        except Exception as e:
            raise e
    
    @staticmethod
    def get_clients():
        """
        Get all clients from the database

        :returns: list
        """
        return Client.select_all()
    
    @staticmethod
    def get_client(select_type, value):
        """
        Get a client from the database

        :param
            select_type: str
            value: int

        :returns: Client
        """

        match select_type:
            case "id":
                return Client.select_by_id(value)
            case "name":
                return Client.select_by_name(value)
            case "creation_date":
                return Client.select_by_creation_date(value)
            case "last_update":
                return Client.select_by_last_update(value)
            case _:
                raise ValueError("Select type not found")
    
    @staticmethod
    def search_client(search_option, search_input):
        """
        Search for clients in the database

        :params
            search_options: list
            search_input: str

        :returns: list
        """

        if not search_input:
            raise ValueError("Search input cannot be empty")

        match search_option:
            case "Name":
                return Client.select_by_partial_name(search_input)
            case "Email":
                return Client.select_by_partial_email(search_input)
            case "Phone":
                return Client.select_by_partial_phone(search_input)
            case "Address":
                return Client.select_by_partial_address(search_input)
            case "Creation Date":
                return Client.select_by_creation_date(search_input)
            case "Last Update":
                return Client.select_by_last_update(search_input)
            case _:
                raise ValueError("Search option not found")
            
    @staticmethod
    def edit_client(client_data):
        """
        Edit a client in the database

        :param name: str
        :param email: str
        :param phone: str
        :param address: str

        :returns: Client id
        """
        try:
            Client.update(client_data)
        except Exception as e:    
            raise e
    
    @staticmethod
    def delete_client(client_id):
        """
        Delete a client from the database
        :param client_id: int
        """
        try:
            Client.delete(client_id)
        except Exception as e:
            raise e