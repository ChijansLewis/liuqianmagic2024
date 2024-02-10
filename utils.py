import random

def choose_four_cards():
    # 生成一副标准扑克牌
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(suit, rank) for suit in suits for rank in ranks]

    # 随机选择四张牌
    selected_cards = random.sample(deck, 4)
    return selected_cards

def show_cards(chosen_cards):
    for card in chosen_cards:
        print(f"{card[0]}{card[1]}", end=' ')
    print()