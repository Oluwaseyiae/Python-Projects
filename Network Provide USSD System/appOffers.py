import dataTransactions

def app_offers_new():

    choice = int(input("\nExciting offers only on Glo Cafe App\n1. 100GB Bonus Data\n2. Recharge Bonus - 100%\n3. 10% more on Data Plans\n4. App only Special Data Bundles\n5. Enjoy Glo Cafe offers\n99. Bac\n0. Exit\nWhat's your choose: "))

    try:
        if choice not in [1, 2, 3, 4, 5, 99, 0]:
            raise ValueError("Invalid Option!")
    except ValueError as e:
        print(e)
        app_offers_new()

    if choice == 1:
        print("Only For Users: Download & Rester Glo Cafe & get 100GB Data (75GB instant + 5GB for 5 Months) Hurry! Download the GLO CAFE APP from App Store")
    elif choice == 2:
        print("100% Recharge Bonus on Cafe: Get 100% Recharge Bonus Every Time on recharges done through Glo Cafe App. Hurry! Download the GLO CAFE App from App Store.")
    elif choice == 3:
        print("10% Bonus Data: On Data purchased through Glo Cafe App, Example: 300MB more on N2000 Bundle. Hurry! Download the GLO CAFE App from App Store.")
    elif choice == 4:
        print("Special Bundles: Available only  on APP, N200 = 750MB 1 Day, N300 = 1.5GB 1 Day, N500 = 2.5GB 2 Days, N2000 = 10GB 7 Days. Hurry! Download the GLO CAFE App from App Store.")
    elif choice == 5:
        print("100GB Bonus + 100% Recharge Bonus + 10% More Data + Special Data Bundles App Download: Android: bit.ly/3zQUZRA, iOS: apple.co/3o60s4v")
    elif choice == 99:
        dataTransactions.data_transaction()
    elif choice == 0:
        exit()
    else:
        print("Invalid Option!")