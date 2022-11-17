row = '1kilg%rli8k'
row = ''.join(i for i in row if i.isalpha())


def almost_a_palindrome_or_not(row):
    row_length = len(row)
    half_of_the_string_length = int(row_length / 2)
    first_half_of_the_string = row[:half_of_the_string_length]
    second_half_of_the_string = row[:-half_of_the_string_length - 1:-1]

    if first_half_of_the_string == second_half_of_the_string:
        return True

    for i in range(half_of_the_string_length):
        if first_half_of_the_string[i] != second_half_of_the_string[i]:
            if first_half_of_the_string[i + 1:] == second_half_of_the_string[i:-1]\
                    or first_half_of_the_string[i:-1] == second_half_of_the_string[i + 1:]:
                return True
            else:
                return False
    return False


print(almost_a_palindrome_or_not(row))
