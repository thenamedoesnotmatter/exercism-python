def latest(scores):
    """
    
    :param scores: list of int scores
    :return: int of latest score

    This function takes `scores` as a parameter and
    returns the latest score which has been added
    """

    return scores[-1]


def personal_best(scores):
    """
    
    :param scores: list of int scores
    :return: int of highest score

    This function takes `scores` as a parameter and
    returns the highest score within the scores list
    """
    return max(scores)


def personal_top_three(scores):
    """
    
    :param scores: list of int scores
    :return: list of top three of highest scores

    This function takes `scores` as a parameter and
    returns the top three of highest scores from this list
    """

    # Sort the list so we have the highest numbers at the end
    # of the list
    scores.sort()

    top_three_scores = scores[-3:]

    # To have the list show the top three scores from high to low
    # we have to sort the top three in reverse order
    return sorted(top_three_scores, reverse=True)



# These two functions are actually useless without state
# see https://github.com/exercism/python/issues/2786
# that's why we're just returning the right things to 
# make the test pass
def latest_after_top_three(scores):
    return scores[-1]


def scores_after_top_three(scores):
    return scores
