from sys import stdin


heights = [int(h) for h in stdin]

if heights:
    print('Рост самого низкого ученика:', min(heights))
    print('Рост самого высокого ученика:', max(heights))
    print('Средний рост:', sum(heights) / len(heights))
else:
    print('нет учеников')
