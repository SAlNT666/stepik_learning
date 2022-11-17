def hr_size(n, k=0):
    return f"{round(n)} {['B', 'KB', 'MB', 'GB', 'TB'][k]}" if n < 1024 else hr_size(n / 1024, k + 1)


with open('files.txt') as file:
    files = []
    for row in file:
        files.append(row.split())

units_dict = dict(B=1, KB=1024, MB=1024 ** 2, GB=1024 ** 3)
for ext in sorted(set(x[0][-x[0][::-1].find('.') - 1:] for x in files)):
    ext_length = len(ext)
    ext_weights = []
    files_with_current_ext = []
    for file in files:
        if file[0][-ext_length:] == ext:
            files_with_current_ext.append(file[0])
            ext_weights.append(int(file[1]) * units_dict[file[2]])
    print(*sorted(files_with_current_ext), sep='\n')
    print('----------\nSummary: ', end='')
    summary = sum(ext_weights)

    print(hr_size(summary) + '\n')

    # наверное, быстрее, но насколько уродливее
    # if summary >= 1024 ** 3:
    #     print(str(round(summary / 1024 ** 3)) + ' GB\n')
    # elif summary >= 1024 ** 2:
    #     print(str(round(summary / 1024 ** 2)) + ' MB\n')
    # elif summary >= 1024:
    #     print(str(round(summary / 1024)) + ' KB\n')
    # else:
    #     print(str(summary) + ' MB\n')
