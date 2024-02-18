nums = [2, 2, 4, 6, 3, 4, 6, 1]
uniques =[]
for x in nums:
    if x not in uniques:
        uniques.append(x)
print(uniques)
