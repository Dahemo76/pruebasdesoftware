"""
Class for create & delete costumers
"""

import json
import os


class Customer:
    """Represents a customer in the hotel reservation system."""

    def __init__(self, name=None):
        """Initializes a Customer object with ID, name, and email."""
        if name:
            self.name = name
            self.save_to_file()
        else:
            self.name = None

    @staticmethod
    def read_customer(name):
        """Create a costumer from json file"""
        f_name = f"customer_{name}.json"
        try:
            with open(f_name, "r", encoding="utf-8")as file:
                data = json.load(file)
            return Customer(data['name'])
        except FileNotFoundError:
            print(f"Client {name} not exist")
            return None

    @staticmethod
    def from_dict(data):
        """Make reservation from dict"""
        clt = Customer()
        clt.name = data['name']
        return clt

    def to_dict(self):
        """Return a dictionary form os customer"""
        return vars(self)

    def save_to_file(self):
        """Saves customer data to a file."""
        data = {
            'name': self.name
        }
        with open(f"customer_{self.name}.json", 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def get_name(self):
        """Return costumer name"""
        return self.name

    @staticmethod
    def delete_customer(name):
        """Deletes a customer's data file."""
        filename = f"customer_{name}.json"
        try:
            os.remove(filename)
            print(f"{name} deleted")
        except FileNotFoundError:
            print(f"{name} not exist")

    def update_name(self, name):
        """Updates customer details and saves to file."""
        Customer.delete_customer(self.name)
        self.name = name
        self.save_to_file()
