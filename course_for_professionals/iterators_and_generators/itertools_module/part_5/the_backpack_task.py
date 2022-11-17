from collections import namedtuple
import itertools

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

# load_capacity = int(input())
capacity = 500

potential_items = [i for i in items if i.mass <= capacity]
combs = [c for r in range(len(potential_items) + 1) for c in itertools.combinations(potential_items, r)
         if sum(i.mass for i in c) <= capacity]

if not combs or not [print(i.name) for i in sorted(max(combs, key=lambda c: sum(i.price for i in c)), key=lambda x: x.name)]:
    print('Рюкзак собрать не удастся')
