import re


with open('./2023/01/data/calibration.txt', 'r') as f:
    messy_coords = f.read().splitlines()

cleaned_coords = []

for messy_coord in messy_coords:
    first_digit = ""
    last_digit = ""
    splits = re.split(r'(\d+)', messy_coord)
    digits = [s for s in splits if s.isdigit()]
    first_digit = digits[0][0]
    last_digit = digits[-1][-1]
    cleaned_coords.append(int(first_digit + last_digit))

final_total = sum(cleaned_coords)
print(final_total)
