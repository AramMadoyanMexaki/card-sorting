import random


def make_deck():
    """
        Function for making a deck:

        We have four card suits: Clubs, Heart, Diamonds, Spades, and each of them has 13 ranks.

        We also have a set of 13 card ranks. (2, 3, 4, ....,J, Q, K, A), we need one of the cards for each card member.

    """
    
    card_suits = set(("Clubs", "Heart", "Diamonds", "Spades"))
    card_ranks = list(("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"))

    deck = list()

    for suit in card_suits:
        for rank in card_ranks:
            deck.append({suit: rank})

    return deck


def deal_deck():
    deck = make_deck()
    
    new_deck = deck.copy()
    random.shuffle(new_deck)

    dealed_cards = []

    for i in range(1, len(new_deck)):
        if i <= 10:
            dealed_cards.append(new_deck[i])
            new_deck.remove(new_deck[i])
        else:

            break

        
    return dealed_cards


def deck_sorting(user_deck):
    face_ranks = {"J": 11, "Q": 12, "K": 13, "A": 14}
    suits_rank_numerical = []

    for card in user_deck:
        for suit, rank in card.items():
            if rank in face_ranks:
                numeric_rank = face_ranks[rank]
            else:
                numeric_rank = int(rank)

            suits_rank_numerical.append((suit, numeric_rank))


        suits_rank_numerical.sort(key=lambda x: (x[0], x[1]))
    
    def to_letters(deck):
        converted_deck = []
        reverse_face_ranks = {v: k for k, v in face_ranks.items()}
        print(deck)

        for suit, rank in deck:
            print("suit ", suit, "rank", rank)
            rank = reverse_face_ranks.get(rank, str(rank)) 
            converted_deck.append((suit, rank)) 
        return converted_deck

    return to_letters(suits_rank_numerical)


user_deck = deal_deck()

# print(user_deck, "\n")
print(deck_sorting(user_deck))
