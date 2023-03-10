lst = []
for _  in range(5):
  lst.append(int(input()))

sorted_lst = sorted(lst)

print(sum(lst)//5)
print(sorted_lst[2])