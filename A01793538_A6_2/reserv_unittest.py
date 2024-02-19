"""Test for Reservation Class"""

import unittest
import os
from Reservation import reservation
from Customer import customer  # A client is needed to create a reservation
from Hotel import hotel  # A hotel is needed to create a reservation


class TestReserv(unittest.TestCase):
    """Test methods of Reservation"""

    name = "Pedro Cruz"
    room = 5
    rsv_expected = {
        'client': {'name': name},
        'hotel': "Konpeki",
        'room_id': room
    }

    ht = hotel.Hotel("Konpeki", "Pacifica Beach", 10)

    def test_constructor(self):
        """Test for contructor method"""
        rsv = reservation.Reservation(customer.Customer(TestReserv.name), TestReserv.ht, TestReserv.room) # noqa # pylint: disable=global-statement
        self.assertEqual(vars(rsv.client), TestReserv.rsv_expected['client'])
        self.assertEqual(rsv.hotel, TestReserv.rsv_expected['hotel'])
        self.assertEqual(rsv.room_id, TestReserv.rsv_expected['room_id'])

    def test_to_file(self):
        """
        Test for to file method, using the file originated in test_contructor
        """
        self.assertTrue(os.path.isfile(f"rsv_Konpeki_{TestReserv.name}.json"))

    def test_read(self):
        """Test for read a reservation from file & to dict method"""
        # Reservation exist
        rsv = reservation.Reservation(customer.Customer(TestReserv.name), TestReserv.ht, TestReserv.room) # noqa 
        rsv2 = reservation.Reservation.read_reservation(customer.Customer(TestReserv.name), TestReserv.ht) # noqa
        self.assertEqual(rsv.to_dict(), rsv2.to_dict())
        # Reservation dont exist
        print("\nTest: Trying to open a reserv (not exist) for Rebecca at Konpeki") # noqa
        rsv3 = reservation.Reservation.read_reservation(customer.Customer("Rebecca"), TestReserv.ht) # noqa
        self.assertEqual(rsv3, None)

    def test_delete(self):
        """Test for delete a reserv"""
        # The reservation dont exist
        print("\nTest: Trying to delete a reserv for Pepe at Konpeki")
        reservation.Reservation.delete_reservation(customer.Customer("Pepe"), TestReserv.ht) # noqa
        # The reservation exist & is deleted
        print("\nTest: Trying to delete a reserv for Pedro Cruz at Konpeki")
        reservation.Reservation.delete_reservation(customer.Customer(TestReserv.name), TestReserv.ht) # noqa
        is_file = os.path.isfile(f"rsv_Konpeki_{TestReserv.name}.json")
        self.assertFalse(is_file)


if __name__ == '__main__':
    unittest.main()
