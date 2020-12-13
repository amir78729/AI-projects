import time
import copy

'''
5 3 5
5g 5r 4y
2g 4r 3y 3g 2y
1y 4g 1r
1g 2r 5y 3r
#
'''


class Card:
    def __init__(self, number, color):
        self.color = color
        self.number = number

    def get_color(self):
        return self.color

    def get_number(self):
        return self.number


class State:
    def __init__(self, cards_sections, depth, parent, move_from, move_to):
        self.cards_sections = cards_sections
        self.depth = depth
        self.parent = parent
        self.move_from = move_from
        self.move_to = move_to

    # def expand_children(self):
    #     children = []
    #     for i in range(len(self.cards_sections)):
    #         for j in range(len(self.cards_sections)):


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


def print_cards(sections):
    i = 0
    for section in sections:
        print(i, end=" : ")
        i += 1
        if not section:
            print('#')
        else:
            # print(section)
            for card in section:
                print(card.number + card.color, end=" ")
            print("")


def move_card(sec, origin, destination, print_it):
    sections = copy.deepcopy(sec)
    if print_it:
        print("----------------------------------------------------------------")
        print("****  MOVE FROM {} TO {}  ****".format(origin, destination))
    if not sections[origin]:
        if print_it:
            print("!!! section {} is empty".format(origin))
        print_cards(sections)
        return None
    else:
        if not sections[destination]:
            if print_it:
                print(">>> moving card from section {} to  empty section  {}".format(origin, destination))
            sections[destination].append(sections[origin].pop())
        elif sections[destination][-1].number >= sections[origin][-1].number:
            if print_it:
                print(">>> moving card from section {} to section  {}".format(origin, destination))
            sections[destination].append(sections[origin].pop())
        else:
            if print_it:
                print("!!! can not move card from section {} to section  {}".format(origin, destination))
            return None
        if print_it:
            print_cards(sections)
    return sections


# def move():
#     for step in steps:
#         move_card(step[0], step[1], True)
#         time.sleep(.2)


def get_inputs(sections):
    for sec in range(k):
        section = []
        cards_in_section = input()
        if cards_in_section == '#':
            sections.append(section)
            continue
        cards_list = cards_in_section.split()  # "5g 5r 4y" => ["5g", "5r", "4y"]
        for card in cards_list:
            num, clr = split_card(card)  # "5g" => "5", "g"
            card_object = Card(num, clr)  # "5", "g" => Card object
            section.append(card_object)
        sections.append(section)
    return sections


if __name__ == '__main__':
    # k = number of sections
    # m = number of colors
    # n = number of each color of cards (from )
    k, m, n = input().split()
    k, m, n = int(k), int(m), int(n)
    card_sections = []
    # print_cards(card_sections)
    # we are going to have K sections
    card_sections = get_inputs(card_sections)

    print_cards(card_sections)

    steps = []
    steps.append((3, 4))
    steps.append((1, 4))
    steps.append((3, 2))
    steps.append((2, 4))
    steps.append((2, 1))

    # print(steps)
    # steps.append((3, 4))
    # time.sleep(.5)
    print_cards(card_sections)
    a = move_card(card_sections, 3, 4, False)
    print_cards(a)
    print()
    print_cards(card_sections)
    # move_card(1, 4)
    # move_card(3, 2)
    # move_card(2, 4)
    # move_card(2, 1)

    # move()
    # print_cards()

    # time.sleep(.5)


