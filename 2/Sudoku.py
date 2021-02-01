class Cell:
    def __init__(self, num, col):
        self.num = num
        self.col = col

    def get_col(self):
        return self.col

    def get_num(self):
        return self.num

    def set_col(self, col):
        self.col = col

    def set_num(self, num):
        self.num = num

    def print_cell(self):
        print("{}{}\t".format(self.num, self.col), end='')


class State:
    def __init__(self, table):
        self.table = table

    # Returns a boolean which indicates
    # whether any assigned entry
    # in the specified row matches
    # the given number.
    def used_in_row(self, row, num):
        for i in range(n):
            if self.table[row][i].get_num() == num:
                return True
        return False

    # Returns a boolean which indicates
    # whether any assigned entry
    # in the specified column matches
    # the given number.
    def used_in_col(self, col, num):
        for i in range(n):
            if self.table[i][col].get_num() == num:
                return True
        return False

    def check_location_is_safe(self, row, col, num):

        # Check if 'num' is not already
        # placed in current row,
        # current column and current 3x3 box
        return not self.used_in_row(row, num) and not self.used_in_col(col, num)

    def find_empty_location(self, l):
        for row in range(n):
            for col in range(n):
                if self.table[row][col].get_num() == '*':
                    l[0] = row
                    l[1] = col
                    return True
        return False

    def solve_sudoku(self):

        # 'l' is a list variable that keeps the
        # record of row and col in
        # find_empty_location Function
        l = [0, 0]

        # If there is no unassigned
        # location, we are done
        if not self.find_empty_location(l):
            return True

        # Assigning list values to row and col
        # that we got from the above Function
        row = l[0]
        col = l[1]

        # consider digits 1 to n
        for num in range(1, n + 1):

            # if looks promising
            if self.check_location_is_safe(row, col, num):

                # make tentative assignment
                self.table[row][col].set_num(num)

                # return, if success,
                # ya !
                if self.solve_sudoku:
                    return True

                # failure, unmake & try again
                self.table[row][col].set_num('*')

        # this triggers backtracking
        return False

    def is_valid_by_number(self):
        for i in range(n):  # Elements on the main diameter
            d = self.table[i][i].get_num()
            if d != '*':
                row, col = [], []
                row.append(d)
                col.append(d)
                for j in range(n):
                    if j != i:
                        r, c = self.table[i][j].get_num(), self.table[j][i].get_num()
                        if r != '*':
                            if r in row:
                                return False
                            else:
                                row.append(r)
                        if c != '*':
                            if c in col:
                                return False
                            else:
                                row.append(c)
        return True

    def print_table(self):
        for i in range(n):
            for j in range(n):
                self.table[i][j].print_cell()
            print()


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
    m, n = map(int, input().split())  # m is number of colors and n is the size of table
    colors = list(map(str, input().strip().split()))[:m]  # getting colors from the user
    print(colors)
    table = []
    for i in range(n):
        row_input = list(map(str, input().strip().split()))[:n]
        row = []
        for cell_string in row_input:
            cell_number, cell_color = split_cell_input(cell_string)  # splitting the cell
            cell = Cell(cell_number, cell_color)  # creating the Cell object
            row.append(cell)
        table.append(row)

    initial_state = State(table)
    initial_state.print_table()
    print(initial_state.solve_sudoku())
    initial_state.print_table()
    print(initial_state.is_valid_by_number())





