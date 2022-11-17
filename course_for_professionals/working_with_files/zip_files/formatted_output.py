from zipfile import ZipFile
from datetime import datetime


with ZipFile('workbook.zip') as zf_in:
    for f in sorted(filter(lambda x: not x.is_dir(), zf_in.infolist()), key=lambda y: y.filename.split('/')[-1].lower()):
        print(f.filename.split('/')[-1])
        print(f'  Дата модификации файла: {datetime(*f.date_time)}')
        print(f'  Объем исходного файла: {f.file_size} байт(а)')
        print(f'  Объем сжатого файла: {f.compress_size} байт(а)\n')
