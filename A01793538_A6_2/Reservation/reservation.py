"""Class for create & delete reservation"""

import json
import os
from Customer import customer


class Reservation:
    """Reservation in room at the hotel"""

    def __init__(self, client=None, hotel=None, room_id=None):
        """Initializes a Reservation with necessary details."""

        if client is not None:
            self.client = client
            self.hotel = hotel.name
            self.room_id = room_id
            self.save_to_file()
        else:
            self.client = None
            self.hotel = None
            self.room_id = None

    def save_to_file(self):
        """Saves reservation details to a file."""
        data = {
            'client': vars(self.client),
            'hotel': self.hotel,
            'room_id': self.room_id
        }
        filename = f"rsv_{self.hotel}_{self.client.get_name()}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def delete_reservation(client, hotel):
        """Cancel a room reservation."""
        f_name = f"rsv_{hotel.name}_{client.name}.json"
        try:
            os.remove(f_name)
            print(f"{f_name} is deleted")
        except FileNotFoundError:
            print(f"There's no reservation for {client.name} in {hotel.name}")

    @staticmethod
    def read_reservation(client, hotel):
        """Create a reserv from json file"""
        f_name = f"rsv_{hotel.name}_{client.name}.json"
        try:
            with open(f_name, "r", encoding="utf-8")as file:
                data = json.load(file)
            rsv = Reservation()
            rsv.client = customer.Customer.from_dict(data['client'])
            rsv.hotel = hotel.name
            rsv.room_id = data['room_id']
            return rsv
        except FileNotFoundError:
            print(f"Client {client.name} has no reservations at {hotel.name}")
            return None

    @staticmethod
    def from_dict(data):
        """Make reservation from dict"""
        rsv = Reservation()
        rsv.client = customer.Customer.from_dict(data['client'])
        rsv.hotel = data['hotel']
        rsv.room_id = data['room_id']
        return rsv

    def to_dict(self):
        """To dictionaty method"""
        return {
            'client': vars(self.client),
            'hotel': self.hotel,
            'room_id': self.room_id
        }
