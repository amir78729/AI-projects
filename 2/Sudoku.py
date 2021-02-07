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

#prototype
def sazegar_konande_yek_cell(row,col,colors_table,cdt,numbers_table,m):
    colors_domain = copy.deepcopy(cdt)
    temp = colors_table[row][col]
    if col>0:
        if numbers_table[row][col] > numbers_table[row][col-1]:
            for color in range(1,temp):
                while True:
                    try:
                        colors_domain[row][col-1].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp,m+1):
                while True:
                    try:
                        colors_domain[row][col-1].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colors_domain[row][col-1].remove(temp)
            except ValueError:
                break
        if colors_table[row][col-1] == 0 and len(colors_domain[row][col - 1]) == 0 or\
                colors_table[row][col - 1] == 0 and len(colors_domain[row][col - 1]) == 0:
            return 0
    if col < n - 1:
        if numbers_table[row][col] > numbers_table[row][col+1]:
            for color in range(1, temp):
                while True:
                    try:
                        colors_domain[row][col+1].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp, m + 1):
                while True:
                    try:
                        colors_domain[row][col+1].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colors_domain[row][col+1].remove(temp)
            except ValueError:
                break
        if colors_table[row][col + 1] == 0 and len(colors_domain[row][col+1]) == 0 or \
                colors_table[row][col + 1] == 0 and len(colors_domain[row][col+1]) == 0:
            return 0
    if row > 0:
        if numbers_table[row][col] > numbers_table[row-1][col]:
            for color in range(1, temp):
                while True:
                    try:
                        colors_domain[row-1][col].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp, m + 1):
                while True:
                    try:
                        colors_domain[row-1][col].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colors_domain[row-1][col].remove(temp)
            except ValueError:
                break
        if colors_table[row - 1][col] == 0 and len(colors_domain[row - 1][col]) == 0 or\
                colors_table[row - 1][col] == 0 and len(colors_domain[row - 1][col]) == 0:
            return 0
    if row < n - 1:
        if numbers_table[row][col] > numbers_table[row+1][col]:
            for color in range(1, temp):
                while True:
                    try:
                        colors_domain[row+1][col].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp, m+1):
                while True:
                    try:
                        colors_domain[row+1][col].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colors_domain[row+1][col].remove(temp)
            except ValueError:
                break
        if (colors_table[row+1][col] == 0 and len(colors_domain[row+1][col])==0) or (colors_table[row+1][col]==0 and len(colors_domain[row+1][col])==0):
            return 0
    return colors_domain


def forwadChecking(row,col,num,dt,table,colotrable):
    domainTable = copy.deepcopy(dt)
    for i in range(n):
        while True:
            try:
                domainTable[i][col].remove(num)
            except ValueError:
                break
        while True:
            try:
                domainTable[row][i].remove(num)
            except ValueError:
                break

    if table[i][col] == 0 and len(domainTable[i][col]) == 0 or table[row][i] == 0 and len(domainTable[row][i]) == 0:
        return 0
        # if tow side cell has color and num:
    if numbers_table[row][col] > 0 and colors_table[row][col] > 0:
        if col > 0:
            if numbers_table[row][col - 1] > 0 and colors_table[row][col - 1] > 0:
                if numbers_table[row][col] > numbers_table[row][col - 1] and colors_table[row][col] > colors_table[row][col - 1]:
                    return 0
                elif numbers_table[row][col] < numbers_table[row][col - 1] and colors_table[row][col] < colors_table[row][col - 1]:
                    return 0
        if col < n - 1:
            if numbers_table[row][col + 1] > 0 and colors_table[row][col + 1] > 0:
                if numbers_table[row][col] > numbers_table[row][col + 1] and colors_table[row][col] > colors_table[row][col + 1]:
                    return 0
                elif numbers_table[row][col] < numbers_table[row][col + 1] and colors_table[row][col] < colors_table[row][col + 1]:
                    return 0
        if row < n - 1:
            if numbers_table[row + 1][col] > 0 and colors_table[row + 1][col] > 0:
                if numbers_table[row][col] > numbers_table[row + 1][col] and colors_table[row][col] > colors_table[row + 1][col]:
                    return 0
                elif numbers_table[row][col] < numbers_table[row + 1][col] and colors_table[row][col] < colors_table[row + 1][col]:
                    return 0
        if row > 0:
            if numbers_table[row - 1][col] > 0 and colors_table[row - 1][col] > 0:
                if numbers_table[row][col] > numbers_table[row - 1][col] and colors_table[row][col] > colors_table[row - 1][col]:
                    return 0
                elif numbers_table[row][col] < numbers_table[row - 1][col] and colors_table[row][col] < colors_table[row - 1][col]:
                    return 0

    return domainTable


# get domain table return MRV chosen cell
def mrv_heuristic(domainTable, table, maxlen, numORColor):
    mincond = maxlen + 1
    mincell = []
    resault = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 0:
                if len(domainTable[i][j]) < mincond:
                    mincell = []
                    mincell.append([i, j])
                    mincond = len(domainTable[i][j])
                elif len(domainTable[i][j]) == mincond:
                    mincell.append([i, j])
    if len(mincell) == 0:
        return [-1, -1]
    if numORColor == 1:
        resault = degreeNum(domainTable, table, mincell)
    else:
        resault = degreeColor(domainTable, table, mincell)
    return resault


def degreeNum(domaintable, table, candids):
    n = len(table)
    maximum_degree = -1
    maxcell = []
    for cell in candids:
        counts = 0
        for i in range(n):
            if table[i][cell[1]] == 0 or table[cell[0]][i] == 0:
                counts += 1
        if counts > maximum_degree:
            maxcell = cell
            maximum_degree = counts
    return maxcell


def degreeColor(domaintable, table, candids):
    n = len(table)
    maximum_degree = -1
    maxcell = []
    for cell in candids:
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


def co(table, colors_table, colors_domain, m):
    row, col = mrv_heuristic(colors_domain, colors_table, m, 0)
    if row == -1:
        # colors filled
        return 1
    for assinNum in colors_domain[row][col]:
        colors_table[row][col] = assinNum
        updated = sazegar_konande_yek_cell(row, col, colors_table, colors_domain, table, m)
        if (updated != 0):
            if co(table, colors_table, updated, m) != 0:
                return 1
    colors_table[row][col] = 0
    return 0


def f(table, domainTable, colors_table, colors_domain, m, n):
    row, col = mrv_heuristic(domainTable, table, n, 1)
    if row == -1:
        # nums filled
        if co(table, colors_table, colors_domain, m) != 0:
            return 1
        return 0
    for assinNum in domainTable[row][col]:
        table[row][col] = assinNum
        updated = forwadChecking(row, col, assinNum, domainTable, table, colors_table)
        if (updated != 0):
            if f(table, updated, colors_table, colors_domain, m, n) != 0:
                return 1
    table[row][col] = 0
    return 0


def sazegar_kaman(row, col, colors_table, colors_domain, numbers_table):
    temp = colors_table[row][col]
    if col > 0:
        while True:
            try:
                colors_domain[row][col - 1].remove(temp)
            except ValueError:
                break
    if col < n - 1:
        while True:
            try:
                colors_domain[row][col + 1].remove(temp)
            except ValueError:
                break
    if row > 0:
        while True:
            try:
                colors_domain[row - 1][col].remove(temp)
            except ValueError:
                break
    if row < n - 1:
        while True:
            try:
                colors_domain[row + 1][col].remove(temp)
            except ValueError:
                break
    return colors_domain


if __name__ == '__main__':

    # getting n and m from the user
    m, n = map(int, input().split())
    colors = dict()

    # getting the colors of the problem
    input_colors = input().split()
    for i in range(m):
        colors[input_colors[i]] = i + 1
    colors['0'] = 0

    # initializing data tables
    numbers_table, colors_table = [[0 for i in range(n)] for j in range(n)], [[0 for i in range(n)] for j in range(n)]

    # initializing domain tables
    numbers_domain, colors_domain = [[0 for i in range(n)] for j in range(n)], [[0 for i in range(n)] for j in range(n)]

    # putting data in data tables
    for i in range(n):
        s = input().split()
        for j in range(n):
            # empty color for the cell
            if s[j][1] == '#':
                colors_table[i][j] = colors['0']
            else:
                colors_table[i][j] = colors[s[j][1]]
            # empty number for the cell
            if s[j][0] == '*':
                numbers_table[i][j] = 0
            else:
                numbers_table[i][j] = int(s[j][0])

    # set the domains (for numbers)
    for i in range(n):
        for j in range(n):
            if numbers_table[i][j] == 0:
                numbers_domain[i][j] = list(range(1, n + 1))
            else:
                numbers_domain[i][j] = [0]

    # set the domains (for colors)
    for i in range(n):
        for j in range(n):
            if colors_table[i][j] == 0:
                colors_domain[i][j] = list(range(1, m + 1))
            else:
                colors_domain[i][j] = [0]

    # arc consistency for numbers
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

    # arc consistency for colors
    for i in range(n):
        for j in range(n):
            if colors_table[i][j] != 0:  # there is a color in the cell!
                colors_domain = sazegar_kaman(i, j, colors_table, colors_domain, numbers_table)

    f(numbers_table, numbers_domain, colors_table, colors_domain, m, n)

    print(numbers_table)
    print(colors_table)
