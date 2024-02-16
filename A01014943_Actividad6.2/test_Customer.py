import unittest
from unittest.mock import mock_open, patch
from customer import Customer

class CustomerTestCase(unittest.TestCase):
    """
    Test case for the Customer class.
    """

    def setUp(self):
        """
        Set up the test case by creating a Customer instance.
        """
        self.customer = Customer("John Doe", "123 Main St")
        self.customer_information = """ {"name": "John Doe", "address": "123 Main St"} """

    def test_display_information(self):
        """ Test case 1: Display customer information."""
        output = "Customer Name: John Doe\nAddress: 123 Main St\n"
        self.assertEqual(self.customer.display_information(), output)

    def test_load_information(self):
        """ Test case 1: Load customer information from a JSON file."""
        with patch('builtins.open', mock_open(read_data=self.customer_information), create=False):
            self.customer.load_information()
            self.assertEqual(self.customer.name, "John Doe")
            self.assertEqual(self.customer.address, "123 Main St")

    def test_save_information(self):
        """ Test case 1: Save customer information to a JSON file."""
        with patch('builtins.open', create=False) as mock_json_file:
            self.customer.save_information()
            mock_json_file.assert_called_once_with('customers.json', 'w', encoding='utf-8')

    def test_modify_information(self):
        """ Test case 1: Modify customer information."""
        with patch('builtins.open', mock_open(read_data=self.customer_information), create=False):
            self.customer.modify_information(name="Jane Smith", address="456 Elm St")
            self.assertEqual(self.customer.name, "Jane Smith")
            self.assertEqual(self.customer.address, "456 Elm St")        

    def test_delete_customer(self):
        """ Test case 1: Delete a customer."""
        with patch('builtins.open', mock_open(), create=True):
            self.customer.delete_customer()
            self.assertEqual(self.customer.name, None)
            self.assertEqual(self.customer.address, None)

if __name__ == '__main__':
    unittest.main()