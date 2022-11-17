from zipfile import ZipFile


with ZipFile('workbook.zip') as zf_in:
    print(sum(not file.is_dir() for file in zf_in.infolist()))
