s = input()

# Sort using a custom key that assigns priority to each character type
# Priority: lowercase (0) < uppercase (1) < odd digits (2) < even digits (3)
print("".join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))))
