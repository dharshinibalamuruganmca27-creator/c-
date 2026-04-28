import re

for _ in range(int(input())):
    s = input()
    # Regex: Optional sign, optional digits, must have '.', then at least one digit
    # float(s) ensures it can actually be converted (catches things like '4.0O0')
    try:
        print(bool(re.fullmatch(r'[+-]?\d*\.\d+', s)) and bool(float(s) or True))
    except ValueError:
        print(False)
