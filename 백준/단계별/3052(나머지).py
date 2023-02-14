remain_set = set()

for i in range(10):
  remain_set.add(int(input())%42)

print(len(remain_set))