from lab3_1 import line_base

def line(col):
    line_base(0, col)

def block(row, col):
    for i in range(row):
        line(col)

if __name__ == "__main__":
    block(5, 10)