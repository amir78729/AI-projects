class Cell:
    def __init__(self, num, col):
        self.num = num
        self.col = col

    def get_col(self):
        return self.col

    def get_num(self):
        return self.num

    def print_cell(self):
        print("{}{}\t".format(self.num, self.col), end='')


class State:
    def __init__(self, table):
        self.table = table

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
    print(initial_state.is_valid_by_number())




