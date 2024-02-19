"""Test for Customer Class"""

import unittest
import os
from Customer import customer


class TestCustomer(unittest.TestCase):
    """Test methods of Customer"""

    name = "Jorge Arce"
    clt_expected = {
        'name': name
    }

    def test_constructor(self):
        """Test for contructor method"""
        clt = customer.Customer(TestCustomer.name)
        self.assertEqual(vars(clt), TestCustomer.clt_expected)

    def test_to_file(self):
        """
        Test for to file method, using the file originated in test_contructor
        """
        self.assertTrue(os.path.isfile(f"customer_{TestCustomer.name}.json"))

    def test_delete(self):
        """Test for delete a customer"""
        # The client dont exist
        print("\nTest: Trying to delete a customer that not exist: Nan")
        customer.Customer.delete_customer("Nan")
        # The client exist & is deleted, creating temporal customer
        print("\nTest: Trying to delete a customer that exist: Ramon")
        temp_name = "Ramon"
        clt = customer.Customer(temp_name)
        customer.Customer.delete_customer(clt.name)
        is_file = os.path.isfile(f"customer_{temp_name}.json")
        self.assertFalse(is_file)

    def test_read(self):
        """Test for read costumer from file using the file created in constructor method & to dict method""" # noqa
        # Client exist
        clt = customer.Customer(TestCustomer.name)
        clt2 = customer.Customer.read_customer(TestCustomer.name)
        self.assertEqual(clt.to_dict(), clt2.to_dict())
        # Client not found
        print("\nTest: Trying to open costumer Veronica")
        rsv3 = customer.Customer.read_customer("Veronica") # noqa
        self.assertEqual(rsv3, None)

    def test_display(self):
        """Test for display methods, only has attribute name"""
        clt = customer.Customer(TestCustomer.name)
        self.assertEqual(clt.get_name(), TestCustomer.name)

    def test_update(self):
        """Test for update methods, only has attribute name"""
        clt = customer.Customer(TestCustomer.name)
        print("\nTest: Updating to Jazmin")
        clt.update_name("Jazmin")
        print("\nTest: Verifying old name is deleted")
        old_file = os.path.isfile(f"customer_{TestCustomer.name}.json")
        new_file = os.path.isfile(f"customer_{clt.get_name()}.json")
        self.assertFalse(old_file)
        self.assertTrue(new_file)


if __name__ == '__main__':
    unittest.main()
