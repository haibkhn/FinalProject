n = 4
prev = 1
res = 1
for i in range(2, n + 1):
    prev = prev * 1/i
    res = res + prev
print(res)