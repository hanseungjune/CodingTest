croatia_lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()

for rep in range(len(croatia_lst)):
    word = word.replace(croatia_lst[rep], '?')

print(len(word))
