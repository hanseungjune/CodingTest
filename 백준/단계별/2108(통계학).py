from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
  lst.append(int(input()))

def avg(lst):
  return round(sum(lst)/len(lst))

def middle(lst):
  lst.sort()
  return lst[len(lst)//2]


def frequent(lst):
  freq = dict(Counter(lst))

  arr = []
  for key, value in freq.items():
    if value == max(freq.values()):
      arr.append(key)
  
  arr.sort()

  if len(arr) >= 2:
    return arr[1]
  elif len(arr) == 1:
    return arr[0]
  else:
    return 0  

def scope(lst):
  return max(lst) - min(lst)

print(avg(lst))
print(middle(lst))
print(frequent(lst))
print(scope(lst))


