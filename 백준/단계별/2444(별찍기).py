n = int(input())

# 0,1,2,3,4
for i in range(n):
    # n-i : 5,4,3,2,1
    for j in range(n-(i+1)):
        print(' ', end='')
    for k in range(2*(i+1)-1):
        print('*', end='')
    print()
# 0,1,2,3
for a in range(n-1):
    for b in range(a+1):
        print(' ', end='')
    for c in range(2*(n-1)-(2*a+1)):
        print('*', end='')
    print()