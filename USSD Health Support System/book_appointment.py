#Book Appointment

def book_appointment():
    print("\n Book an Appointment")
    name = input("Enter your name: ")
    service = input("Type of appointment (e.g., General Checkup, Dental, Eye Test): ")
    date = input("Preferred date (e.g., 2025-04-20): ")

    print(f"\nThank you, {name}!")
    print(f"Your appointment for {service} has been booked for {date}.")
    print("We’ll get back to you with a confirmation message soon.")