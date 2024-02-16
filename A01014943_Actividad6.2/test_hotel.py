""" Test cases for the Hotel class. """
import unittest
from unittest.mock import mock_open,patch
from hotel import Hotel

class HotelTestCase(unittest.TestCase):
    """
    Test case for the Hotel class.
    """

    def setUp(self):
        """
        Set up the test case by creating a Hotel instance and a mocked reservation.
        """
        self.hotel = Hotel("My Hotel", "123 Main St", list(range(101, 111)))
        self.mocked_reservation = """[
            {
                "id": 1,
                "customer": "John Doe",
                "hotel": "My Hotel",
                "room_number": 101,                
                "start_date": "2021-10-01",
                "end_date": "2021-10-15"
            }
        ]"""

    def test_create_hotel(self):
        """ Test case 1: Create a hotel with default values."""
        self.assertEqual(self.hotel.name, "My Hotel")
        self.assertEqual(self.hotel.address, "123 Main St")
        self.assertEqual(self.hotel.rooms, list(range(101, 111)))
        self.assertEqual(self.hotel.reservations, [])

    def test_save_data(self):
        """ Test case 1: Save hotel data to a JSON file."""
        with patch('builtins.open', create=True) as mock_json_file:
            self.hotel.save_data()
            mock_json_file.assert_called_once_with('hotel_My Hotel_data.json', 'w', encoding='utf-8')

    def test_load_data(self):
        """ Test case 1: Load hotel data from a JSON file."""
        self.hotel.load_data() #FIXME this is not loading anything
        self.assertEqual(self.hotel.name, "My Hotel")
        self.assertEqual(self.hotel.address, "123 Main St")
        self.assertEqual(self.hotel.rooms, list(range(101, 111)))
        self.assertEqual(self.hotel.reservations, [])

    def test_load_reservations(self):
        """ Test case 1: Load reservations from a JSON file."""
        with patch('builtins.open', mock_open(read_data='[{"room_number": 101, "hotel": "My Hotel", "customer": "John Doe"}]'), create=True):
            self.hotel.load_reservations()
            self.assertEqual(self.hotel.reservations, [(101, "John Doe")])

    def test_display_information(self):
        """ Test case 1: Display hotel information."""
        output = f"Hotel Name: My Hotel\nAddress: 123 Main St\nNumber of Rooms: 10\nAvailable Rooms: {list(range(101, 111))}\nNumber of Reservations: 0\n"
        self.assertEqual(self.hotel.display_information(), output)

    def test_modify_information(self):
        """ Test case 1: Modify hotel information."""
        self.hotel.modify_information(name="New Hotel", address="456 Elm St")
        self.assertEqual(self.hotel.name, "New Hotel")
        self.assertEqual(self.hotel.address, "456 Elm St")

    def test_verify_room_availability(self):
        """ Verify room availability."""
        # Test case 1: Room is available
        with patch('builtins.open', mock_open(read_data=self.mocked_reservation), create=True):
            self.assertTrue(self.hotel.verify_room_availability(102, '2021-10-01', '2021-10-15'))

        # Test case 2: Room is not available
        with patch('builtins.open', mock_open(read_data=self.mocked_reservation), create=True):
            self.assertFalse(self.hotel.verify_room_availability(101, '2021-10-01', '2021-10-15'))

        # Test case 3: No reservations file found
        with patch('builtins.open', side_effect=FileNotFoundError):
            self.assertTrue(self.hotel.verify_room_availability(101, '2021-10-01', '2021-10-15'))

    def test_reserve_room(self):
        """ Test case 1: Reserve a room."""
        with patch('builtins.open', mock_open(read_data=self.mocked_reservation), create=True):
            self.hotel.reserve_room(102, "John Doe", "2021-10-01", "2021-10-15")

            self.assertEqual(self.hotel.reservations, [(102, "John Doe")])

    def test_cancel_reservation(self):
        """ Test case 1: Cancel a reservation."""
        with patch('builtins.open', mock_open(read_data=self.mocked_reservation), create=True):
            self.hotel.cancel_reservation(1)
            self.assertEqual(self.hotel.reservations, [])

    def test_delete_hotel(self):
        """ Test case 1: Delete a hotel."""
        with patch('builtins.open', mock_open(), create=True):
            self.hotel.delete_hotel()
            self.assertEqual(self.hotel.name, None)
            self.assertEqual(self.hotel.address, None)
            self.assertEqual(self.hotel.rooms, [])
            self.assertEqual(self.hotel.reservations, [])

if __name__ == '__main__':
    unittest.main()
