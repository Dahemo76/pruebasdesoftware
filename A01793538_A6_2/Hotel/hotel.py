"""
Class Hotel representation
"""

import json
import os
from Room import room
from Reservation import reservation


class Hotel:
    """Hotel representation"""

    def __init__(self, name=None, location=None, q_room=None, price=None):
        """
        Hotel object with a name, location & rooms.
        """
        if name:
            if price > 0 and q_room > 0:
                self.name = name
                self.location = location
                self.price = price
                self.rooms = []
                for x in range(q_room):
                    self.rooms.append(room.Room(f"H{x+1}"))
                self.save_to_file()
            else:
                print("Invalid data")
                self.name = None
                self.location = None
                self.rooms = None
        else:
            self.name = None
            self.location = None
            self.rooms = None

    def to_dict(self):
        """Return hotel in dict form"""
        return {
            'name': self.name,
            'location': self.location,
            'price': self.price,
            'rooms': [room.to_dict() for room in self.rooms]
        }

    @staticmethod
    def read_hotel(name):
        """Create a reserv from json file"""
        f_name = f"{name}_data.json"
        ht = Hotel()
        try:
            with open(f_name, "r", encoding="utf-8")as file:
                data = json.load(file)
            location = data['location']
            price = data['price']
            rooms = []
            for rm in data['rooms']:
                rooms.append(room.Room.from_dict(rm))
            ht.name = name
            ht.location = location
            ht.price = price
            ht.rooms = rooms
        except FileNotFoundError:
            print(f"{f_name} no exist")
        return ht

    def save_to_file(self):
        """Saves hotel data to a file."""
        data = {
            'name': self.name,
            'location': self.location,
            'price': self.price,
            'rooms': [room.to_dict() for room in self.rooms]
        }
        with open(self.name + "_data.json", 'w', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def delete_hotel(hotel_name):
        """Deletes hotel data file."""
        try:
            os.remove(f"{hotel_name}_data.json")
            print(f"{hotel_name} deleted")
        except FileNotFoundError:
            print(f"Hotel {hotel_name} not exist")

    def reserve_room(self, rsv: reservation):
        """Reserve a room for a client"""
        rm_index = rsv.room_id - 1
        name = rsv.client.get_name()
        if 0 < rsv.room_id < len(self.rooms):
            status = self.rooms[rm_index].is_available()
            if status:
                self.rooms[rm_index].reserv = rsv
                self.rooms[rm_index].not_available()
                print(f"\nRoom H{rsv.room_id} reserved for {name}")
                self.save_to_file()
            else:
                n = self.rooms[rm_index].reserv.client.name
                print(f"\nRoom is already occuped by {n}")
        else:
            print("Invalid Room")

    def cancel_reserve(self, rsv: reservation):
        """Cancel a reservation"""
        rm_index = rsv.room_id - 1
        if 0 < rsv.room_id < len(self.rooms):
            available = self.rooms[rm_index].is_available()
            name = rsv.client.get_name()
            if available:
                print("The room is not reserved")
            elif not available and self.rooms[rm_index].reserv.client.get_name() != name: # noqa
                print(f"{name} not reserve the room")
            else:
                self.rooms[rm_index].make_available()
                self.save_to_file()
        else:
            print("Invalid Room")

    def get_name(self):
        """Returns hotel information as a string."""
        return self.name

    def get_location(self):
        """Returns hotel information as a string."""
        return self.location

    def get_price(self):
        """Return price per room"""
        return self.price

    def modify_information(self, new_name=None, new_location=None, new_price=None): # noqa
        """Modifies hotel information and updates the file."""
        if new_name:
            self.name = new_name
        if new_location:
            self.location = new_location
        if new_price and new_price > 0:
            self.price = new_price
        self.save_to_file()
