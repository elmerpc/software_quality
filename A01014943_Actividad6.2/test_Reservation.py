""" Test cases for the Reservation class. """
import unittest
from reservation import Reservation

class ReservationTestCase(unittest.TestCase):
    """
    Test case for the Reservation class.
    """

    def setUp(self):
        """
        Set up the test case by creating a Reservation instance.
        """
        self.reservation = Reservation("John Doe", "Fiesta", 101, "2022-01-01", "2022-02-15")

    def test_to_dict(self):
        """ Test case 1: Convert reservation to dictionary."""
        expected_dict = {
            'id': 1,
            'customer': "John Doe",
            'hotel': "Fiesta",
            'room_number': 101,
            'start_date': "2022-01-01",
            'end_date': "2022-02-15"
        }
        self.assertEqual(self.reservation.to_dict(), expected_dict)

    def test_get_next_id(self):
        """ Test case 2: Get next available ID for a reservation."""
        self.assertEqual(self.reservation.get_next_id(), 1)

    def test_print_reservation_details(self):
        """ Test case 3: Print reservation details."""
        expected_details = "Reservation ID: 1\n"
        expected_details += "Customer: John Doe\n"
        expected_details += "Hotel: Fiesta\n"
        expected_details += "Room Number: 101\n"
        expected_details += "Start Date: 2022-01-01\n"
        expected_details += "End Date: 2022-02-15\n"
        self.assertEqual(self.reservation.print_reservation_details(), expected_details)

if __name__ == '__main__':
    unittest.main()
