func = input()
a, b = [int(i) for i in input().split()]
val_lst = [eval(func) for x in range(a, b + 1)]

print(f'Минимальное значение функции {func} на отрезке [{a}; {b}] равно {min(val_lst)}')
print(f'Максимальное значение функции {func} на отрезке [{a}; {b}] равно {max(val_lst)}')
