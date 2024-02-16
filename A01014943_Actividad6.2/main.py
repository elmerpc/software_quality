import hotel as h
import customer as c


marriott = h.Hotel("Marriott", "123 Main St.")

print(marriott.display_information())
marriott.reserve_room(101, "John Doe", "2022-01-01", "2022-02-15")
marriott.reserve_room(102, "John Doe", "2022-01-01", "2022-01-15")
#past_marriott = marriott.load_data()

#past_marriott.display_information()

#past_marriott.cancel_reservation(7)
#marriott.save_data()
