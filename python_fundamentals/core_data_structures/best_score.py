#!/usr/bin/env python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)


if __name__ == "__main__":
    scores = {'John': 12, 'Bob': 14, 'Mike': 15, 'Molly': 16, 'Adam': 10}
    print(best_score(scores))
    print(best_score(None))
