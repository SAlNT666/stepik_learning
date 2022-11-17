from zipfile import ZipFile


tg_date = (2021, 11, 30, 14, 22)

with ZipFile('workbook.zip') as zf_in:
    print(*sorted(f.filename.split('/')[-1] for f in
          filter(lambda x: not x.is_dir() and x.date_time > tg_date, zf_in.infolist())), sep='\n')
