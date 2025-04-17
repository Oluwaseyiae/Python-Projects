import dataTransactions 
import airtimeBalance
import dataBalance

# Welcome
def main():
    while True:
        print("\nWelcome to Glo Network")
        entry = int(input("\nWhat do you wish to do: \n1.Check Airtime(*310#)\n2.Data Transaction(*312#)\n3.Check Data Balance (*323#)\n4.Exit\nWhat's your choose: "))
        
        try:
            if entry not in [1,2,3,4]:
                raise ValueError("Invalid Option!\n")
        except ValueError as e:
            print(e)
            continue

        if entry == 1:
            airtimeBalance.check_Airtime_balance()
        elif entry == 2:
            dataTransactions.data_transaction()
        elif entry == 3:
            dataBalance.check_data_balance()
        elif entry == 4:
            exit()
        else:
            print("\nInvalid Option!")

# Run Main Function
main()


