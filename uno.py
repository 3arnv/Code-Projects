
import random


colors = ['Red', 'Yellow', 'Green', 'Blue']
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']
wilds = ['Wild', 'Wild Draw Four']


deck = [color + ' ' + value for color in colors for value in values] + wilds * 4
random.shuffle(deck)


players = []
num_players = int(input("Enter number of players: "))
for i in range(num_players):
    players.append([])


for i in range(7):
    for player in players:
        player.append(deck.pop())


discard_pile = [deck.pop()]
current_player = 0
direction = 1

def display_hand(player):
    print(f"Player {player + 1}'s hand: {', '.join(players[player])}")

def valid_play(card, top_card):
    if 'Wild' in card:
        return True
    card_color, card_value = card.split(' ', 1)
    top_color, top_value = top_card.split(' ', 1)
    return card_color == top_color or card_value == top_value


while True:
    print(f"Top card: {discard_pile[-1]}")
    display_hand(current_player)
    
    
    while True:
        play = input(f"Player {current_player + 1}, choose a card to play or type 'draw' to draw a card: ")
        if play == 'draw':
            players[current_player].append(deck.pop())
            display_hand(current_player)
        elif play in players[current_player] and valid_play(play, discard_pile[-1]):
            discard_pile.append(play)
            players[current_player].remove(play)
            break
        else:
            print("Invalid play. Try again.")
    
    
    if not players[current_player]:
        print(f"Player {current_player + 1} wins!")
        break
    
    
    if 'Reverse' in play:
        direction *= -1
    elif 'Skip' in play:
        current_player = (current_player + direction) % num_players
    elif 'Draw Two' in play:
        next_player = (current_player + direction) % num_players
        players[next_player].extend([deck.pop(), deck.pop()])
    elif 'Wild Draw Four' in play:
        next_player = (current_player + direction) % num_players
        players[next_player].extend([deck.pop() for _ in range(4)])
    
    
    current_player = (current_player + direction) % num_players
