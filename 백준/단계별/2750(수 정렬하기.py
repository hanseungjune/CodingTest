n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if a[min_idx] > a[j]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

for num in a:
    print(num)