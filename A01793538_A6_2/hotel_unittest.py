"""Test for Hotel Class"""

import unittest
import os
from Hotel import hotel
from Reservation import reservation
from Customer import customer


class TestHotel(unittest.TestCase):
    """Test methods of Hotel"""

    # Data for hotel to test
    name = "Konpeki"
    location = "Night City"
    price = 250
    q_room = 10

    hotel_demo = hotel.Hotel(name, location, q_room, price)

    def test_constructor(self):
        """Test for contructor method"""
        ht = hotel.Hotel(TestHotel.name, TestHotel.location, TestHotel.q_room, TestHotel.price) # noqa
        self.assertEqual(ht.to_dict(), TestHotel.hotel_demo.to_dict())
        self.assertEqual(ht.name, TestHotel.name)
        self.assertEqual(ht.location, TestHotel.location)

        # Creating a hotel with invalid data, must return None values
        ht2 = hotel.Hotel("Brisas", "Guadalajara", 20, -250)
        self.assertEqual(ht2.name, None)
        self.assertEqual(ht2.location, None)
        self.assertEqual(ht2.rooms, None)

    def test_read_hotel(self):
        """
        Test for read from file method

        Data of hotel:
        name = "Pacifica"
        location = "California"
        price per room = 550
        rooms = 20
        """
        helper = hotel.Hotel("Pacifica", "California", 20, 550)
        helper.save_to_file()
        ht = hotel.Hotel.read_hotel("Pacifica")
        self.assertEqual(ht.name, helper.name)
        self.assertEqual(ht.location, helper.location)
        self.assertEqual(len(ht.rooms), len(helper.rooms))
        self.assertEqual(ht.price, 550)

    def test_delete(self):
        """Test for delete an hotel"""
        # The hoetl dont exist
        print("\nTest: Trying to delete a customer that not exist: Picasso")
        hotel.Hotel.delete_hotel("Picasso")
        # The hotel exist & is deleted, creating temporal hotel
        print("\nTest: Trying to delete a hotel that exist: Royal")
        ht = hotel.Hotel("Royal", "Roma", 100, 1000) # noqa
        hotel.Hotel.delete_hotel("Royal")
        is_file = os.path.isfile("Royal_data.json")
        self.assertFalse(is_file)

    def test_reserv_room(self):
        """Test for reserv room method"""
        ht = hotel.Hotel("Dreams", "California", 10, 100)
        clt1 = customer.Customer("Scarlett Johanson")
        rsv1 = reservation.Reservation(clt1, ht, 1)
        print("\nTest: Trying to reserve a room that is available")
        ht.reserve_room(rsv1)
        self.assertEqual(ht.rooms[0].reserv.client.name, "Scarlett Johanson")
        self.assertEqual(ht.rooms[0].reserv.room_id, 1)

        print("\nTest: Trying to reserve a room that is occuped")
        clt2 = customer.Customer("Bradd Pit")
        rsv2 = reservation.Reservation(clt2, ht, 1)
        ht.reserve_room(rsv2)

        print("\nTest: Trying to reserve a invalid room -110")
        rsv2 = reservation.Reservation(clt2, ht, -110)
        ht.reserve_room(rsv2)

    def test_cancel_reserve(self):
        """Test for cancel reservation method"""
        ht = hotel.Hotel("Mamba", "California", 10, 100)
        clt = customer.Customer("Scarlett Johanson")
        rsv = reservation.Reservation(clt, ht, 1)
        ht.reserve_room(rsv)
        print("\nTest: Trying to cancel a reserv")
        ht.cancel_reserve(rsv)
        self.assertEqual(ht.rooms[0].reserv, None)

        print("\nTest: Trying to cancel a room available")
        ht.cancel_reserve(rsv)
        self.assertEqual(ht.rooms[0].available, True)

        print("\nTest: Trying to cancel a room from a different client")
        ht.reserve_room(rsv)
        clt1 = customer.Customer("Ezra Miller")
        rsv1 = reservation.Reservation(clt1, ht, 1)
        ht.cancel_reserve(rsv1)
        self.assertNotEqual(ht.rooms[0].reserv.client.name, clt1.name)

    def test_getters(self):
        """Test for all getters"""
        ht = hotel.Hotel("The black", "Uganda", 30, 500)
        self.assertEqual(ht.get_name(), "The black")
        self.assertEqual(ht.get_location(), "Uganda")
        self.assertEqual(ht.get_price(), 500)

    def test_modify(self):
        """Test for modify information"""
        ht = hotel.Hotel("Pink", "France", 40, 700)
        ht.modify_information(new_name="Rose")
        self.assertEqual(ht.get_name(), "Rose")
        ht.modify_information(new_location="Italy")
        self.assertEqual(ht.get_location(), "Italy")
        ht.modify_information(new_price=1500)
        self.assertEqual(ht.get_price(), 1500)
        # Trying to modify with invalid data
        ht.modify_information(new_price=-234)
        self.assertNotEqual(ht.get_price(), -234)


if __name__ == '__main__':
    unittest.main()
