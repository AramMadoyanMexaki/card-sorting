import random


# def make_deck():
#     """
#         Function for making a deck:

#         We have four card suits: Clubs, Heart, Diamonds, Spades, and each of them has 13 ranks.

#         We also have a set of 13 card ranks. (2, 3, 4, ....,J, Q, K, A), we need one of the cards for each card member.

#     """
    
#     card_suits = set(("Clubs", "Heart", "Diamonds", "Spades"))
#     card_ranks = list(("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"))

#     deck = list()

#     for suit in card_suits:
#         for rank in card_ranks:
#             deck.append({suit: rank})

#     return deck


def deck_sorting(user_deck):
    face_ranks = {"J": 11, "Q": 12, "K": 13, "A": 14}
    suits_rank_numerical = []

    for card in user_deck:
        rank = card['rank']
        suit = card['suit']

        if rank in face_ranks:
            numeric_rank = face_ranks[rank]
        else:
            numeric_rank = int(rank)

        suits_rank_numerical.append({"rank": numeric_rank, "suit": suit})


    suits_rank_numerical.sort(key=lambda x: (x['suit'], x['rank']))
    
    def to_letters(deck):
        converted_deck = []
        reverse_face_ranks = {v: k for k, v in face_ranks.items()}

        for card in deck:
            rank = card['rank']
            suit = card['suit']

            if rank in reverse_face_ranks:
                rank = reverse_face_ranks[rank]

            converted_deck.append({"rank": rank, "suit": suit}) 


        return converted_deck

    return to_letters(suits_rank_numerical)


user_deck = [
    { "rank": 'J', "suit": 'Clubs'},
    { "rank": 'J', "suit": 'Heart'},
    { "rank": '7', "suit": 'Diamonds'},
    { "rank": '8', "suit": 'Diamonds'},
    { "rank": '9', "suit": 'Spades'},
    { "rank": '2', "suit": 'Clubs'},
    { "rank": '3', "suit": 'Heart'},
    { "rank": '5', "suit": 'Diamonds'},
    { "rank": '10', "suit": 'Clubs'},
    { "rank": 'J', "suit": 'Diamonds'}]


print(deck_sorting(user_deck))
