from random import randint

player_lost = False
player_won = False
player_card = int(randint(2, 20))
computer_card = randint(2, 20)
if player_card >= 22:
    player_lost = True
while player_lost == False and player_won == False:
    print("Your card value is: " + str(player_card))
    player_action = input("Hit or stand? ").lower()
    if player_action == "hit":
        player_card = player_card + randint(1, 10)
        if player_card > 21:
            break
    elif player_action == "stand":
        break
    else:
        print('Invalid input')
while computer_card < 21:
    computer_card = computer_card + randint(1, 10)

if player_card > 21:
    player_lost = True
    player_won = False
elif player_card == 21:
    player_lost = False
    player_won = True
elif computer_card > 21:
    player_lost = False
    player_won = True
elif computer_card == 21:
    player_lost = True
    player_won = False

if player_won == True and player_lost == False:
    print("You win! Your card value is " + str(player_card))
elif player_won == False and player_lost == True:
    print("You lost. Your card value is " + str(player_card))
# Add if player_card > computer_card and vice versa, also check if player_card == computer_card
# Future action items: you can remove player_won and lost and replace with game_statufrom random import randint

player_lost = False
player_won = False
player_card = int(randint(2, 20))
computer_card = randint(2, 20)
if player_card >= 22:
    player_lost = True
while player_lost == False and player_won == False:
    print("Your card value is: " + str(player_card))
    player_action = input("Hit or stand? ").lower()
    if player_action == "hit":
        player_card = player_card + randint(1, 10)
        if player_card > 21:
            break
    elif player_action == "stand":
        break
    else:
        print('Invalid input')
while computer_card < 21:
    computer_card = computer_card + randint(1, 10)

if player_card > 21:
    player_lost = True
    player_won = False
elif player_card == 21:
    player_lost = False
    player_won = True
elif computer_card > 21:
    player_lost = False
    player_won = True
elif computer_card == 21:
    player_lost = True
    player_won = False

if player_won == True and player_lost == False:
    print("You win! Your card value is " + str(player_card))
elif player_won == False and player_lost == True:
    print("You lost. Your card value is " + str(player_card))
# Add if player_card > computer_card and vice versa, also check if player_card == computer_card
# Future action items: you can remove player_won and lost and replace with game_status