def get_rounds(number: int) -> list:
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list, rounds_2: list) -> list:
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: list, number: int) -> bool:
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand: list) -> float:
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: list) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    average_first_last = (hand[0] + hand[-1]) / 2
    average_median_index = round(len(hand) / 2)
    average_median = hand[average_median_index]
    actual_average = card_average(hand)

    compare_list = [average_first_last, average_median]

    if actual_average in compare_list:
        return True

    return False


def average_even_is_average_odd(hand: list) -> bool:
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    average_even = card_average(hand[::2])
    average_odd = card_average(hand[::1])

    if average_even == average_odd:
        return True

    return False


def maybe_double_last(hand: list) -> list:
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22

    return hand
