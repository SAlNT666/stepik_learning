old_mails = [input() for _ in range(int(input()))]
new_names = [input() for _ in range(int(input()))]


for name in new_names:
    new_name = name + '@beegeek.bzz'

    counter = 1
    while new_name in old_mails:
        new_name = name + str(counter) + '@beegeek.bzz'
        counter += 1

    print(new_name)
    old_mails.append(new_name)
