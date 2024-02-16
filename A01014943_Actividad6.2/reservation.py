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
        self.id = self.get_next_id()
        self.customer = customer
        self.hotel = hotel
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    def get_next_id(self):
        """
        Gets the next available ID for a reservation.

        Returns:
            int: The next available ID for a reservation.
        """
        try:
            with open('reservations.json', 'r', encoding='utf-8') as file:
                reservations = json.load(file)
                if reservations:
                    last_reservation = reservations[-1]
                    return last_reservation['id'] + 1
                return 1
        except FileNotFoundError:
            return 1

    def print_reservation_details(self):
        """
        Prints the details of the reservation.
        """
        print("Reservation Details:")
        print(f"ID: {self.id}")
        print(f"Customer: {self.customer}")
        print(f"Hotel: {self.hotel}")
        print(f"Room Number: {self.room_number}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")

    def save_reservation_json(self):
        """
        Saves the reservation details in a JSON file.
        """
        reservation_data = {
            "id": self.id,
            "customer": self.customer,
            "hotel": self.hotel,
            "room_number": self.room_number,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
        try:
            with open("reservations.json", "r", encoding='utf-8') as file:
                reservations = json.load(file)
        except FileNotFoundError:
            reservations = []

        reservations.append(reservation_data)

        with open("reservations.json", "w", encoding='utf-8') as file:
            json.dump(reservations, file, indent=4)

def create_reservation(customer, hotel, room_number, start_date, end_date):
    """ Creates a reservation and saves it to the JSON file."""
    r = Reservation(customer, hotel, room_number, start_date, end_date)
    r.save_reservation_json()
    return r

def delete_reservation(reservation_id):
    """
    Cancels the reservation by deleting it from the JSON file.
    """
    with open("reservations.json", "r", encoding='utf-8') as file:
        reservations = json.load(file)

    updated_reservations = [reservation for reservation in reservations if reservation['id'] != reservation_id]

    with open("reservations.json", "w", encoding='utf-8') as file:
        print("Reservation deleted successfully.")
        json.dump(updated_reservations, file, indent=4)
