""" Module to represent a hotel with its name, address, and available rooms. """
import json
from reservation import create_reservation, delete_reservation


class Hotel:
    """
    Represents a hotel with its name, address, and available rooms.

    Attributes:
        name (str): The name of the hotel.
        address (str): The address of the hotel.
        rooms (list): A list of room numbers available in the hotel.
        reservations (list): A list of reservations made in the hotel.
    """

    def __init__(self, name, address, rooms=None):
        """
        Initializes a Hotel object with the given name, address, and rooms.

        Args:
            name (str): The name of the hotel.
            address (str): The address of the hotel.
            rooms (list): A list of room numbers available in the hotel.
        """
        self.name = name
        self.address = address
        self.rooms = list(range(101, 111)) if rooms is None else rooms
        self.reservations = []


    def load_data(self, filename=None):
        """
        Loads hotel data from a JSON file.
        """
        filename = filename if filename else f'hotel_{self.name}_data.json'

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.name = data.get('name', self.name)
                self.address = data.get('address', self.address)
                self.rooms = data.get('rooms', self.rooms)
                reservations = self.load_reservations()
                self.reservations = reservations if reservations else []
                return self
        except FileNotFoundError:
            print("No existing data found. Starting with default values.")

    def load_reservations(self):
        """
        Loads reservations from a JSON file.
        """
        try:
            with open('reservations.json', 'r', encoding='utf-8') as file:
                reservations = json.load(file)
                for reservation in reservations:
                    if reservation['hotel'] == self.name:
                        self.reservations.append((reservation['room_number'], reservation['customer']))
                return reservations
        except FileNotFoundError:
            print("No existing reservations found.")

    def save_data(self):
        """
        Saves hotel data to a JSON file.
        """
        data = {
            'name': self.name,
            'address': self.address,
            'rooms': self.rooms,
            'reservations': self.reservations
        }
        with open(f'hotel_{self.name}_data.json', 'w',encoding='utf-8') as file:
            json.dump(data, file)

    def display_information(self):
        """
        Returns the information of the hotel, including its name, address,
        number of rooms, and number of reservations.

        Returns:
            str: The information of the hotel.
        """
        information = ""
        information += f"Hotel Name: {self.name}\n"
        information += f"Address: {self.address}\n"
        information += f"Number of Rooms: {len(self.rooms)}\n"
        information += f"Available Rooms: {self.rooms}\n"
        information += f"Number of Reservations: {len(self.reservations)}\n"
        return information

    def modify_information(self, name=None, address=None):
        """
        Modifies the information of the hotel, such as its name and address.

        Args:
            name (str, optional): The new name of the hotel. Defaults to None.
            address (str, optional): The new address of the hotel. Defaults to None.
        """
        if name:
            self.name = name
        if address:
            self.address = address
        self.save_data()

    def reserve_room(self, room_number, guest_name, start_date, end_date):
        """
        Reserves a room in the hotel for a guest.

        Args:
            room_number (int): The number of the room to be reserved.
            guest_name (str): The name of the guest.

        Returns:
            None
        """
        if room_number in self.rooms and self.verify_room_availability(room_number, start_date, end_date):
            create_reservation(guest_name, self.name, room_number, start_date, end_date)
            self.reservations.append((room_number, guest_name))
            self.rooms.remove(room_number)
            print(f"Room {room_number} reserved for {guest_name}.")
            self.save_data()
        else:
            print(f"Room {room_number} is not available.")

    def verify_room_availability(self, room_number, start_date, end_date):
        """
        Checks the availability of a room within a specified date range.

        Args:
            room_number (int): The number of the room to check availability for.
            start_date (str): The start date of the date range to check.
            end_date (str): The end date of the date range to check.

        Returns:
            bool: True if the room is available, False otherwise.
        """
        availability = True
        try:
            with open('reservations.json', 'r', encoding='utf-8') as file:
                reservations = json.load(file)
            for reservation in reservations:
                if reservation['room_number'] == room_number and reservation['hotel'] == self.name and reservation['start_date'] < end_date and reservation['end_date'] > start_date:
                    availability = False
        except FileNotFoundError:
            return availability
        return availability

    def cancel_reservation(self, reservation_id):
        """
        Cancels a reservation for a room in the hotel.

        Args:
            room_number (int): The number of the room for which the reservation is to be cancelled.

        Returns:
            None
        """
        for reservation in self.reservations:
            print(reservation)
            if reservation['id'] == reservation_id:
                self.reservations.remove(reservation)
                self.rooms.append(reservation['room_number'])
                print(f"Reservation {reservation_id} for {reservation['customer']} cancelled.")
                self.save_data()
                delete_reservation(reservation_id)
                return
        print(f"No reservation found for ID {reservation_id}.")

    def delete_hotel(self):
        """
        Deletes the hotel by resetting its attributes.

        Returns:
            None
        """
        self.name = None
        self.address = None
        self.rooms = []
        self.reservations = []
        self.save_data()
