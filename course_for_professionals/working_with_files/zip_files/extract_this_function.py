from zipfile import ZipFile


def extract_this(zip_name: str, *args):
    if not args:
        args = None
    with ZipFile(zip_name) as zf_in:
        zf_in.extractall(members=args)
