class Cell:
    # constructor
    def __init__(self, num, col):
        self.num = num
        self.col = col
        self.conflict_set = []  # used for colors

    # getters
    def get_col(self):
        return self.col

    def get_num(self):
        return self.num

    # setters
    def set_col(self, col):
        self.col = col

    def set_num(self, num):
        self.num = num

    def add_to_conf(self, color):
        if not (color in self.conflict_set):
            self.conflict_set.append(color)

    def remove_from_conf(self, color):
        self.conflict_set.remove(color)

    def print_cell(self):
        print("{}{}\t".format(self.num, self.col), end='')


class State:
    # constructor
    def __init__(self, tlb):
        self.table = tlb

    ########################################################################
    # NUMBER
    ########################################################################

    # to check if num is in a row
    def used_in_row_number(self, row, num):
        q = []
        for i in range(n):
            if (self.table[row][i].get_num()) != '*':
                q.append(int(self.table[row][i].get_num()))
        # print('row {} :'.format(row))
        # print(q)
        return num in q

    # to check if num is in a column
    def used_in_col_number(self, col, num):
        q = []
        for i in range(n):
            if (self.table[i][col].get_num()) != '*':
                q.append(int(self.table[i][col].get_num()))
        # print('col {} :'.format(col))
        # print(q)
        return num in q

    def check_location_is_safe_number(self, row, col, num):
        return not self.used_in_row_number(row, num) and not self.used_in_col_number(col, num)

    def find_empty_location_number(self, l):
        for row in range(n):
            for col in range(n):
                if self.table[row][col].get_num() == '*':
                    l[0], l[1] = row, col
                    print('\t>>> LOCATION[{}][{}] IS EMPTY.'.format(row, col))
                    return True
        return False

    def solve_sudoku_number(self):
        # print("solve_sudoku")

        # used for empty locations
        tmp = [0, 0]

        # no empty locations!
        if not self.find_empty_location_number(tmp):
            return True

        row, col = tmp[0], tmp[1]

        # for 1 to n ...
        for num in range(1, n + 1):
            # if looks promising
            if self.check_location_is_safe_number(row, col, num):
                print('\t>>> LOCATION[{}][{}] IS SAFE FOR {}'.format(row, col, num))
                self.table[row][col].num = num
                self.print_table()
                # done
                if self.solve_sudoku_number():
                    return True
                # try again
                self.table[row][col].set_num('*')
        return False  # backtracking

    ########################################################################
    # COLORS
    ########################################################################
    def solve_sudoku_color(self):
        pass

    ########################################################################
    # OTHER METHODS
    ########################################################################
    def print_table(self):
        for i in range(n):
            print('\t\t', end='')
            for j in range(n):
                self.table[i][j].print_cell()
            print()
        print('- - - - - - - - - - - - - - - - - -')


def split_cell_input(string):
    color = ""
    number = ""
    for i in range(len(string)):
        if (string[i].isdigit() or
                string[i] == '*'):
            number = number + string[i]
        elif (('A' <= string[i] <= 'Z') or
              ('a' <= string[i] <= 'z') or
              string[i] == '#'):
            color += string[i]
    return number, color


def print_conf_table():
    for i in range(n):
        print('\t\t', end='')
        for j in range(n):
            print(conflict_table[i][j], end='\t\t')
        print('\n')
    print('- - - - - - - - - - - - - - - - - -')


if __name__ == '__main__':
    print('>>> SUDOKU+')
    print('\t>>> INPUTS:')
    m, n = map(int, input().split())  # m is number of colors and n is the size of table
    colors = list(map(str, input().strip().split()))[:m]  # getting colors from the user
    conflict_table = [[[] for i in range(n)] for j in range(n)]
    table = []
    for counter in range(n):
        row_input = list(map(str, input().strip().split()))[:n]
        r = []
        c = 0
        for cell_string in row_input:
            cell_number, cell_color = split_cell_input(cell_string)  # splitting the cell
            if cell_color != '#':
                conflict_table[counter][c] = '\"{}\"'.format(cell_color.upper())
            cell = Cell(cell_number, cell_color)  # creating the Cell object
            r.append(cell)
            c += 1
        table.append(r)

    game_state = State(table)
    print('>>> SOLVING SUDOKU BY NUMBERS')
    if game_state.solve_sudoku_number():
        game_state.print_table()
        print('>>> PART 1 (NUMBERS): DONE!')
    else:
        print('>>> THE PROBLEM HAS NO ANSWERS')

    print('= = = = = = = = = = = = = = = = = =')
    print('>>> SOLVING SUDOKU BY COLORS')

    # print_conf_table()

    #  initializing the conflict table
    for i in range(n):
        for j in range(n):
            if isinstance(conflict_table[i][j], str):
                for x in range(3):
                    for y in range(3):
                        index_x, index_y = x - 1, y - 1
                        if i + index_x >= 0 and j + index_y >= 0:
                            if not (index_x == 0 and index_y == 0):
                                try:
                                    if table[i][j].get_col() not in conflict_table[i + index_x][j + index_y]:
                                        conflict_table[i + index_x][j + index_y].append(table[i][j].get_col())
                                except (AttributeError, IndexError):
                                    pass
    # print_conf_table()

