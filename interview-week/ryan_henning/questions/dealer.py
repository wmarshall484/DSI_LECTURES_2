from __future__ import division, absolute_import, print_function


def dealer_probs(hand_sum, is_hand_soft, deck, soft_17_hit):
    """
    `deck` is a list of 11 values.
        deck[0] = the number of cards in the deck
        deck[1] = the number of aces in the deck
        deck[2] = the number of 2s in the deck
        ...
        deck[9] = the number of 9s in the deck
        deck[10] = the number of 10s and face-cards in the deck

    Returns tuple (prob_17, prob_18, prob_19, prob_20, prob_21, prob_bust)
    """

    if hand_sum > 21 and is_hand_soft:
        hand_sum -= 10
        is_hand_soft = False

    if hand_sum > 21:
        # BUST
        return 0.0, 0.0, 0.0, 0.0, 0.0, 1.0

    if 17 <= hand_sum <= 21 and (not is_hand_soft or not soft_17_hit or hand_sum > 17):
        probs = [0.0] * 6
        probs[hand_sum-17] = 1.0
        return tuple(probs)

    # Else hand is <17

    probs = [0.0] * 6

    n_cards = float(deck[0])

    for card_value, card_count in enumerate(deck):

        if card_value == 0:
            continue

        if card_value == 1 and hand_sum <= 10:
            # In this case count the ace as a soft 11.
            card_effective_value = 11
        else:
            card_effective_value = card_value

        if card_count > 0:
            prob_this_card = card_count / n_cards
            #deck[0] -= 1
            #deck[card_value] -= 1
            probs_next = dealer_probs(hand_sum + card_effective_value,
                                      is_hand_soft or (card_effective_value == 11),
                                      deck,
                                      soft_17_hit)
            #deck[0] += 1
            #deck[card_value] += 1

            probs = [prob + prob_this_card*next_prob for prob, next_prob in zip(probs, probs_next)]

    return tuple(probs)


def build_deck(num_decks):
    deck = [52 * num_decks] + ([4 * num_decks] * 9) + [16 * num_decks]
    return deck


if __name__ == '__main__':

    import pandas as pd
    import argparse

    parser = argparse.ArgumentParser(description="Prints blackjack dealer probabilites")
    parser.add_argument('-d', '--num_decks', type=int, required=True,
                        help="number of decks in the dealer's shoe")
    parser.add_argument('-s', '--soft_17_hit', action='store_true',
                        help="whether or not the dealer hits on soft-17 hands")
    args = parser.parse_args()

    num_decks = args.num_decks
    print('num_decks', num_decks)

    soft_17_hit = args.soft_17_hit
    print('soft_17_hit', soft_17_hit)

    row_names = ['none specified', 'ace', 'two', 'three', 'four',
                 'five', 'six', 'seven', 'eight', 'nine', 'ten or face']

    col_names = ['prob_17', 'prob_18', 'prob_19', 'prob_20', 'prob_21', 'prob_bust']

    rows = []

    for up_card in range(0, 11):
        if up_card == 1:
            up_card = 11
        probs = dealer_probs(up_card, up_card == 11, build_deck(num_decks), soft_17_hit)
        rows.append(probs)


    df = pd.DataFrame(rows, index=row_names, columns=col_names)
    print(df)

