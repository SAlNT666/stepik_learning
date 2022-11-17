class PowerOf:
    def __init__(self, number):
        self.number = number
        self.degree = -1
        self.results = {0: 1}

    def __iter__(self):
        return self

    def __next__(self):
        self.degree += 1
        new_res = self.results[self.degree] * self.number
        self.results[self.degree + 1] = new_res
        return self.results[self.degree]


power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
