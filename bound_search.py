from typing import List

target = 2
lst = [1, 2, 2, 2, 3, 5]

def bound_search(target: int,
                 lst: List[int],
                 compare,):
    
    lo, hi = 0, len(lst)
    while lo < hi : 
        mid = (lo + hi) // 2
        
        if compare(target, lst[mid]): 
            hi = mid
        else : 
            lo = mid + 1
    print(lo)
    return lo


lower = lambda x, elem: x <= elem
bound_search(target, lst, lower)

upper = lambda x, elem: x < elem
bound_search(target, lst, upper)
