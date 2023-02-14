lst = []
for i in range(9):
  lst.append(int(input()))

mx_lst = max(lst)

search_idx = 0
for i in range(9):
  if mx_lst == lst[i]:
    search_idx = i
  else:
    continue

print(mx_lst)
print(search_idx+1) 