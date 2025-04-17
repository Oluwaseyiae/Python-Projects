# Speak with a Doctor

import random

def contact_doctor():
    print("\nContact a Doctor")
    
    doctor_names = ["Dr. John", "Dr. George", "Dr. Ken", "Dr. Kelly", "Dr. Tim"]
    doctor_numbers = ["0802", "0803", "0701", "0814", "0905"]
    
    selected_name = random.choice(doctor_names)
    selected_number = random.choice(doctor_numbers) + str(random.randint(1000000, 9999999))
    
    print(f"You can reach {selected_name} at {selected_number}")
