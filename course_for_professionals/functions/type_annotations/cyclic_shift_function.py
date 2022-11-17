from collections import deque


def cyclic_shift(numbers_: list[int | float], step: int) -> None:
    global numbers
    numbers = deque(numbers)
    numbers.rotate(step)
    numbers = list(numbers)

# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     step %= len(numbers)
#     if step > 0: [numbers.insert(0, numbers.pop(len(numbers) - 1)) for _ in range(step)]
#     elif step < 0: [numbers.insert(len(numbers), numbers.pop(0)) for _ in range(abs(step))]


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)