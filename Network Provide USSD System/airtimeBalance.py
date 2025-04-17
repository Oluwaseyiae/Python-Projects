def check_Airtime_balance():

    choice = int(input("\nSelect 1 for Main Balance\nSelect 2 for Bonus Balance "))

    try:
        if choice not in [1, 2]:
            raise ValueError("Invalid Option")
    except ValueError as e:
        print(e)
        check_Airtime_balance()

    if choice == 1:
        print("\nYour credit balance is 0.00 NGN valid until 23-07-2025. Take your Chance and earn a reward, Dial *20905*1*1# @N100/ day to attempt the prize")
        exit()

    elif choice == 2:
        print("\nYou do not have any bonus balance on your account")
        exit()
    
    else:
        print("\nInvalid Option")