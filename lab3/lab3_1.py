def line_base(nspace, ncol):
    for i in range(nspace):
        print(" ", end="")
    for i in range(ncol):
        print("#", end="")
    print()

if __name__ == "__main__":
    line_base(0, 3)
    line_base(1, 3)
    line_base(2, 5)
    line_base(3, 3)