# 5. print the pattern

# No. of rows = 5
row = 5
for i in range(row):
    # Printing spaces
    print(' ' * (row - i - 1), end='')
    # Printing stars
    print('*' * (2 * i + 1))
