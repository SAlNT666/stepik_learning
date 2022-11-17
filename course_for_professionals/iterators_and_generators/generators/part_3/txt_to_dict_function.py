def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as f_in:
        planet_info = dict()
        for line in f_in:
            if line.strip():
                planet_info[line.split(' = ')[0]] = line.strip().split(' = ')[1]
            else:
                yield planet_info
                planet_info = dict()

        yield planet_info


planets = txt_to_dict()

print(*planets)
