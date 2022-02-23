details = [
           [1, 'abc', 90],
           [2, 'ijk', 80],
           [3, 'xyz', 70]
        ]
print("{:<10} {:<10} {:<10}" .format('roll no', 'name', 'marks')  )
for x in details:
    for y in x:
       print(y, end=" "*9)
    print()
