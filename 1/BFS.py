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

    def get_parent(self):
        return self.parent

    def get_cards_sections(self):
        return self.cards_sections

    def expand_children(self):
        children = []
        number_of_children = 0
        for i in range(len(self.cards_sections)):
            for j in range(i + 1, len(self.cards_sections)):
                mv = move_card(self.cards_sections, i, j, False)
                if mv:
                    child = State(mv, self.depth + 1, self, i, j)
                    # if child not in child.get_parents():
                    if child.get_cards_sections() not in child.get_parents():
                        children.append(child)
                        number_of_children += 1
                mv = move_card(self.cards_sections, j, i, False)
                if mv:
                    child = State(mv, self.depth + 1, self, j, i)
                    # if child not in child.get_parents():
                    if child.get_cards_sections() not in child.get_parents():
                        children.append(child)
                        number_of_children += 1
        print("expanding depth {} completed!\n{} children have been created.".format(self.depth + 1, number_of_children))
        return children

    def get_parents(self):
        parents = []
        current_node = self.parent
        count = 0
        while current_node is not None:
            count += 1
            # parents.append(current_node)
            parents.append(current_node.get_cards_sections())
            current_node = current_node.get_parent()
        # print(count)
        return parents

    def print_state(self):
        print("----------------------------------------------------------------")
        print("****  MOVE FROM {} TO {}  ****".format(self.move_from, self.move_to))
        print("depth: {}".format(self.depth))
        print_cards(self.cards_sections)

    def goal_test(self):
        visited_colors = []  # to check all cards with the same colors are placed in the same section
        for sec in self.cards_sections:
            if sec:  # if the section is not empty:
                color = sec[0].get_color()
                if color in visited_colors:  # 2 cards with same colors in 2 sections
                    return False
                number = sec[0].get_number()
                for card in sec:
                    # checking the card number and colors in one section
                    if card.get_color() == color and card.get_number() <= number:
                        number = card.get_number()
                    else:
                        return False
                visited_colors.append(color)
            else:
                continue
        return True


def split_card(string):
    color = ""
    number = ""
    for i in range(len(string)):
        if string[i].isdigit():
            number = number + string[i]
        elif (('A' <= string[i] <= 'Z') or
              ('a' <= string[i] <= 'z')):
            color += string[i]
    return number, color


def print_cards(sections):
    i = 0
    for section in sections:
        print(i, end=" : ")
        i += 1
        if not section:
            print('#')
        else:
            for card in section:
                print(card.number + card.color, end=" ")
            print("")


def move_card(sec, origin, destination, print_it):
    sections = copy.deepcopy(sec)
    empty = []
    if print_it:
        print("----------------------------------------------------------------")
        print("****  MOVE FROM {} TO {}  ****".format(origin, destination))
    if not sections[origin]:
        if print_it:
            print("!!! section {} is empty".format(origin))
            print_cards(sections)
        return empty
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
            return empty
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


def breadth_first_search(initial_state):
    # is_goal = False
    i = 1
    frontier.append(initial_state)
    while True:
        print(i)

        if not frontier:
            print("failure!!!")
            return
        # redundent = False
        print("frontier:{} - explored:{}".format(len(frontier), len(explored)))

        candidate = frontier.pop()
        explored.append(candidate)

        if candidate.goal_test():
            print("goal!")
            return  # solution

        candidate.print_state()

        children = candidate.expand_children()
        for child in children:
            print('#', end="")
            if  (child not in explored):
                # if child.goal_test():
                #     print("goal!")
                #     return  # solution
                frontier.append(child)
        i += 1


if __name__ == '__main__':
    frontier = []
    explored = []
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

    # selected pattern from BFS search
    steps = []
    steps.append((3, 4))
    steps.append((1, 4))
    steps.append((3, 2))
    steps.append((2, 4))
    steps.append((2, 1))

    nodes = []

    s = State(card_sections, 0, None, -1, -1)

    # breadth_first_search(s)


    # c = s.expand_children()
    # nodes.append(c)
    #
    # for cc in c:
    #
    #     cc.print_state()
    #     print(cc.goal_test())
    #     ccc = cc.expand_children()
    #     for cccc in ccc:
    #         cccc.print_state()
    #         print(cccc.goal_test())


    # print(steps)
    # steps.append((3, 4))
    # time.sleep(.5)
    # print_cards(card_sections)
    # a = move_card(card_sections, 3, 4, False)
    # print_cards(a)
    # print()
    # print_cards(card_sections)
    # move_card(1, 4)
    # move_card(3, 2)
    # move_card(2, 4)
    # move_card(2, 1)

    # move()
    # print_cards()

    # time.sleep(.5)

    i = 1
    frontier.append(s)
    while True:
        print(i)

        if not frontier:
            print("failure!!!")

        # redundent = False
        print("frontier:{} - explored:{}".format(len(frontier), len(explored)))

        candidate = frontier.pop(0)
        explored.append(candidate)

        if candidate.goal_test():
            print("goal!")
            # solution
            break

        candidate.print_state()

        children = candidate.expand_children()
        for child in children:
            print('#', end="")
            if child not in explored:
                # if child.goal_test():
                #     print("goal!")
                #     return  # solution
                frontier.append(child)
        i += 1


