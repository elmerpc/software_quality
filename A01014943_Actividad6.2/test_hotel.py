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
        self.hotel = Hotel("Fiesta", "123 Main St", list(range(101, 111)))
        # Mocked JSON file with hotel information to avoid reading from a file.
        self.hotel_information = """
               {
                    "name": "Fiesta", 
                    "address": "123 Main St.", 
                    "rooms": [103, 104, 105, 106, 107, 108, 109, 110], 
                    "reservations": 
                        [
                            {
                                "id": 1, 
                                "customer": "John Doe", 
                                "hotel": "Fiesta", 
                                "room_number": 101, 
                                "start_date": "2022-01-01", 
                                "end_date": "2022-02-15"}]}"""

    def test_create_hotel(self):
        """ Test case 1: Create a hotel with default values."""
        self.assertEqual(self.hotel.name, "Fiesta")
        self.assertEqual(self.hotel.address, "123 Main St")
        self.assertEqual(self.hotel.rooms, list(range(101, 111)))
        self.assertEqual(self.hotel.reservations, [])
        self.assertEqual(self.hotel.filename, "hotel_Fiesta_data.json")

    def test_save_data(self):
        """ Test case 1: Save hotel data to a JSON file."""
        with patch('builtins.open', create=False) as mock_json_file:
            self.hotel.save_data()
            mock_json_file.assert_called_once_with('hotel_Fiesta_data.json', 'w', encoding='utf-8')

    def test_load_data(self):
        """ Test case 1: Load hotel data from a JSON file."""
        # Mock the open function to avoid reading from a file.
        with patch('builtins.open', mock_open(read_data=self.hotel_information), create=True):
            hotel = Hotel("Fiesta","123 Main St.")
            loaded_hotel = hotel.load_data()
            self.assertEqual(loaded_hotel.name, "Fiesta")
            self.assertEqual(loaded_hotel.address, "123 Main St.")
            self.assertEqual(loaded_hotel.rooms, [103, 104, 105, 106, 107, 108, 109, 110])
            self.assertEqual(loaded_hotel.reservations, [{"id": 1, "customer": "John Doe", "hotel": "Fiesta", "room_number": 101, "start_date": "2022-01-01", "end_date": "2022-02-15"}])

    def test_display_information(self):
        """ Test case 1: Display hotel information."""
        output = f"Hotel Name: Fiesta\nAddress: 123 Main St\nNumber of Rooms: 10\nAvailable Rooms: {list(range(101, 111))}\nNumber of Reservations: 0\n"
        self.assertEqual(self.hotel.display_information(), output)

    def test_modify_information(self):
        """ Test case 1: Modify hotel information."""
        with patch('builtins.open', mock_open(read_data=self.hotel_information), create=True):
            self.hotel.modify_information(name="Grand Fiesta", address="456 Elm St")

    def test_verify_room_availability(self):
        """ Verify room availability."""
        # Test case 1: Room is available
        with patch('builtins.open', mock_open(read_data=self.hotel_information), create=True):
            self.assertTrue(self.hotel.verify_room_availability(102, '2021-10-01', '2021-10-15'))

        # Test case 2: Room is not available
        with patch('builtins.open', mock_open(read_data=self.hotel_information), create=True):
            self.assertFalse(self.hotel.verify_room_availability(101, '2022-01-01', '2022-02-15'))

        # Test case 3: No reservations file found
        with patch('builtins.open', side_effect=FileNotFoundError):
            self.assertTrue(self.hotel.verify_room_availability(101, '2021-10-01', '2021-10-15'))

    def test_reserve_room(self):
        """ Test reserving a room."""
        # Test case 1: Reserve a room.
        with patch('builtins.open', mock_open(read_data=self.hotel_information), create=True):
            self.hotel.reserve_room(102, "John Doe", "2021-10-01", "2021-10-15")

            self.assertEqual(self.hotel.reservations, [{"id": 2, "customer": "John Doe", "hotel": "Fiesta", "room_number": 102, "start_date": "2021-10-01", "end_date": "2021-10-15"}])

        # Test case 2: Room is not available.
        with patch('builtins.open', mock_open(read_data=self.hotel_information), create=True):
            self.hotel.reserve_room(102, "John Doe", "2021-10-01", "2021-10-15")

            self.assertEqual(self.hotel.reservations, [{"id": 2, "customer": "John Doe", "hotel": "Fiesta", "room_number": 102, "start_date": "2021-10-01", "end_date": "2021-10-15"}])

    def test_cancel_reservation(self):
        """ Test canceling a reservation."""
        # Test case 1: Cancel a reservation.
        with patch('builtins.open', mock_open(read_data=self.hotel_information), create=False):
            self.hotel.load_data()
            self.assertIn({"id": 1, "customer": "John Doe", "hotel": "Fiesta", "room_number": 101, "start_date": "2022-01-01", "end_date": "2022-02-15"}, self.hotel.reservations)
            self.hotel.cancel_reservation(1)
            self.assertEqual(self.hotel.reservations, [])

        # Test case 2: Reservation ID not found.
        with patch('builtins.open', mock_open(read_data=self.hotel_information), create=False):
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
