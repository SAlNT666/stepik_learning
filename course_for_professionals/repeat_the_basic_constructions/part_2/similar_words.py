target_word = input()
words = (input() for _ in range(int(input())))
vowels = 'ауоыиэяюёе'

t_w_vowels_positions = [i for i, x in enumerate(target_word) if x in vowels]
print(*[w for w in words if t_w_vowels_positions == [i for i, x in enumerate(w) if x in vowels]], sep='\n')
