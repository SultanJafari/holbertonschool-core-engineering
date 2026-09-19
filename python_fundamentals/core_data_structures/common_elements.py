#!/usr/bin/env python3


def common_elements(set_1, set_2):
    return set_1 & set_2


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    print(sorted(list(common_elements(set_1, set_2))))
