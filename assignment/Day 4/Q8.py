data = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

result = []

# Number of tuples
n = len(data)

# Number of elements in each inner tuple
m = len(data[0])

for i in range(m):
    total = 0
    for j in range(n):
        total += data[j][i]
    result.append(total / n)

print(result)