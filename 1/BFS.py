class Card:

    def __init__(self, number, color):
        self.color = color
        self.number = number


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


if __name__ == '__main__':
    # k = number of sections
    # m = number of colors
    # n = number of each color of cards (from )
    k, m, n = input().split()
    k, m, n = int(k), int(m), int(n)
    # we are going to have K sections
    sections = []
    for sec in range(k):
        section = []
        cards_in_section = input()
        if cards_in_section == '#':
            sections.append(None)
            continue
        cards_list = cards_in_section.split()
        print(cards_list)
        for card in cards_list:
            num, clr = split_card(card)
            card_object = Card(num, clr)
            section.append(card_object)
        sections.append(section)
        # sections.append(userList)
    print(sections)
