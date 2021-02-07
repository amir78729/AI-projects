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
def sazegar_konande_yek_cell(row,col,colortable,cdt,numtable,m):
    colordomainTable = copy.deepcopy(cdt)
    temp = colortable[row][col]
    if col>0:
        if numtable[row][col] > numtable[row][col-1]:
            for color in range(1,temp):
                while True:
                    try:
                        colordomainTable[row][col-1].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp,m+1):
                while True:
                    try:
                        colordomainTable[row][col-1].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colordomainTable[row][col-1].remove(temp)
            except ValueError:
                break
        if colortable[row][col-1] == 0 and len(colordomainTable[row][col - 1]) == 0 or\
                colortable[row][col - 1] == 0 and len(colordomainTable[row][col - 1]) == 0:
            return 0
    if col < n - 1:
        if numtable[row][col] > numtable[row][col+1]:
            for color in range(1, temp):
                while True:
                    try:
                        colordomainTable[row][col+1].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp, m + 1):
                while True:
                    try:
                        colordomainTable[row][col+1].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colordomainTable[row][col+1].remove(temp)
            except ValueError:
                break
        if colortable[row][col + 1] == 0 and len(colordomainTable[row][col+1]) == 0 or \
                colortable[row][col + 1] == 0 and len(colordomainTable[row][col+1]) == 0:
            return 0
    if row > 0:
        if numtable[row][col] > numtable[row-1][col]:
            for color in range(1, temp):
                while True:
                    try:
                        colordomainTable[row-1][col].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp,m+1):
                while True:
                    try:
                        colordomainTable[row-1][col].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colordomainTable[row-1][col].remove(temp)
            except ValueError:
                break
        if (colortable[row-1][col]==0 and len(colordomainTable[row-1][col])==0) or (colortable[row-1][col]==0 and len(colordomainTable[row-1][col])==0):
            return 0
    if row<n-1:
        if numtable[row][col] > numtable[row+1][col]:
            for color in range(1,temp):
                while True:
                    try:
                        colordomainTable[row+1][col].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp,m+1):
                while True:
                    try:
                        colordomainTable[row+1][col].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colordomainTable[row+1][col].remove(temp)
            except ValueError:
                break
        if (colortable[row+1][col] == 0 and len(colordomainTable[row+1][col])==0) or (colortable[row+1][col]==0 and len(colordomainTable[row+1][col])==0):
            return 0
    return colordomainTable


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
    if numtable[row][col] > 0 and colortable[row][col] > 0:
        if col > 0:
            if numtable[row][col - 1] > 0 and colortable[row][col - 1] > 0:
                if (numtable[row][col] > numtable[row][col - 1] and colortable[row][col] > colortable[row][col - 1]):
                    return 0
                elif (numtable[row][col] < numtable[row][col - 1] and colortable[row][col] < colortable[row][col - 1]):
                    return 0
        if col < n - 1:
            if numtable[row][col + 1] > 0 and colortable[row][col + 1] > 0:
                if (numtable[row][col] > numtable[row][col + 1] and colortable[row][col] > colortable[row][col + 1]):
                    return 0
                elif (numtable[row][col] < numtable[row][col + 1] and colortable[row][col] < colortable[row][col + 1]):
                    return 0
        if row < n - 1:
            if numtable[row + 1][col] > 0 and colortable[row + 1][col] > 0:
                if (numtable[row][col] > numtable[row + 1][col] and colortable[row][col] > colortable[row + 1][col]):
                    return 0
                elif (numtable[row][col] < numtable[row + 1][col] and colortable[row][col] < colortable[row + 1][col]):
                    return 0
        if row > 0:
            if numtable[row - 1][col] > 0 and colortable[row - 1][col] > 0:
                if (numtable[row][col] > numtable[row - 1][col] and colortable[row][col] > colortable[row - 1][col]):
                    return 0
                elif (numtable[row][col] < numtable[row - 1][col] and colortable[row][col] < colortable[row - 1][col]):
                    return 0

    return domainTable


# get domain table return MRV chosen cell
def MRV(domainTable, table, maxlen, numORColor):
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
            if numtable[row + 1][col] == 0:
                counts += 1
        if row > 0:
            if numtable[row - 1][col] == 0:
                counts += 1
        if counts > maximum_degree:
            maxcell = cell
            maximum_degree = counts
    return maxcell


def co(table, colortable, colordomainTable, m):
    row, col = MRV(colordomainTable, colortable, m, 0)
    if row == -1:
        # colors filled
        return 1
    for assinNum in colordomainTable[row][col]:
        colortable[row][col] = assinNum
        updated = sazegar_konande_yek_cell(row, col, colortable, colordomainTable, table, m)
        if (updated != 0):
            if co(table, colortable, updated, m) != 0:
                return 1
    colortable[row][col] = 0
    return 0


def f(table, domainTable, colortable, colordomainTable, m, n):
    row, col = MRV(domainTable, table, n, 1)
    if row == -1:
        # nums filled
        if co(table, colortable, colordomainTable, m) != 0:
            return 1
        return 0
    for assinNum in domainTable[row][col]:
        table[row][col] = assinNum
        updated = forwadChecking(row, col, assinNum, domainTable, table, colortable)
        if (updated != 0):
            if f(table, updated, colortable, colordomainTable, m, n) != 0:
                return 1
    table[row][col] = 0
    return 0


def sazegar_kaman(row, col, colortable, colordomainTable, numtable):
    temp = colortable[row][col]
    if col > 0:
        while True:
            try:
                colordomainTable[row][col - 1].remove(temp)
            except ValueError:
                break
    if col < n - 1:
        while True:
            try:
                colordomainTable[row][col + 1].remove(temp)
            except ValueError:
                break
    if row > 0:
        while True:
            try:
                colordomainTable[row - 1][col].remove(temp)
            except ValueError:
                break
    if row < n - 1:
        while True:
            try:
                colordomainTable[row + 1][col].remove(temp)
            except ValueError:
                break
    return colordomainTable


if __name__ == '__main__':
    m, n = map(int, input().split())
    colors = dict()

    temp = input().split()
    for i in range(m):
        colors[temp[i]] = i + 1
    colors['0'] = 0

    # initialization
    numtable = [[0 for i in range(n)] for j in range(n)]
    numdomainTable = [[0 for i in range(n)] for j in range(n)]

    colortable = [[0 for i in range(n)] for j in range(n)]
    colordomainTable = [[0 for i in range(n)] for j in range(n)]

    # fill the main table of nums and colors
    for i in range(n):
        s = input().split()
        for j in range(n):
            if (s[j][1] == '#'):
                colortable[i][j] = colors['0']
            else:
                colortable[i][j] = colors[s[j][1]]
            if s[j][0] == '*':
                numtable[i][j] = 0
            else:
                numtable[i][j] = int(s[j][0])

    # دامنه
    for i in range(n):
        for j in range(n):
            if numtable[i][j] == 0:
                numdomainTable[i][j] = list(range(1, n + 1))
            else:
                numdomainTable[i][j] = [0]

    for i in range(n):
        for j in range(n):
            if colortable[i][j] == 0:
                colordomainTable[i][j] = list(range(1, m + 1))
            else:
                colordomainTable[i][j] = [0]

    # سازگار کمان
    for i in range(n):
        for j in range(n):
            if numtable[i][j] != 0:
                for k in range(n):
                    temp = numtable[i][j]
                    while True:
                        try:
                            numdomainTable[i][k].remove(temp)
                        except ValueError:
                            break
                    while True:
                        try:
                            numdomainTable[k][j].remove(temp)
                        except ValueError:
                            break

    # سازگار کمان رنگی
    for i in range(n):
        for j in range(n):
            if colortable[i][j] != 0:
                colordomainTable = sazegar_kaman(i, j, colortable, colordomainTable, numtable)

    f(numtable, numdomainTable, colortable, colordomainTable, m, n)

    print(numtable)
    print(colortable)