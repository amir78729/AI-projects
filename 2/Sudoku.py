from copy import deepcopy
import time


def check_number(row, col, row_, col_):
    # if the neighbor cell has number AND color...
    if numbers_table[row_][col_] > 0 and colors_table[row_][col_] > 0:

        # if the number of current cell was greater than other cell but
        # the color priority was not, return 0.
        if numbers_table[row][col] > numbers_table[row_][col_] and \
                colors_table[row][col] > colors_table[row_][col_]:
            return 0

        # if the number of current cell was smaller than other cell but
        # the color priority was not, return 0.
        elif numbers_table[row][col] < numbers_table[row_][col_] and \
                colors_table[row][col] < colors_table[row_][col_]:
            return 0


def check_color(row, col, row_, col_, temp, colors_domain_copy):
    # if the number of the neighbor was smaller than current cell
    # then remove colors with higher priority from domain
    if numbers_table[row][col] > numbers_table[row_][col_]:
        for color in range(1, temp + 1):
            while True:
                try:
                    colors_domain_copy[row_][col_].remove(color)
                except ValueError:
                    break
    # if the number of the neighbor was greater than current cell
    # then remove colors with lower priority from domain
    else:
        for color in range(temp, m + 1):
            while True:
                try:
                    colors_domain_copy[row_][col_].remove(color)
                except ValueError:
                    break

    # if domains saw empty return 0
    if colors_table[row_][col_] == 0 and len(colors_domain_copy[row_][col_]) == 0:
        return 0


def forward_checking_for_colors(row, col, colors_table, colors_domain):
    colors_domain_copy = deepcopy(colors_domain)
    temp = colors_table[row][col]

    # check the left cell
    if col > 0:
        if check_color(row, col, row, col - 1, temp, colors_domain_copy) == 0:
            return 0

    # check the right cell
    if col < n - 1:
        if check_color(row, col, row, col + 1, temp, colors_domain_copy) == 0:
            return 0

    # check the top cell
    if row > 0:
        if check_color(row, col, row - 1, col, temp, colors_domain_copy) == 0:
            return 0

    # check the bottom cell
    if row < n - 1:
        if check_color(row, col, row + 1, col, temp, colors_domain_copy) == 0:
            return 0

    return colors_domain_copy


def forward_checking_for_numbers(row, col, num, numbers_domain, numbers_table):
    numbers_domain_copy = deepcopy(numbers_domain)
    for i in range(n):
        # remove the number from the cells in the same row or column
        while True:
            try:
                numbers_domain_copy[i][col].remove(num)
            except ValueError:
                break
        while True:
            try:
                numbers_domain_copy[row][i].remove(num)
            except ValueError:
                break

        # no value and empty domain
        if numbers_table[i][col] == 0 and len(numbers_domain_copy[i][col]) == 0 or\
                numbers_table[row][i] == 0 and len(numbers_domain_copy[row][i]) == 0:
            return 0

    # when a cell has color and number
    if numbers_table[row][col] > 0 and colors_table[row][col] > 0:
        # check the left cell
        if col > 0:
            if check_number(row, col, row, col - 1) == 0:
                return 0

        # check the right cell
        if col < n - 1:
            if check_number(row, col, row, col + 1) == 0:
                return 0

        # check the top cell
        if row > 0:
            if check_number(row, col, row - 1, col) == 0:
                return 0

        # check the bottom cell
        if row < n - 1:
            if check_number(row, col, row + 1, col) == 0:
                return 0

    return numbers_domain_copy


# get domain table return MRV chosen cell by colors
def mrv_heuristic_for_colors(numbers_domain_copy, table):
    mincond = m + 1
    candidates = []
    for i in range(n):
        for j in range(n):
            # the cell is empty
            if table[i][j] == 0:
                if len(numbers_domain_copy[i][j]) < mincond:
                    candidates.append([i, j])
                    mincond = len(numbers_domain_copy[i][j])
                elif len(numbers_domain_copy[i][j]) == mincond:
                    candidates.append([i, j])
    # no candidates found because all cells has a value
    if len(candidates) == 0:
        return [-1, -1]
    return degree_heuristic_for_colors(table, candidates)


# get domain table return MRV chosen cell by numbers
def mrv_heuristic_for_numbers(numbers_domain_copy, table):
    mincond = n + 1
    candidates = []
    for i in range(n):
        for j in range(n):
            # the cell is empty
            if table[i][j] == 0:
                if len(numbers_domain_copy[i][j]) < mincond:
                    candidates.append([i, j])
                    mincond = len(numbers_domain_copy[i][j])
                elif len(numbers_domain_copy[i][j]) == mincond:
                    candidates.append([i, j])
    # no candidates found because all cells has a value
    if len(candidates) == 0:
        return [-1, -1]
    return degree_heuristic_for_numbers(table, candidates)


#  assign a value to the variable that is involved in the
#  largest number of constraints on other unassigned variables (for numbers)
def degree_heuristic_for_numbers(table, candidates):
    maximum_degree = -1
    maxcell = []
    for cell in candidates:
        counts = 0
        for i in range(n):
            if table[i][cell[1]] == 0 or table[cell[0]][i] == 0:
                counts += 1
        if counts > maximum_degree:
            maxcell = cell
            maximum_degree = counts
    return maxcell


#  assign a value to the variable that is involved in the
#  largest number of constraints on other unassigned variables (for colors)
def degree_heuristic_for_colors(table, candidates):
    maximum_degree = -1
    maxcell = []
    for cell in candidates:
        counts = 0
        row = cell[0]
        col = cell[1]
        if col > 0:
            if table[row][col - 1] == 0:
                counts += 1
        if col < n - 1:
            if table[row][col + 1] == 0:
                counts += 1
        if row < n - 1:
            if numbers_table[row + 1][col] == 0:
                counts += 1
        if row > 0:
            if numbers_table[row - 1][col] == 0:
                counts += 1
        if counts > maximum_degree:
            maxcell = cell
            maximum_degree = counts
    return maxcell


def solve_sudoku_by_colors(table, colors_table, colors_domain):
    row, col = mrv_heuristic_for_colors(colors_domain, colors_table)
    # table is complete
    if row == -1:
        return 1
    for assinNum in colors_domain[row][col]:
        colors_table[row][col] = assinNum
        res = forward_checking_for_colors(row, col, colors_table, colors_domain)
        if res != 0:
            if solve_sudoku_by_colors(table, colors_table, res) != 0:
                return 1
    colors_table[row][col] = 0
    return 0


def solve_sudoku_by_numbers(numbers_table, numbers_domain, colors_table, colors_domain):
    row, col = mrv_heuristic_for_numbers(numbers_domain, numbers_table)
    # table is complete from numbers
    # now we need to solve the problem by colors
    if row == -1:
        if solve_sudoku_by_colors(numbers_table, colors_table, colors_domain) != 0:
            return 1
        return 0
    for n in numbers_domain[row][col]:
        numbers_table[row][col] = n
        res = forward_checking_for_numbers(row, col, n, numbers_domain, numbers_table)
        if res != 0:
            if solve_sudoku_by_numbers(numbers_table, res, colors_table, colors_domain) != 0:
                return 1
    numbers_table[row][col] = 0
    return 0


# arc consistency function used for colors
def arc_consistency(row, col):
    temp = colors_table[row][col]
    if col > 0:
        try:
            colors_domain[row][col - 1].remove(temp)
        except ValueError:
            pass
    if col < n - 1:
        try:
            colors_domain[row][col + 1].remove(temp)
        except ValueError:
            pass
    if row > 0:
        try:
            colors_domain[row - 1][col].remove(temp)
        except ValueError:
            pass
    if row < n - 1:
        try:
            colors_domain[row + 1][col].remove(temp)
        except ValueError:
            pass
    return colors_domain


def print_result(numbers_table, colors_table):
    for i in range(n):
        print('\t', end='')
        for j in range(n):
            print('\t{}{}'.format(numbers_table[i][j], input_colors[colors_table[i][j] - 1]), end='')
        print()


if __name__ == '__main__':
    print('>>> SUDOKU+')
    while True:
        try:
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
            print('\t>>> ENTER THE INPUTS: (PRINT Q TO EXIT)')

            # getting n and m from the user
            m, n = map(int, input().split())
            colors = dict()

            # getting the colors of the problem
            input_colors = input().split()
            for i in range(m):
                colors[input_colors[i]] = i + 1
            colors['0'] = 0

            # initializing data tables
            numbers_table, colors_table = [[0 for i in range(n)] for j in range(n)],\
                                          [[0 for i in range(n)] for j in range(n)]

            # initializing domain tables
            numbers_domain, colors_domain = [[0 for i in range(n)] for j in range(n)],\
                                            [[0 for i in range(n)] for j in range(n)]

            # putting data in data tables
            for i in range(n):
                line = input().split()
                for j in range(n):
                    # empty color for the cell
                    if line[j][1] == '#':
                        colors_table[i][j] = colors['0']
                    else:
                        try:
                            colors_table[i][j] = colors[line[j][1]]
                        except KeyError:
                            print('\t>>> WRONG COLOR DETECTED!!')
                            continue
                    # empty number for the cell
                    if line[j][0] == '*':
                        numbers_table[i][j] = 0
                    else:
                        numbers_table[i][j] = int(line[j][0])
            print('\t>>> STARTING THE ALGORITHM...')
            starting_time = time.time()
            print('\t>>> TIMER IS ACTIVATED')
            print('\t>>> SET THE DOMAINS (NUMBERS):', end=' ')
            # set the domains (for numbers)
            for i in range(n):
                for j in range(n):
                    if numbers_table[i][j] == 0:
                        numbers_domain[i][j] = list(range(1, n + 1))
                    else:
                        numbers_domain[i][j] = [0]
            print('DONE')
            print('\t>>> SET THE DOMAINS (COLORS):', end=' ')
            # set the domains (for colors)
            for i in range(n):
                for j in range(n):
                    if colors_table[i][j] == 0:
                        colors_domain[i][j] = list(range(1, m + 1))
                    else:
                        colors_domain[i][j] = [0]
            print('DONE')

            print('\t>>> ARC CONSISTENCY (NUMBERS):', end=' ')
            # arc consistency (for numbers)
            for i in range(n):
                for j in range(n):
                    if numbers_table[i][j] != 0:  # there is a number in the cell!
                        for k in range(n):
                            tmp = numbers_table[i][j]
                            while True:
                                try:
                                    numbers_domain[i][k].remove(tmp)
                                except ValueError:
                                    break
                            while True:
                                try:
                                    numbers_domain[k][j].remove(tmp)
                                except ValueError:
                                    break
            print('DONE')

            print('\t>>> ARC CONSISTENCY (COLORS):', end=' ')
            # arc consistency (for colors)
            for i in range(n):
                for j in range(n):
                    if colors_table[i][j] != 0:  # there is a color in the cell!
                        colors_domain = arc_consistency(i, j)

            print('DONE')
            result = solve_sudoku_by_numbers(numbers_table, numbers_domain, colors_table, colors_domain)
            print('\t>>> ALGORITHM HAS BEEN FINISHED')
            ending_time = time.time()
            print('\t>>> TIMER IS STOPPED')
            print('\t\t>>> CALCULATION TIME: {}s'.format(ending_time - starting_time))
            if result == 1:
                print('\t>>> SHOWING THE RESULT\n')
                print_result(numbers_table, colors_table)
            else:
                print('\t>>> THE PROBLEM HAS NO ANSWERS\n')
        except ValueError:
            print('\t>>> END OF THE PROGRAM')
            break


