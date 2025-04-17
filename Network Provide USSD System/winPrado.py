import dataTransactions

def win_a_prado():

    choice = int(input("\nWin exciting Prizes like Toyota PRADO, KIA Picanto, KEKE NAPEPs, Generator, Sewing Machine, Grinder, during Festival of Joy Promo. Hurry!\n1. Participate\n99. Back\n0. Exit\nWhat's your choose: "))

    try:
        if choice not in [1, 99, 0]:
            raise ValueError("Invalid Option!")
    except ValueError as e:
        print(e)
        return win_a_prado()

    if choice == 1:
        print("You have been registered.")
        exit()
    elif choice == 99:
        dataTransactions.data_transaction()
    elif choice == 0:
        exit()
    else:
        print("Invalid Option!")