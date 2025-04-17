# Import program functionalities
import health_tips
import book_appointment
import contact_doctor


# Welcome & Menu
def main():
    while True:
        print("\nWelcome to Health Support System!")
        entry = int(input("\nWhat do you wish to do:\n1. View health tips\n2. Book an appointment\n3. Speak with a doctor\n4. Exit\n\nWhat's your pick: "))

        # Handling wrong option
        try:
            if entry not in [1,2,3,4]:
                raise ValueError("\nInvalid Option!")
        except ValueError as e:
            print(e)
            continue

        

        if entry == 1:
            health_tips.health_tips()
            exit()
        elif entry == 2:
            book_appointment.book_appointment()
            exit()
        elif entry == 3:
            contact_doctor.contact_doctor()
            exit()
        elif entry == 4:
            print("Thank you for using this USSD app!")
            exit()
        else: 
            print("\nInvalid Option!")


# Excecute main function
if __name__ == "__main__":
    main()
