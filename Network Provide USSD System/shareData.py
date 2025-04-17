#1. Share data
def share_data():
    number = input("Please enter Glo subscriber number, you want to share data with")
    print(F"{number} has been added to your share data subscription")
    exit()

#2. Unshare Data
def unshare_data() :
    number = input("Please enter Glo subscriber number, you want to unshare")
    print(F"{number} has been removed from your share data subscription")
    exit()

#3. List of Shared Numbers
def list_numbers() :
    print("\nNOTE: There is no number sharing your plan subscription")
    exit()

#4. Gett Data Settings
def get_data_settings():
    print("\nNOTE: There is no number sharing your plan subscription")
    exit()

#5. Manual Configuration Details
def config_details():
    print("\nPlease save the APN details under setting option in your handset.\nApn Name: glo flat\nUser Name: flat\nPassword: flat")
    exit()

#6. Easy Share (Credit Share)
def easy_share():
    
    print("To share airtime with other Glo Number, pls dial *131*Glo Number*Amount*PIN#\nDefault PIN: 00000 Not: Easy share is not available for Brekete Customers.")
    exit()



# 3. Share Data
def sharing_data():
    choice = int(input("\n1. Share data\n2. Unshare Data\n3. List of Shared Numbers\n4. Gett Data Settings\n5. Manual Configuration Details\n6. Easy Share (Credit Share)\n99. Back\n0. Exit\nWhat's your choose: "))

    try:
        if choice not in [1, 2, 3, 4, 5, 6, 0]:
            raise ValueError("Invalid Options!")
    except ValueError as e:
        print(e)
        sharing_data()

    if choice == 1:
        share_data()
    elif choice == 2:
        unshare_data() 
    elif choice == 3:
        list_numbers() 
    elif choice == 4:
        get_data_settings() 
    elif choice == 5:
        config_details() 
    elif choice == 6:
        easy_share() 
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 

