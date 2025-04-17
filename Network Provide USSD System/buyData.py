import dataTransactions

# ---------------------------------------------------Buy Data Options
#1. Mini Plans

def mini_plans():

    choice = int(input("\n1. N100 = 105MB 1 Day incl 5MB nite\n2. N200 = 235MB 2 Days incl 25MB nite\n3. N500 = 1.5GB 7 Days incl 1GB nite\n4. N50 = 1 Day 5MB nite\n5. More Plans\n99. Back \n0. Exit\nWhat's your choose: "))

    def more_plans():

        choice = int(input("\n1. N750 = 1.1GB 14 Days\n2. N1000 = 3.5GB 7 Days incl 2GBB nite\n3. N2000 = 8.5GB 7 Days incl 2.5GB nite\n4. N5000 = 20.5GB 7 Days incl 2GB nite\n99. Back \n0. Exit\nWhat's your choose: "))

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
        elif choice == 99:
            mini_plans()
        elif choice == 0:
            exit()
        else:
            print("Invalid Options!") 


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
        more_plans()
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 

#2. Monthly Plans

def monthly_plans():
    
    choice = int(input("\n1. N1000 = 2.6GB 30 Day incl 1.5GB nite\n2. N1500 = 5GB 30 Days incl 3GB nite\n3. N2000 = 6.15GB 30 Days incl 3GB nite\n4. N2500 = 7.25GB 30 Day incl 3GB nite\n5. More Plans\n99. Back \n0. Exit\nWhat's your choose: "))

    def more_plans():
        choice = int(input("\n1. N3000 = 10GB 30 Days incl 2GBB nite\n2. N4000 = 12.5GB 30 Days incl 2GBB nite\n3. N5000 = 16GB 30 Days incl 2.5GB nite\n4. N6000 = 20.5GB 30 Days incl 2GB nite\n99. Back \n0. Exit\nWhat's your choose: "))

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
        elif choice == 99:
            monthly_plans()
        elif choice == 0:
            exit()
        else:
            print("Invalid Options!") 


    if choice == 1:
        print("SORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 2:
        print("SORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 3:
        print("SORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 4:
        print("SORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 5:
        more_plans()
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 

#3. Mega Plans

def mega_plans():
    
    choice = int(input("\n1. N10000 = 38GB 30 Days incl 2GBB nite\n2. N15000 = 64GB 30 Days incl 2GBB nite\n3. N20000 = 107GB 30 Days incl 2GB nite\n4. More Plans\n99. Back \n0. Exit\nWhat's your choose: "))

    def more_plans():

        choice = int(input( "\n1. N25000 = 135GB 30 Days \n2. N30000 = 165GB for 30 Days \n3. N40000 = 220GB 30 Days \n4. N50000 = 310GB for 60 Days \n5. N60000 = 355GB for 90 Days \n6. N75000 = 475GB for 90 Days \n99. Back \n0. Exit\nWhat's your choose: "))

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
            mega_plans()
        elif choice == 0:
            exit()
        else:
            print("Invalid Options!") 
    

    if choice == 1:
        print("SORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 2:
        print("SORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 3:
        print("SORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit() 
    elif choice == 4:
        more_plans()
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 


#4. Super Mega Plans

def super_mega_plans():
    
    choice = int(input("\n1. N25000 = 135GB 30 Days \n2. N30000 = 165GB for 30 Days \n3. N40000 = 220GB 30 Days \n4. N50000 = 310GB for 60 Days \n5. N60000 = 355GB for 90 Days \n6. N75000 = 475GB for 90 Days \n99. Back \n0. Exit\nWhat's your choose: "))
    

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
        buy_data
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 

#5. Special Data offer

#5.1. Special Plans

def special_plans():
    choice = int(input("\n1. N350 = 1GB 1 Day\n2. N500 = 2GB 1 Day incl 1GBB nite\n3. N600 = 3.55GB 1 Day incl 2GB nite\n4. N1000 = 5.1GB 2 Days incl 2GB nite\n5. N1500 = 5.9GB 7 Days incl 2GB nite\n99. Back \n0. Exit\nWhat's your choose: " ))

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
    elif choice == 3:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 99:
        buy_data
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!")


#5.2. Campus Booster

def campus_booster():
    choice = int(input("\n1. N100 = 200MB 1 Day\n2. N200 = 445MB 2 Days incl 25MB nite on campus\n3. More\n99. Back \n0. Exit\nWhat's your Choose: "))

    def more_plans():

        choice = int(input("\n1. N500 = 2GB 7 Days incl 1GB nite on campus\n2. N1000 = 4.2GB 30 Days incl 2GB nite on campus\n3. More\n99. Back \n0. Exit\nWhat's yoour Choose: "))

        def another_more_plans():

            choice = int(input("\n1. N2000 = 9.8GB 30 Days incl 3.5GB nite on campus\n2. N5000 = 30GB 30 Days incl 3GB nite on campus\n99. Back \n0. Exit\nWhat's yoour Choose: "))

            if choice == 1:
                print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
                exit()
            elif choice == 2:
                print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
                exit()
            elif choice == 99:
                more_plans()
            elif choice == 0:
                exit()
            else:
                print("Invalid Options!")

        if choice == 1:
            print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
            exit()
        elif choice == 2:
            print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
            exit()
        elif choice == 3:
            another_more_plans()
        elif choice == 99:
            campus_booster()
        elif choice == 0:
            exit()
        else:
            print("Invalid Options!")

    if choice == 1:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 2:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 3:
        more_plans()
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!")

#5.3. Hourly Bundles

def hourly_bundles():
    choice = int(input("\n1. N200 = 500MB 1hr\n2. N300 = 1GB 2hrs\n99. Back \n0. Exit\nWhat's your choose: "))
     
    if choice == 1:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 2:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!")

#5.4. Betting Agent

def bestting_agent():
    choice = int(input("\n1. N1000 = 4GB 30 Days\n2. N5000 = 30GB 30 Days\n3. N10000 = 75GB 30 Days\n99. Back \n0. Exit\nWhat's your choose: "))

    if choice == 1:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 2:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 3:
        print("\nSORRY! Insufficient credit balance for the plan you want to buy. Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *303#")
        exit()
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!")


def special_data_offer():
    
    choice = int(input("\n1. Special Plans\n2. Campus Booster\n3. Hourly Bundles\n4. Betting Agent Plan\n99. Back \n0. Exit\nWhat's your choose: "))
    
    if choice == 1:
        special_plans()
    elif choice == 2:
        campus_booster() 
    elif choice == 3:
        hourly_bundles() 
    elif choice == 4:
        bestting_agent() 
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 

#6. Social Bundles

def social_bundles():

    choice = int(input("\n1. Bundles for WhatsApp, Twitter, Facebook, TikTok, snapchat, Telegram, Instagram, Threads abd GloTV\n2. MY-G Bundles-WhatsApp, TikTok, Insta, Snapchat, Boomplay\n99. Back \n0. Exit\nWhat's your choose: "))

    def all_social():
        
        choice = int(input("\n1. N50 = 135MB 3 Days\n2. N100 = 335MB 7 Days\n3. N300 = 1.1GB 10 Days\n4. N500 = 1.8GB 15 Days\n99. Back \n0. Exit\nWhat's your choose: "))

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
        elif choice == 99:
            social_bundles()
        elif choice == 0:
            exit()
        else:
            print("Invalid Options!") 
    
    def limited_social():
        
        choice = int(input("\n Apps: WhatsApp, TikTok, Insta, Boomplay, Snapchat\n1. N100 = 300MB + 1 hr, 1 Day\n2. N300 = 1GB + 1 hr, 3 Days\n3. N500 = 1.5GB + 1 hr, 7 Days\n4. N1000 = 3.5GB + 1 hr, 30 Days\n99. Back \n0. Exit\nWhat's your choose: "))

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
        elif choice == 99:
            social_bundles()
        elif choice == 0:
            exit()
        else:
            print("Invalid Options!") 


    if choice == 1:
        all_social()
    elif choice == 2:
        limited_social() 
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 


#7. Night & Weekend Plans

def night_weekend_plans():

    choice = int(input("\n1. N60 = 350MB 1 Day (12am - 05am)\n2. N1200 = 750MB 1 Day (12am - 05am)\n3. N200 = 875MB 2 Days SAT-SUN\n4. N500 = 2.5MB 2 Days SAT-SUN\n99. Back \n0. Exit\nWhat's your choose: "))

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
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 


#8. My-G Bundles

def my_G_bundles():

    choice = int(input("\nApps: WhatsApp, TikTok, Insta, Boomplay, Snapchat\n1. N100 = 300MB + 1 hr, 1 Day\n2. N300 = 1GB + 1 hr, 3 Days\n3. N500 = 1.5GB + 1 hr, 7 Days\n4. N1000 = 3.5GB + 1 hr, 30 Days\n99. Back \n0. Exit\nWhat's the choose: "))

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
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 

#9. GLOTV Plans#

def glotv_plans():

    choice = int(input("\n1. N150 = VOD 500MB 5 Days\n2. N450 = VOD 2GB  7 Days\n3. N1,400 = VOD 6GB 30 Days\n4. N900 = VOD + TV 2GB 7 Days\n5. N3,200 = VOD + TV 6GB 30 Days\n99. Back \n0. Exit\nWhat's your choose: "))

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
    elif choice == 99:
        buy_data()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 



# ---------------------------------------------------Data Plans
def all_data_plans():

    choice = int(input("\n1. Mini Plans\n2. Monthly Plans\n3. Mega Plans\n4. Super Mega Plans\n5. Special Data offer\n6. Social Bundles\n7. Night & Weekend Plans\n8. My-G Bundles\n9. GLOTV Plans\n99. Back\n0. Exit\nWhat's your choose: "))

    if choice == 1:
        mini_plans()
    elif choice == 2:
        monthly_plans() 
    elif choice == 3:
        mega_plans() 
    elif choice == 4:
        super_mega_plans() 
    elif choice == 5:
        special_data_offer() 
    elif choice == 6:
        social_bundles() 
    elif choice == 7:
        night_weekend_plans() 
    elif choice == 8:
        my_G_bundles()
    elif choice == 9:
        glotv_plans() 
    elif choice == 99:
        pass
    elif choice == 0:
        pass
    else:
        print("Invalid Options!") 

# ---------------------------------------------------Buy Data Options

# 1. Preceed (Auto-Renew) 

def auto_renewal():
    all_data_plans()


# 2. Preceed (One-Off) 

def no_auto_renewal():
    all_data_plans()



#------------------------------Final Execution -------------------------------------------
# Buy Data
def buy_data():

    choice = int(input("\n1. Proceed (Auto-Renew)\n2. Proceed (0ne-Off)\n99. Back\n0. Exit\nWhat's your choose: "))

    try:
        if choice not in [1, 2, 99, 0]:
            raise ValueError("Invalid Options!")
    except ValueError as e:
        print(e)
        buy_data()

    if choice == 1:
        auto_renewal()
    elif choice == 2:
        no_auto_renewal()
    elif choice == 99:
        dataTransactions.data_transaction()
    elif choice == 0:
        exit()
    else:
        print("Invalid Options!") 
