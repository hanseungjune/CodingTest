first, second = map(str, input().split())

rev_first = ''.join(list(reversed(list(first))))
rev_second = ''.join(list(reversed(list(second))))

if rev_first > rev_second:
    print(rev_first)
else:
    print(rev_second)
