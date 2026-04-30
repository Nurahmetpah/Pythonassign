nums = [5, 12, 7, 18, 20]

filtered = list(filter(lambda x: x > 10, nums))
result = list(map(lambda x: x ** 2, filtered))

print(result)
