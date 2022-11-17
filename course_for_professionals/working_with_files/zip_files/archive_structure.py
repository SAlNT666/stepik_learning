from zipfile import ZipFile


def hr_size(n, k=0):
    return f"{round(n)} {['B', 'KB', 'MB', 'GB', 'TB'][k]}" if n < 1024 else hr_size(n / 1024, k + 1)


with ZipFile('desktop.zip') as zf_in:
    for i in zf_in.infolist():
        i_name = p = i.filename.strip('/').split('/')
        print('  ' * (len(i_name) - 1) + i_name[-1] + ('' if i.is_dir() else ' ' + hr_size(i.file_size)))
