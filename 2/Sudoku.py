class Cell:
    def __init__(self, num, col):
        self.num = num
        self.col = col

    def get_col(self):
        return self.col

    def get_num(self):
        return self.num


if __name__ == '__main__':
    sudoku_table = []
    m, n = map(int, input().split()) # 
