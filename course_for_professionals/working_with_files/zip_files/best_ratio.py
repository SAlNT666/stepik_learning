from zipfile import ZipFile


with ZipFile('workbook.zip') as zf_in:
    print(min(filter(lambda x: x.file_size, zf_in.infolist()), key=lambda x: x.compress_size / x.file_size).filename.split('/')[-1])
