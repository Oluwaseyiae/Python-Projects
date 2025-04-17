import dataTransactions

#1. Tariff Plans

def tariff_plan():

    choice = int(input("\n1. My Package\n2. My Number\n3. Friends & Family Number\n4. Easy Share\n99. Bac\n0. Exit\nWhat's your choose: "))

    if choice == 1:
        print("\n1. To know your Package Dial #100#\n2. To Migerate to other profile Dial *100#")
        exit()
    elif choice == 2:
        print("\nDear customer, to know your Glo Number, please Dial *777#")
        exit() 
    elif choice == 3:
        print("\n1. To Manage Friends & Family, Dial #606*1#\n2. View Friends & Family list, Dial *170*50#")
        exit()
    elif choice == 4:
        print("\nDear customer, for Me2U please dial *131*phne number*amount*PIN#")
        exit()  
    elif choice == 99:
        voice_data_roaming_offers()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 

#2. Intl Call offers

def intl_call_offers():

    choice = int(input("\n1. N100 = 3 Min 1 Day\n2. N200 = 7 Min 3 Day\n3. N500 = 18 Min 10 Days\n4. N1000 = 37 Min 30 Days\n5. List of 8 countries\n6. Check IDD Pack Balance\n99. Bac\n0. Exit\nWhat's your choose: "))

    if choice == 1:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 2:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 3:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 4:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()  
    elif choice == 5:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 6:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 99:
        voice_data_roaming_offers()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 

#3. Data Roaming Offers 

def data_roaming_offers():

    choice = int(input("\n1. N2500 = 50MB 3 Days\n2. N5000 = 125MB 7 Days\n3. N10000 = 1GB 10 Days\n4. n25000 = 2.5GB 30 Days \n5. N50000 = 6GB 60 Days\n6. List of countries & partners\n99. Bac\n0. Exit\nWhat's your choose: "))

    if choice == 1:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 2:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 3:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 4:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()  
    elif choice == 5:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 6:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 99:
        voice_data_roaming_offers()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 


#4. Glo Talk On

def glo_talk_on():

    choice = int(input("\nGet 10 times vlue of all your recharges with GLO TALK ON. To migerate:\n1. Glo TalkOn\n99. Back\n0. Exit\nWhat's your Choose: "))

    if choice == 1:
        print("Your request for ALWAYS ON subscription is being processed. Please dial #100# after 2hrs for confirmation. A fee N500 is charged for this service. Thank you.")
        exit()
    elif choice == 99:
        voice_data_roaming_offers()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 

#5. Glo Super Talk 

def super_talk():

    print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
    exit() 


#6. Always open

def always_open():

    choice = int(input("\nGet 10 times vlue of all your recharges with GLO TALK ON. To migerate:\n1. Glo TalkOn\n99. Back\n0. Exit\nWhat's your Choose: "))

    if choice == 1:
        print("Your request for ALWAYS ON subscription is being processed. Please dial #100# after 2hrs for confirmation. A fee N500 is charged for this service. Thank you.")
        exit()
    elif choice == 99:
        voice_data_roaming_offers()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 

def voice_data_roaming_offers():

    choice = int(input("\n1. My Tariff Plan\n2. Intl Call offers \n3. Data Roaming offers \n4. Glo Talk on \n5. Glo Super Talk \n6. Always open\n99. Bac\n0. Exit\nWhat's your choose: "))

    try:
        if choice not in [1,2,3,4,5,6,99,0]:
            raise ValueError("Invalid Options!")
    except ValueError as e:
        print(e)
        voice_data_roaming_offers()

    if choice == 1:
        tariff_plan()
    elif choice == 2:
         intl_call_offers()
    elif choice == 3:
         data_roaming_offers()
    elif choice == 4:
         glo_talk_on()
    elif choice == 5:
         super_talk()
    elif choice == 6:
         always_open()
    elif choice == 99:
        dataTransactions.data_transaction()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 