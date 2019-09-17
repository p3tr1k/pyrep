alpha = 0
digits = 0
spaces = 0
other = 0

with open("data.txt") as f:
    lines = f.readlines()

    for line in lines:
        for c in line:
            if c.isalpha():
                alpha += 1
            elif c.isdigit():
                digits += 1
            elif c.isspace():
                spaces += 1
            else:
                other += 1

print(f"znaky: {alpha}")
print(f"cisla: {digits}")
print(f"medzery: {spaces}")
print(f"ine: {other}")
