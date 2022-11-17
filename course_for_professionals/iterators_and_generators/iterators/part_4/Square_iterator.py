class Square:
    def __new__(cls, n):
        return (i ** 2 for i in range(1, n + 1))


squares = Square(10)

print(list(squares))
