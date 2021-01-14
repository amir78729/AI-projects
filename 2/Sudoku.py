class Cell:
    def __init__(self, num, col):
        self.num = num
        self.col = col

    def get_col(self):
        return self.col

    def get_num(self):
        return self.num


if __name__ == '__main__':
    m, n = map(int, input().split())  # m is number of colors and n is the size of table
    colors = list(map(str, input().strip().split()))[:m]
    print(colors)
    table = []
    for r in range(n):
        for c in range(n):
            

