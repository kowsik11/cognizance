details = [
           [1, 'abc', 90],
           [2, 'ijk', 80],
           [3, 'xyz', 70]
        ]
print("{:<10} {:<10} {:<10}" .format('roll no', 'name', 'marks')  )
for x in range(0,3):
    print(details[1][x], end=" "*9)
input()