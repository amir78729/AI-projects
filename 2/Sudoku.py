import time
import copy


class Cell:
    # constructor
    def __init__(self, num, col):
        self.num = num
        self.col = col
        # self.number_domain = []  # used for numbers
        # self.color_domain = []  # used for colors

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

    def mrv_for_numbers(self, l):
        for row in range(n):
            for col in range(n):
                if self.table[row][col].get_num() == '*':
                    l[0], l[1] = row, col
                    # print('\t>>> LOCATION[{}][{}] IS EMPTY '.format(row, col), end='')
                    return True
        return False

    def solve_sudoku_number(self):
        # used for empty locations
        tmp = [0, 0]

        # no empty locations!
        if not self.mrv_for_numbers(tmp):
            return True

        row, col = tmp[0], tmp[1]

        # for 1 to n ...
        for num in range(1, n + 1):
            # if looks promising
            if self.check_location_is_safe_number(row, col, num):
                # print('AND IS SAFE FOR {}'.format(row, col, num))
                self.table[row][col].num = num
                # self.print_table()
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


def print_domains():
    print('color domain')
    for i in range(n):
        print('\t\t', end='')
        for j in range(n):
            print(color_domain[i][j], end='\t\t')
        print('\n')
    print('- - - - - - - - - - - - - - - - - -')
    print('number domain')
    for i in range(n):
        print('\t\t', end='')
        for j in range(n):
            print(number_domain[i][j], end='\t\t')
        print('\n')
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


if __name__ == '__main__':

    print('>>> SUDOKU+')
    print('\t>>> INPUTS:')
    m, n = map(int, input().split())  # m is number of colors and n is the size of table
    colors = list(map(str, input().strip().split()))[:m]  # getting colors from the user
    # conflict_table = [[[] for i in range(n)] for j in range(n)]
    color_domain = [[copy.deepcopy(colors) for i in range(n)] for j in range(n)]
    number_domain = [[[item for item in range(1, n + 1)] for i in range(n)] for j in range(n)]
    table = []
    for counter in range(n):
        row_input = list(map(str, input().strip().split()))[:n]
        r = []
        c = 0
        for cell_string in row_input:
            cell_number, cell_color = split_cell_input(cell_string)  # splitting the cell
            if cell_color != '#':
                #  initializing the color domain
                color_domain[counter][c] = cell_color
                if isinstance(color_domain[counter][c], str):
                    print(color_domain[counter][c])
                    for x in range(3):
                        for y in range(3):
                            index_x, index_y = x - 1, y - 1

                            if counter + index_x >= 0 and c + index_y >= 0:
                                try:
                                    print('color_domain[{}][{}] = {}'.format(counter + index_x, c + index_y, color_domain[counter + index_x][c + index_y]))
                                except:
                                    pass
                                if not (index_x == 0 and index_y == 0):
                                    try:
                                        print('lll')
                                        if color_domain[counter][c] in color_domain[counter + index_x][c + index_y]:
                                            color_domain[counter + index_x][c + index_y].remove(color_domain[counter][c])
                                    except (AttributeError, IndexError):
                                        pass

            if cell_number != '*':
                #  initializing the number domain
                number_domain[counter][c] = cell_number
                for rr in range(n):
                    if isinstance(number_domain[rr][c], list):
                        if rr != counter:
                            try:
                                number_domain[rr][c].remove(int(cell_number))
                            except:
                                pass
                for cc in range(n):
                    if isinstance(number_domain[counter][cc], list):
                        if cc != c:
                            try:
                                number_domain[counter][cc].remove(int(cell_number))
                            except:
                                pass

                # for rr in range(n):
                #     if rr != counter:
                #         if cell_number in number_domain[rr][c]:
                #             number_domain[rr][c].remove(cell_number)
                #     if rr != c:
                #         if cell_number in number_domain[counter][rr]:
                #             number_domain[counter][rr].remove(cell_number)


            cell = Cell(cell_number, cell_color)  # creating the Cell object
            r.append(cell)
            c += 1
        table.append(r)
    start = time.time()
    game_state = State(table)



    print('>>> SOLVING SUDOKU BY NUMBERS')
    if game_state.solve_sudoku_number():
        game_state.print_table()
        print('>>> PART 1 (NUMBERS): DONE!')
    else:
        print('>>> THE PROBLEM HAS NO ANSWERS')

    print('= = = = = = = = = = = = = = = = = =')
    print('>>> SOLVING SUDOKU BY COLORS')


    # #  initializing the domain table for numbers
    # for i in range(n):
    #     for j in range(n):
    #         if not isinstance(number_domain[i][j], str):
    #             for x in range(n):
    #                 if game_state.check_location_is_safe_number(i, j, x + 1):
    #                     number_domain[i][j].append(x)
    #                 else:
    #                     number_domain[i][j].append(-1)
    #
    # #  initializing the domain table for colors
    # for i in range(n):
    #     for j in range(n):
    #         if isinstance(color_domain[i][j], str):
    #
    #             for x in range(3):
    #                 for y in range(3):
    #                     index_x, index_y = x - 1, y - 1
    #
    #                     if i + index_x >= 0 and j + index_y >= 0:
    #                         if not (index_x == 0 and index_y == 0):
    #                             try:
    #
    #                                 if table[i][j].get_col() in color_domain[i + index_x][j + index_y]:
    #                                     color_domain[i + index_x][j + index_y].remove(table[i][j].get_col())
    #                             except (AttributeError, IndexError):
    #                                 pass
    print_domains()
    end = time.time()
    print((end - start))
