from operator import le, ge


class Xrange:
    def __init__(self, start, end, step=1):
        self.step = step
        self.end = end
        self.start = start - step
        self.condition = (le, ge)[step < 0]

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.condition(self.end, self.start):
            raise StopIteration
        return self.start


evens = Xrange(0, 10, 2)

print(*evens)
