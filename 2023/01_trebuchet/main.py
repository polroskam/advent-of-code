import re

DIGITS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def part_1():
    array = import_data('2023/01_trebuchet/input.txt')
    final_digits = []

    for row in array:
        # Find all digits, only the numbers
        regex = "(?=(" + '|'.join(DIGITS.values()) + "))"
        digits = re.findall(regex, row)

        first = digits[0]
        last = digits[-1]

        final_digits.append(int(first + last))

    return sum(final_digits)

def part_2():
    array = import_data('2023/01_trebuchet/input.txt')
    final_digits = []

    for row in array:
        digits_together = list(DIGITS.values()) + list(DIGITS.keys())

        # Find all digits, both words and numbers
        regex = "(?=(" + '|'.join(digits_together) + "))"
        digits = re.findall(regex, row)

        first = digits[0]
        last = digits[-1]
        first_and_last = first + last

        # Replace words with numbers
        for key, value in DIGITS.items():
            first_and_last = first_and_last.replace(key, value)

        final_digits.append(int(first_and_last))

    return sum(final_digits)


def import_data(path):
    with open(path) as f:
        array = f.read().splitlines()

    return array

if __name__ == '__main__':
    answer = part_1()
    print(f'Answer 1: {answer}')

    answer = part_2()
    print(f'Answer 2: {answer}')
