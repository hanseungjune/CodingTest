from collections import Counter;

def solution(s)
    exception = ['', ]
    lst = []
    
    ans = s.replace('{','').replace('}','').replace(',','')
    split_complete = ans.split('')
    
    for i in split_complete
        if i in exception
            continue
        else
            lst.append(i)
    
    ans_dict = dict(Counter(lst))
    sort_dict_list = sorted(ans_dict.items(), key=lambda x x[1], reverse=True)
    
    answer = [int(j[0]) for j in sort_dict_list]
    return answer
