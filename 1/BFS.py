import time
from queue import LifoQueue


class Card:
    def __init__(self, number, color):
        self.color = color
        self.number = number

    def get_color(self):
        return self.color

    def get_number(self):
        return self.number


def split_card(string):
    color = ""
    number = ""
    for i in range(len(string)):
        if string[i].isdigit():
            number = number + string[i]
        elif (('A' <= string[i] <= 'Z') or
              ('a' <= string[i] <= 'z')):
            color += string[i]
    # print(color)
    # print(number)
    return number, color


def print_cards():
    for section in sections:
        if section == []:
            print('#')
        else:
            # print(section)
            for card in section:
                print(card.number + card.color, end=" ")
            print("")


def move_card(origin, destination):
    if not sections[origin]:
        print("section {} is empty".format(origin))
        return
    else:
        if not sections[destination]:
            print("moving card from section {} to  empty section  {}".format(origin, destination))
            sections[destination].append(sections[origin].pop())
        elif sections[destination][-1].number >= sections[origin][-1].number:
            print("moving card from section {} to section  {}".format(origin, destination))
            sections[destination].append(sections[origin].pop())
        else:
            print("can not move card from section {} to section  {}".format(origin, destination))
            return


if __name__ == '__main__':
    # k = number of sections
    # m = number of colors
    # n = number of each color of cards (from )
    k, m, n = input().split()
    k, m, n = int(k), int(m), int(n)
    sections = []
    # we are going to have K sections
    for sec in range(k):
        section = []
        cards_in_section = input()
        if cards_in_section == '#':
            # sections.append('')
            # sections[sec] = []
            sections.append(section)
            continue
        cards_list = cards_in_section.split()  # "5g 5r 4y" => ["5g", "5r", "4y"]
        for card in cards_list:
            num, clr = split_card(card)  # "5g" => "5", "g"
            card_object = Card(num, clr)  # "5", "g" => Card object
            section.append(card_object)
        sections.append(section)

    print_cards()

    time.sleep(.5)
    move_card(3, 4)

    time.sleep(.5)
    print_cards()

