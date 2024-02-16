"""Module to represent a reservation made by a customer at a hotel."""
import json

class Reservation:
    """
    Represents a reservation made by a customer at a hotel.

    Attributes:
        customer (Customer): The customer making the reservation.
        hotel (Hotel): The hotel where the reservation is made.
        room_number (int): The room number for the reservation.
        ID (int): The ID of the reservation.
        start_date (str): The start date of the reservation.
        end_date (str): The end date of the reservation.
    """

    def __init__(self, customer, hotel, room_number, start_date, end_date):
        self.hotel = hotel
        self.id = self.get_next_id()
        self.customer = customer
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self):
        """ Returns a dictionary representation of the reservation. """
        return {
            'id': self.id,
            'customer': self.customer,
            'hotel': self.hotel,
            'room_number': self.room_number,
            'start_date': self.start_date,
            'end_date': self.end_date
        }

    def get_next_id(self, filename=None):
        """
        Gets the next available ID for a reservation.

        Returns:
            int: The next available ID for a reservation.
        """
        filename = filename if filename else f'hotel_{self.hotel}_data.json'

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                hotel_data = json.load(file)
                reservations = hotel_data.get('reservations', [])
                if reservations:
                    return reservations[-1]['id'] + 1
                else:
                    return 1
        except FileNotFoundError:
            return 1

    def print_reservation_details(self):
        """
        Returns a string with the details of the reservation.

        Returns:
            str: A string with the details of the reservation.
        """
        details = f"Reservation ID: {self.id}\n"
        details += f"Customer: {self.customer}\n"
        details += f"Hotel: {self.hotel}\n"
        details += f"Room Number: {self.room_number}\n"
        details += f"Start Date: {self.start_date}\n"
        details += f"End Date: {self.end_date}\n"
        return details

def create_reservation(customer, hotel, room_number, start_date, end_date):
    """ Creates a reservation and saves it to the JSON file."""
    r = Reservation(customer, hotel, room_number, start_date, end_date)
    #r.save_reservation_json()
    return r
