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

    def get_move_from(self):
        return self.move_from

    def get_move_to(self):
        return self.move_to

    def get_parent(self):
        return self.parent

    def get_depth(self):
        return self.depth

    def get_cards_sections(self):
        return self.cards_sections

    def expand_children(self, print_it):
        children = []
        global number_of_children
        for i in range(len(self.cards_sections)):
            for j in range(i + 1, len(self.cards_sections)):
                mv = move_card(self.cards_sections, i, j, False)
                if mv:
                    child = State(mv, self.depth + 1, self, i, j)
                    # if child.get_cards_sections() not in child.get_parents():
                    if child not in explored:
                        children.append(child)
                        number_of_children += 1
                    else:
                        print("gooooooooooooood")
                mv = move_card(self.cards_sections, j, i, False)
                if mv:
                    child = State(mv, self.depth + 1, self, j, i)
                    # if child.get_cards_sections() not in child.get_parents():
                    if child not in explored:
                        children.append(child)
                        number_of_children += 1
        if print_it:
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
                # if color in visited_colors:  # 2 cards with same colors in 2 sections
                #     return False
                number = sec[0].get_number()
                for card in sec:
                    # checking the card number and colors in one section
                    if card.get_color() == color and card.get_number() <= number:
                        number = card.get_number()
                    else:
                        return False
                # visited_colors.append(color)
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
        elif sections[destination][-1].number > sections[origin][-1].number:
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


def breadth_first_search(init, print_it):
    print("----------------------------------------------------------------")
    print("RUNNING THE BREADTH FIRST SEARCH ALGORITHM")
    i = 1
    frontier.append(init)
    while True:
        if i % 200 == 0:
            print(".", end=" ")
        if i % (200 * 20) == 0:
            print()

        if print_it:
            print(i)
        if not frontier:
            print("failure!!!")
        if print_it:
            print("frontier:{}\nexplored:{}".format(len(frontier), len(explored)))

        candidate = frontier.pop(0)

        explored.append(candidate)

        if print_it:
            candidate.print_state()

        if candidate.goal_test():
            print("\nGOAL STATE FOUNDED!")
            return candidate
            # solution

        children = candidate.expand_children(print_it)
        for child in children:
            if child not in explored or child not in frontier:
                frontier.append(child)
        i += 1


if __name__ == '__main__':
    frontier = []
    explored = []
    number_of_children = 0
    # k = number of sections
    # m = number of colors
    # n = number of each color of cards (from )
    k, m, n = input().split()
    k, m, n = int(k), int(m), int(n)
    card_sections = []

    # we are going to have K sections.
    # the "card_sections" is the real and physical
    # card sections and is going to be modified after
    # finding the pattern to the goal state.
    card_sections = get_inputs(card_sections)

    # starting time
    start_time = time.time()

    # selected pattern from BFS search
    steps = []

    initial_state = State(card_sections, 0, None, -1, -1)

    goal_state = breadth_first_search(initial_state, False)

    # finishing time
    finish_time = time.time()

    depths = goal_state.get_depth()

    # # print(len(goal_state.get_parents()))
    # p = goal_state.get_parents()
    # for cc in p:
    #     print_cards(cc)

    # save the goal pattern
    while goal_state.get_parent() is not None:
        steps.insert(0, goal_state)
        goal_state = goal_state.get_parent()

    # print the results
    print("GOAL DEPTH: {}".format(depths))

    print("----------------------------------------------------------------")
    print("APPLYING THE PATTERN TO THE REAL CARD SECTIONS")
    print_cards(card_sections)
    for s in steps:
        # print_cards(s.get_cards_section() in p)
        card_sections = move_card(card_sections, s.get_move_from(), s.get_move_to(), True)
        print("STEP: {} / {}".format(s.get_depth(), depths))
        time.sleep(.5)

    print("\n*** Time spent finding solution to reach the goal: {}s".format(finish_time - start_time))
    print("*** Number of Explored Nodes: {}".format(len(explored)))
    print("*** Number of Produced Nodes: {}".format(number_of_children))

