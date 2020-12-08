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
        if sec is None:
            print('#')
        else:
            for card in section:
                print(card.number + card.color, end=" ")
            print("")


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
            sections.append(None)
            continue
        cards_list = cards_in_section.split()  # "5g 5r 4y" => ["5g", "5r", "4y"]
        for card in cards_list:
            num, clr = split_card(card)  # "5g" => "5", "g"
            card_object = Card(num, clr)  # "5", "g" => Card object
            section.append(card_object)
        sections.append(section)
        # sections.append(userList)
    print_cards()
