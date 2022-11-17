from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(','))
spaces = len(max(order, key=len))
check = list()

total = 0
for i in sorted(order):
    total += ingredients[i] * order[i]
    check.append(f'{i.ljust(spaces)} x {order[i]}')

check.append(f'ИТОГ: {total}р')
print(*check[:-1], '-' * len(max(check, key=len)), check[-1], sep='\n')
