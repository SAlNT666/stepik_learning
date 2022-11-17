from zipfile import ZipFile


with ZipFile('workbook.zip') as zf_in:
    print(f'Объем исходных файлов: {sum(f.file_size for f in zf_in.infolist())} байт(а)')
    print(f'Объем сжатых файлов: {sum(f.compress_size for f in zf_in.infolist())} байт(а)')
