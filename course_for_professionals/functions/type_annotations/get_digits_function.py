def get_digits(number: int | float) -> list[int]:
    return [int(d) for d in str(number) if d.isdigit()]
