import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
arr = sorted(list(set(lst)))
dic = {arr[i]: i for i in range(len(arr))}

for l in lst:
   print(dic[l], end= ' ')


      
