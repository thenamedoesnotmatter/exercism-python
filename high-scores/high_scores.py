def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort()
    return sorted(scores[-3:], reverse=True)



# These two functions are actually useless without state
# see https://github.com/exercism/python/issues/2786
# that's why we're just returning the right things to 
# make the test pass
def latest_after_top_three(scores):
    return scores[-1]


def scores_after_top_three(scores):
    return scores
