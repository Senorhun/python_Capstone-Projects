import random


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer = []
player = []
def deal(option):
    if option == "y":
        player.append(random.choice(cards))
    if sum(dealer) < 17 and sum(player) < 21:
        dealer.append(random.choice(cards))
    
while True:    
    option = input("Do you want to play Black Jack 'y' or 'n' ?   ")
    if option == "n":
        print("Thank you for using our program, bye!")
        break
    elif option == "y":
        dealer.clear()
        player.clear()
    player.append(random.choice(cards))
    player.append(random.choice(cards))

    dealer.append(random.choice(cards))
    dealer.append(random.choice(cards))
    print(f"Dealer hand: {dealer[0]}")

    while True:
        print(f"Player hand: {player} in total {sum(player)}")
        if sum(player) > 21:
            print("***LOST***")
            print(f"Dealer hand: {dealer} in total {sum(dealer)}")
            print(f"Player hand: {player} in total {sum(player)}")
            break
        elif sum(player) == 21 or sum(dealer) > 21:
            print("***WON***")
            print(f"Dealer hand: {dealer} in total {sum(dealer)}")
            print(f"Player hand: {player} in total {sum(player)}")
            break

        option = input("Do you want a card 'y' or 'n' ?   ")
        deal(option)
        if option == "n":
            if sum(player) < sum(dealer) and sum(dealer) <= 21:
                print("***LOST***")
                print(f"Dealer hand: {dealer} in total {sum(dealer)}")
                print(f"Player hand: {player} in total {sum(player)}")
                break
            elif sum(player) > sum(dealer) and sum(player) <= 21:
                print("***WON***")
                print(f"Dealer hand: {dealer} in total {sum(dealer)}")
                print(f"Player hand: {player} in total {sum(player)}")
                break
            elif sum(player) == sum(dealer) and sum(player) <= 21 and sum(dealer) <= 21:
                print("***TIE***")
                print(f"Dealer hand: {dealer} in total {sum(dealer)}")
                print(f"Player hand: {player} in total {sum(player)}")
                break
        print(f"Dealer hand: {dealer}")
        