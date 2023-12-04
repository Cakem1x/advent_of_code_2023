#!/usr/bin/env python3

import unittest
from math import pow

def string_to_int_list(string_list):
    int_list = []
    for s in string_list.split(" "):
        if s != "":
            int_list.append(int(s))
    return int_list

def parse_card(card_string):
    name, remainder_string = card_string.split(":")
    winning_numbers, numbers = map(string_to_int_list, remainder_string.split("|"))
    return name, winning_numbers, numbers

def count_winning_numbers(winning_numbers, numbers):
    nr_win = 0
    for number in numbers:
        if number in winning_numbers:
            nr_win += 1
    return nr_win

def parse_cards_to_win(cards_list):
    return [count_winning_numbers(w_num, num) for _, w_num, num in [parse_card(card_string) for card_string in cards_list]]

def main():
    total_value = 0
    with open("input.txt", 'r', encoding="UTF-8") as input_file:
        while line := input_file.readline():
            name, winning_numbers, numbers = parse_card(line)
            nr_win = count_winning_numbers(winning_numbers, numbers)
            value = int(pow(2, nr_win-1)) if nr_win > 0 else 0
            print(f"Value of {name}: {value}")
            total_value += value
    print(f"Total value {total_value}")


# Run with:
# python -m unittest day04
class TestDay04(unittest.TestCase):
    def test_string_to_int_list(self):
        self.assertEqual(string_to_int_list("41 48 83 86 17"), [41,48,83,86,17])
        self.assertEqual(string_to_int_list("83 86  6 31 17  9 48 53"), [83,86,6,31,17,9,48,53])

    def test_parse_card(self):
        card_string = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        name, winning_numbers, numbers = parse_card(card_string)
        self.assertEqual(name, "Card 1")
        self.assertEqual(winning_numbers, [41,48,83,86,17])
        self.assertEqual(numbers, [83,86,6,31,17,9,48,53])

    def test_count_winning_numbers(self):
        test_data = [(4, "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"),
                     (2, "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"),
                     (2, "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"),
                     (1, "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"),
                     (0, "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"),
                     (0, "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")]
        for nr_win_expected, card_string in test_data:
            _, winning_numbers, numbers = parse_card(card_string)
            nr_win = count_winning_numbers(winning_numbers, numbers)
            self.assertEqual(nr_win, nr_win_expected)

    def test_parse_cards_to_win(self):
        test_data = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
                     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
                     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
                     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
                     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
                     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
        self.assertEqual([4,2,2,1,0,0], parse_cards_to_win(test_data))

if __name__ == '__main__':
    main()
