import regex as re


with open('./2023/01/data/calibration.txt', 'r') as f:
    messy_coords = f.read().splitlines()

cleaned_coords = []
numbers_pattern = r'(zero|one|two|three|four|five|six|seven|eight|nine|\d+)'


def digit_parser(number: str) -> int:
    number_lookup = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    try:
        int(number)
        print(number, number[0])
        return number[0]  #Need to index incase of multiple digits
    except ValueError:
        return number_lookup[number]


for messy_coord in messy_coords:
    first_digit = ""
    last_digit = ""
    numbers = re.findall(numbers_pattern, messy_coord, overlapped=True)
    first_digit = digit_parser(numbers[0])
    last_digit = digit_parser(numbers[-1])
    cleaned_coords.append(int(first_digit + last_digit))

final_total = sum(cleaned_coords)
print(final_total)
