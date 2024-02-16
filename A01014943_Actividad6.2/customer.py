""" Module to represent a customer with a name and address."""
import json

class Customer:
    """ Class to represent a customer with a name and address."""

    def __init__(self, name, address="123 Main St"):
        """
        Initializes a Customer object with the given name and address.

        Args:
            name (str): The name of the customer.
            address (str): The address of the customer.
        """
        self.name = name
        self.address = address

    def load_information(self):
        """
        Loads the customer information from the JSON file.
        """
        try:
            with open('customers.json', "r",encoding='utf-8') as file:
                data = json.load(file)
                self.name = data.get("name", self.name)
                self.address = data.get("address", self.address)
        except FileNotFoundError:
            pass

    def save_information(self):
        """
        Saves the customer information to the JSON file.
        """
        data = {
            "name": self.name,
            "address": self.address
        }
        with open('customers.json', "w",encoding='utf-8') as file:
            json.dump(data, file)

    def display_information(self):
        """
        Displays the information of the customer.
        """
        information = f"Customer Name: {self.name}\n"
        information += f"Address: {self.address}\n"
        return information

    def modify_information(self, name=None, address=None):
        """
        Modifies the information of the customer.

        Args:
            name (str, optional): The new name of the customer. Defaults to None.
            address (str, optional): The new address of the customer. Defaults to None.
        """
        if name:
            self.name = name
        if address:
            self.address = address
        self.save_information()

    def delete_customer(self):
        """
        Deletes the customer by setting the name and address to None.
        """
        self.name = None
        self.address = None
        self.save_information()
