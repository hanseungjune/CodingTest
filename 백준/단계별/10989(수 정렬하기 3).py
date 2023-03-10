import sys
input = sys.stdin.readline

# # 퀵 정렬
# def quick(lst):
#   if len(lst) <= 1:
#     return lst
#   pivot = lst[len(lst) // 2]
#   left, mid, right = [], [] ,[]
#   for e in lst:
#     if e < pivot:
#       left.append(e)
#     elif e > pivot:
#       right.append(e)
#     else:
#       mid.append(e)
#   return quick(left) + mid + quick(right)

# n = int(input())
# lst = []
# for _ in range(n):
#   lst.append(int(input()))

# # 퀵정렬 함수 적용하기
# arr = quick(lst)

# for a in arr:
#   print(str(a)+'\n')

n = int(input())
lst = [0] * 10001

for _ in range(n):
    lst[int(input())] += 1

for e in range(10001):
  if lst[e] != 0:
     for k in range(lst[e]):
        print(e)