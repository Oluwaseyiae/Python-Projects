#Data Transactions
import buyData
import giftData
import shareData
import dataBalance
import voiceDataRoamingOffers
import dataTransactions
import appOffers
import winPrado

#------------------------------Final Execution -------------------------------------------
# Data Transaction

def data_transaction():
    
    choice = int(input("\n1. Buy Data\n2. Gift Data\n3. Share Data\n4. Check Data Bal\n5. Voice/ Data ROAMING oFFER\n6. Glo My-G Bundle\n7. App offers- NEW\n8. WIN A PRADO\n0. Exit\nWhat's your choose: "))

    try:
        if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            raise ValueError("Invalid Option!")
    except ValueError as e:
        print(e)
        data_transaction()

    if choice == 1:
        buyData.buy_data()
    elif choice == 2:
        giftData.gift_data()
    elif choice == 3:
        shareData.sharing_data()
    elif choice == 4:
        dataBalance.check_data_balance()
    elif choice == 5:
        voiceDataRoamingOffers.voice_data_roaming_offers()
    elif choice == 6:
        dataTransactions.my_G_bundles()
    elif choice == 7:
        appOffers.app_offers_new()
    elif choice == 8:
        winPrado.win_a_prado()
    elif choice == 0:
        exit()
    else:
        print("Invalid Option!")
